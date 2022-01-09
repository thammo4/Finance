import config;
import requests;
import pandas as pd;
import datetime
import numpy as np;
import os;
import sys;
from datetime import datetime as dt;



API_BASE_URL = 'https://api.binance.us/api/v3';

API_KEY = '...';
API_SECRET = '...';


ENDPOINT_TICKER_PRICE = "/ticker/price";