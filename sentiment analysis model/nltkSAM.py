import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text=open("data.txt",encoding="utf-8").read().lower()
cleaned=text.translate(str.maketrans('','',string.punctuation))
tokenised=word_tokenize(cleaned,"english")

final=[]
for word in tokenised:
    if word not in stopwords.words('english'):
        final.append(word)

emotion_list=[]
with open("emotions.txt",'r') as file:
    for line in file:
        clearline=line.replace('\n','').replace(',','').replace("'",'').strip()       
        word, emotion=clearline.split(': ')
        if word in final:
            emotion_list.append(emotion)


print(emotion_list,'\n')
data=Counter(emotion_list)
print(data)

def sentimentanalyze(sentimenttext):
    score = SentimentIntensityAnalyzer().polarity_scores(sentimenttext)
    print(score)
    # neg=score['neg']
    # neu=score['neu']
    # pos=score['pos']
    # compound=score['compound']
    

sentimentanalyze(cleaned)

fig, ax1=plt.subplots()
ax1.bar(data.keys(),data.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show