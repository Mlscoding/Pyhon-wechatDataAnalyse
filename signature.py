from textblob import TextBlob
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='darkgrid', palette='deep')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

with open('english.txt', 'r') as file:
    signatures = file.read()
polarity_scores = []
positive = 0
negative = 0
neutral = 0
for signature in signatures.split('\n'):
    blob = TextBlob(signature)
    polarity_scores.append(blob.sentiment.polarity)
    if blob.sentiment.polarity > 0:
        positive += 1
    elif blob.sentiment.polarity < 0:
        negative += 1
    else:
        neutral += 1

# 使用Seaborn库绘制直方图和KDE曲线
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(polarity_scores, bins=20, color='#4A4A4A', kde=True, ax=ax)

# 添加平均线和标签
mean = sum(polarity_scores) / len(polarity_scores)
ax.axvline(x=mean, color='r', linestyle='--', linewidth=2, label='Mean')
ax.text(mean+0.01, max(ax.get_ylim())/2, f"Mean: {mean:.2f}", fontsize=12, color='r')

plt.xlabel('Polarity score')
plt.ylabel('Frequency')
plt.title('Sentiment Polarity Distribution')
plt.legend()
plt.show()
