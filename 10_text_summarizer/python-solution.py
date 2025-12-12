from collections import Counter
import re

text = input("Enter text: ")
words = re.findall(r'\w+', text.lower())
freq = Counter(words)
keywords = [w for w,_ in freq.most_common(5)]
print("Top keywords:", keywords)

sentences = re.split(r'(?<=[.!?]) +', text)
sent_scores = [(s,sum(freq[w.lower()] for w in re.findall(r'\w+',s))) for s in sentences]
summary = sorted(sent_scores, key=lambda x:x[1], reverse=True)[:3]
print("\nSummary:")
for s,_ in summary: print(s)
