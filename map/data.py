# coding=utf-8
import requests as req
import pandas as pd
import csv
import json

url = "https://data.ntpc.gov.tw/api/datasets/8AE8F5DF-EDB7-4650-9C73-1F36405ADD67/csv/file"


def CSVdownload(url):  # 從URL下載CSV
    file = req.get(url, allow_redirects=True)
    with open('download.csv', 'wb')as fw:
        fw.write(file.content)


def DataProcessing():
    data = pd.read_csv('download.csv')  # 讀入CSV

    # data.rename(columns={"district": "鄉鎮市區", "rps01": "交易標的", "rps02": "土地區段位置建物區段門牌", "rps03": "土地面積平方公尺",
    #            "rps04": "都市土地使用分區", "rps05": "非都市土地使用分區", "rps06": "非都市土地使用編定,", "rps07": "租賃年月日", "rps08": "租賃筆棟數", "rps09": "租賃層次", "rps10": "總樓層數", "rps11": "建物型態", "rps12": "主要用途", "rps13": "主要建材", "rps14": "建築完成年月", "rps15": "建物總面積平方公尺", "rps16": "建物現況格局-房", "rps17": "建物現況格局-廳", "rps18": "建物現況格局-衛", "rps19": "建物現況格局-隔間", "rps20": "有無管理組織", "rps21": "有無附傢俱", "rps22": "總額元", "rps23": "單價元平方公尺", "rps24": "車位類別", "rps25": "車位面積平方公尺", "rps26": "車位總額元", "rps27": "備註", "rps28": "編號"}, inplace=True)  # 重新命名欄位

    data = data.iloc[:, [2, 22]]  # 讀取特定欄位
    # print(data)

    data.to_csv("DataProcessing.csv")


def csv_to_json():
    jsonArray = []
    # read csv file
    with open('DataProcessing.csv', encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open('DataProcessing.json', 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4, ensure_ascii=False)
        jsonf.write(jsonString)


CSVdownload(url)  # 根據URL將CSV下載
DataProcessing()  # 只留下感興趣的資料
csv_to_json()  # 將CSV轉成json
