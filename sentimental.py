from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

df = pd.read_csv("History_data.csv", encoding='cp1252')
analyzer = SentimentIntensityAnalyzer()

Negative = []
Neutral = []
Positive = []

for i in range(df.shape[0]):
    title = df.iloc[i, 0]
    context = df.iloc[i, 2]
    title_analyzed = analyzer.polarity_scores(title)
    context_analyzed = analyzer.polarity_scores(context)

    Negative.append(((title_analyzed['neg']) + (context_analyzed['neg'])) / 2)
    Neutral.append(((title_analyzed['neu']) + (context_analyzed['neu'])) / 2)
    Positive.append(((title_analyzed['pos']) + (context_analyzed['pos'])) / 2)


df['Negative'] = Negative
df['Neutral'] = Neutral
df['Positive'] = Positive


pd.set_option('display.max_columns',None)

print(df.head())

print(df["Negative"].mean())
print(df["Neutral"].mean())
print(df["Positive"].mean())