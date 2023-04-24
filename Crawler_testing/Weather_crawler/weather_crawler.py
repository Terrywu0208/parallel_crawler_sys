import pandas as pd
import os
from datetime import datetime

def weather_crawler(start_date):
    station_name = "ANBU"
    station_num = 466910
    altitude = 837.6
    start_time = start_date.strftime("%Y-%m-%d")
    file = pd.read_html(f"https://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station={station_num}&stname={station_name}&datepicker={start_time}&altitude={altitude}m",encoding="utf-8")
    f_col = [i[2] for i in file[1].columns]
    file[1].columns = f_col
    file[1] = file[1].replace("...","NaN")
    file[1]["Station"] = [station_name]*len(file[1])
    f_col.insert(0,"Station")
    result_df = file[1][f_col]

    return result_df

if __name__ == "__main__":
    final_result = weather_crawler(datetime(2023,3,19))
