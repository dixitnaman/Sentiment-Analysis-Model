import string
from collections import Counter
import matplotlib.pyplot as plt

text=open("data.txt",encoding="utf-8").read().lower()
cleaned=text.translate(str.maketrans('','',string.punctuation))
tokenised=cleaned.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final=[]
for word in tokenised:
    if word not in stop_words:
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

fig, ax1=plt.subplots()
ax1.bar(data.keys(),data.values())
fig.autofmt_xdate()
plt.savefig("graph.png")
plt.show