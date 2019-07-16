import pandas as pd
from sklearn.ensemble import RandomForestClassifier

path = "/Users/s.watanabe/Desktop/develop app/predict_stock/data"
file = "code_2327_plus.csv"
filepath = "%s/%s" % (path, file)
df = pd.read_csv(filepath, header=0)

# はじまりを[1:]としているのは、階差系列をとっているため[1]がNaNデータ。
df_train = df.iloc[1:len(df)-2]
# 学習データにNaNデータがあると、エラー。
df_test = df.iloc[len(df)-2:len(df)-1]

xlist = [
  # 上海株式指数・上証50連動型上場投資信託
  "diff_1309",
  # サムスンKODEX200証券上場指数投資信託
  "diff_1313",
  # 上場インデックスファンド中国A株（パンダ）CSI300
  "diff_1322",
  # SPDRゴールド・シェア
  "diff_1326",
  #  NEXT FUNDS 東証REIT指数連動型上場投信
  "diff_1343",
  # 純パラジウム上場信託（現物国内保管型）
  "diff_1543",
  # JASDAQ-TOP20上場投信
  "diff_1551",
  #  NEXT FUNDS 不動産（TOPIX-17）上場投信
  "diff_1633",
  # ETFS 銀上場投資信託
  "diff_1673",
  # NEXT FUNDS インド株式指数・Nifty 50連動型上場投信
  "diff_1678",
  # 上場インデックスファンド海外新興国株式（MSCIエマージング）
  "diff_1681",
  # NEXT FUNDS 日経・東商取白金指数連動型上場投信
  "diff_1682",
  # 上場インデックスファンド日本高配当（東証配当フォーカス100）
  "diff_1698"
]

x_train = []
y_train = []
for s in range(0, len(df_train) - 1):
    x_train.append(df_train[xlist].iloc[s])
    if df_train["Close"].iloc[s + 1] > df_train["Close"].iloc[s]:
        y_train.append(1)
    else:
        y_train.append(-1)

rf = RandomForestClassifier(n_estimators=len(x_train), random_state=0)
rf.fit(x_train, y_train)

test_x = df_test[xlist].iloc[0]
test_y = rf.predict(test_x.values.reshape(1, -1))
print(test_y)
