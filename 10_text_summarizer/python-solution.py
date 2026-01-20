text = input("Enter text:\n")

sentences = text.split(".")
word_freq = {}

for sentence in sentences:
    for word in sentence.lower().split():
        word_freq[word] = word_freq.get(word, 0) + 1

sentence_scores = {}

for sentence in sentences:
    score = 0
    for word in sentence.lower().split():
        score += word_freq.get(word, 0)
    sentence_scores[sentence] = score

summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:2]

print("\nSummary:")
for s in summary:
    if s.strip():
        print(s.strip() + ".")
