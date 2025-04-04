# import os
# import math

# def clean_words(text):
#     res = ""
#     for word in text.split():
#         w = ""
#         for char in word:
#             if char.isalpha():
#                 w += char.lower()
#         res += w + " "
#     return res.strip()

# # Map filenames to their full play titles
# # play_files = {
# #     "ado.txt": "Much Ado About Nothing",
# #     "hamlet.txt": "THE TRAGEDY OF HAMLET, PRINCE OF DENMARK",
# #     "lear.txt": "THE TRAGEDY OF KING LEAR",
# #     "macbeth.txt": "MACBETH",
# #     "merchant.txt": "THE MERCHANT OF VENICE",
# #     "midsummer.txt": "A MIDSUMMER NIGHT’S DREAM",
# #     "othello.txt": "OTHELLO, THE MOOR OF VENICE",
# #     "romeo.txt": "TRAGEDY OFROMEO AND JULIET",
# #     "tempest.txt": "THE TEMPEST",
# #     "twelfth.txt": "TWELFTH NIGHT: OR, WHAT YOU WILL"
# # }



# play_files = {
#     "ado.txt": "Much Ado About Nothing",
#     "hamlet.txt": "Hamlet",
#     "lear.txt": "King Lear",
#     "macbeth.txt": "Macbeth",
#     "merchant.txt": "The Merchant of Venice",
#     "midsummer.txt": "A Midsummer Night's Dream",
#     "othello.txt": "Othello",
#     "romeo.txt": "Romeo and Juliet",
#     "tempest.txt": "The Tempest",
#     "twelfth.txt": "Twelfth Night"
# }


# # Build bag-of-words model for each play
# bow_models = {}
# total_words_per_play = {}
# vocabulary = set()

# for filename, play_name in play_files.items():
#     word_counts = {}
#     total_words = 0
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             line = clean_words(line)
#             for word in line.split():
#                 total_words += 1
#                 word_counts[word] = word_counts.get(word, 0) + 1
#                 vocabulary.add(word)
#     bow_models[play_name] = word_counts
#     total_words_per_play[play_name] = total_words

# vocab_size = len(vocabulary)

# # Read and clean the input sentence
# sentence = input()
# sentence = clean_words(sentence)
# words = sentence.split()

# # Apply Naive Bayes classification using log probabilities and Laplace smoothing
# best_score = float('-inf')
# best_play = None

# for play_name in play_files.values():
#     word_counts = bow_models[play_name]
#     total_words = total_words_per_play[play_name]

#     log_prob = 0
#     for word in words:
#         count = word_counts.get(word, 0)
#         # Laplace smoothing
#         prob = (count + 1) / (total_words + vocab_size)
#         log_prob += math.log(prob)

#     if log_prob > best_score:
#         best_score = log_prob
#         best_play = play_name

# # Output the most likely play
# print(best_play)





import os
import math
import sys
from collections import Counter, defaultdict

def clean_words(text):
    res = []
    for word in text.strip().split():
        cleaned = ''.join(c.lower() for c in word if c.isalpha())
        if cleaned:
            res.append(cleaned)
    return res

# Map filenames to the expected play names
play_files = {
    "ado.txt": "Much Ado About Nothing",
    "hamlet.txt": "Hamlet",
    "lear.txt": "King Lear",
    "macbeth.txt": "Macbeth",
    "merchant.txt": "The Merchant of Venice",
    "midsummer.txt": "A Midsummer Night's Dream",
    "othello.txt": "Othello",
    "romeo.txt": "Romeo and Juliet",
    "tempest.txt": "The Tempest",
    "twelfth.txt": "Twelfth Night"
}

# Step 1: Build bag-of-words for each play
play_word_counts = {}
play_total_words = {}
vocab = set()

for file, play_name in play_files.items():
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        words = clean_words(text)
        counts = Counter(words)
        play_word_counts[play_name] = counts
        play_total_words[play_name] = sum(counts.values())
        vocab.update(counts.keys())

V = len(vocab)

# Step 2: Read and clean input sentence
sentence = input().strip()
sentence_words = clean_words(sentence)

# Step 3: Score each play using log-probabilities (with Laplace smoothing)
scores = {}

for play in play_files.values():
    log_prob = 0
    word_counts = play_word_counts[play]
    total_words = play_total_words[play]
    for word in sentence_words:
        word_freq = word_counts.get(word, 0)
        log_prob += math.log((word_freq + 1) / (total_words + V))
    scores[play] = log_prob

# Step 4: Output the most likely play
best_play = max(scores, key=scores.get)
print(best_play)
