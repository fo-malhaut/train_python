import pandas as pd

infile = "data/2327/stock_2327_2017.csv"
outfile = "code_2327_plus.csv"
path = "/Users/s.watanabe/Desktop/develop app/predict_stock/data"

df = pd.read_csv(infile, header=0)
df.columns = ["Date", "Open", "High", "Low", "Close", "Volume",
              "Trading Value"]
df["index"] = [i for i in range(len(df))]

etf_list = [
 # 上海株式指数・上証50連動型上場投資信託
 1309,
 # サムスンKODEX200証券上場指数投資信託
 1313,
 # 上場インデックスファンド中国A株（パンダ）CSI300
 1322,
 # SPDRゴールド・シェア
 1326,
 # NEXT FUNDS 東証REIT指数連動型上場投信
 1343,
 # 純パラジウム上場信託（現物国内保管型）
 1543,
 # JASDAQ-TOP20上場投信
 1551,
 # NEXT FUNDS 不動産（TOPIX-17）上場投信
 1633,
 # ETFS 銀上場投資信託
 1673,
 # NEXT FUNDS インド株式指数・Nifty 50連動型上場投信
 1678,
 # 上場インデックスファンド海外新興国株式（MSCIエマージング）
 1681,
 # NEXT FUNDS 日経・東商取白金指数連動型上場投信
 1682,
 # 上場インデックスファンド日本高配当（東証配当フォーカス100）
 1698
]
for etf in etf_list:
    file = "%s/%s/stock_%s_2017.csv" % (path, etf, etf)
    # データ読み込み
    df_etf = pd.read_csv(file, header=0)
    df_etf.columns = ["Date", "Open", "High", "Low", "Close", "Volume",
                      "Trading Value"]
    dates = []
    closeis = []
    count = 0
    fc = 1
    for d in df["Date"]:
        date = df_etf.loc[(df_etf.Date == d), "Date"]
        try:
            yesterday_date = date.values[0]
            dates.append(date.values[0])
        except IndexError:
            dates.append(yesterday_date)
# 日付が一致した日のETFのCloseのデータを取り出す
        close = df_etf.loc[(df_etf.Date == d), "Close"]
        try:
            yesterday_close = close.values[0]
            for i in range(fc):
                closeis.append(close.values[0])
            count = count + 1
            fc = 1
        except IndexError:
            if count != 0:
                closeis.append(yesterday_close)
            else:
                fc = fc + 1

    # df_etf2 = pd.DataFrame({"Date_" + str(etf): dates, "Close_" +
    #                        str(etf): closeis})
    # 新しくデータフレームを作成
    df_etf2 = pd.DataFrame({"Close_" + str(etf): closeis})
    # データとETFデータを統合
    df = pd.concat([df, df_etf2], axis=1)
    df["diff_" + str(etf)] = (df["Close_" + str(etf)] / df["Close_" +
                              str(etf)].shift(-1)) - 1

out = "%s/%s" % (path, outfile)
df.to_csv(out)
