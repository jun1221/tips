# ファイル名がテーブル名
# ヘッダあり

import pandas as pd

# csvファイル名
fromCsvPath = "./insertData.csv"
# insert文のひな型
insertTemplate = "insert into %s %s";

def main():
    # ヘッダを取得する
    df = pd.read_csv(fromCsvPath)
    header = ",".join(df.columns.values)
    insertData=""
    # カラムを取得する
    for item in df.values:
        itemStr=[str(n) for n in item.tolist()]
        insertData += "insert into ({0}) values({1})".format(header, ",".join(itemStr))+"\n"
    
    print(insertData)

main()