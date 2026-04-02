from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

import pandas as pd
from plotnine import ggplot, aes, geom_line, geom_point
from plotnine.themes import theme_minimal


df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")

y = df["mpg"]
X = df[["weight"]]

mpgWtDf = df[["weight", "mpg"]]

model = LinearRegression().fit(X, y)

# noinspection PyUnresolvedReferences
print(model.coef_[0])
print(model.intercept_)


print(r2_score(
    y_true=df["mpg"],
    y_pred=model.predict(df[["weight"]])
))

df["fitted"] = model.predict(df[["weight"]])

ggplot(aes('weight', 'mpg'), mpgWtDf) \
    + geom_point(alpha=0.5, color="#000000") \
    + geom_line(aes(y = "fitted"), color = "blue") \
    + theme_minimal()
