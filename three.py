import config;
import requests;
import pandas as pd;
import datetime
import numpy as np;


# import requests
# import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = '{}/depth'.format(config.API_BASE_URL);

r = requests.get(url,
	params=dict(symbol='LTCUSD'),
	headers={'X-MBX-APIKEY':config.API_SECRET}
);

results = r.json();

frames = {side: pd.DataFrame(data=results[side], columns=['price', 'quantity'], dtype=float) for side in ['bids', 'asks']};
frames_list = [frames[side].assign(side=side) for side in frames];

data = pd.concat(frames_list, axis='index', ignore_index=True, sort=True);

print('LTCUSD');
print(data);


price_summary = data.groupby('side').price.describe();
price_summary.to_markdown();

print('\n');
print(price_summary);



# fig, ax = plt.subplots()

# # ax.set_title(f"Last update: {t} (ID: {last_update_id})")
# ax.set_title('hello, world!');

# sns.histplot(x="price", hue="side", binwidth=binwidth, data=data, ax=ax)
# sns.rugplot(x="price", hue="side", data=data, ax=ax)

# plt.show()

































