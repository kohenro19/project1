### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
import csv
def readCsv():
    with open("characterList.csv", encoding="utf-8") as f:
        reader = csv.reader(f)
        for csvData in reader:
            return csvData
        
### 検索ツール
def search():

            word =input("鬼滅の登場人物の名前を入力してください >>> ")

            ### ここに検索ロジックを書く
            source = []
            source = readCsv()
            if word in source:
                print("{}が見つかりした".format(word))

            else:
                print("{}を登録しやす".format(word))
                with open("characterList.csv", mode='a', encoding="utf-8") as f:
                    f.write(","+word)
                    f.close
        
if __name__ == "__main__":
    search()
