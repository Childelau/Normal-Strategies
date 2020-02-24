import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import baostock as bs
import datetime
from datetime import datetime
import os
import warnings;warnings.simplefilter('ignore')
bs.login()


file_path = os.getcwd()
new_file_path = file_path+'\\'
print(file_path,new_file_path)

#================
def download_data(date):
    file_path = os.getcwd() + '\\result.csv'
    # 获取指定日期的指数、股票数据
    stock_rs = bs.query_all_stock(date)
    stock_df = stock_rs.get_data()
    data_df = pd.DataFrame()
    for code in stock_df["code"]:
        k_rs = bs.query_history_k_data_plus(code, "date,code,open,high,low,close", date, date)
        data_df = data_df.append(k_rs.get_data())
    data_df.to_csv(file_path)
    return data_df



#
def stocks_filter():
    today = datetime.now().strftime('%Y-%m-%d')
    test1 = bs.query_history_k_data_plus('sz.000001','open',today,today).get_data()
    if len(test1) != 1:
        print(22222)
        return False
    #获得今日的股票
    stocks_data = download_data(today)
    print(stocks_data)


stocks_filter()







