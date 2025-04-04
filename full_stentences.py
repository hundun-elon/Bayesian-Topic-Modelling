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

# Step 3: Calculate the numerator (log(P(W|S=Ck)*P(S=Ck))) for each play
num_plays = len(play_files)
log_prior = math.log(1 / num_plays)  # Uniform prior

log_numerators = {}

for play in play_files.values():
    log_numerator = log_prior  # Start with uniform prior
    word_counts = play_word_counts[play]
    total_words = play_total_words[play]
    
    # Add log-likelihood for each word
    for word in sentence_words:
        count = word_counts.get(word, 0)
        prob = (count + 1) / (total_words + V)  # Laplace smoothing
        log_numerator += math.log(prob)
    
    log_numerators[play] = log_numerator

# Step 4: Calculate the denominator using the log-sum-exp trick
A = max(log_numerators.values())
log_denominator = A + math.log(sum(math.exp(log_num - A) for log_num in log_numerators.values()))

# Step 5: Calculate posterior probabilities
probabilities = {}
for play, log_numerator in log_numerators.items():
    log_posterior = log_numerator - log_denominator
    posterior = math.exp(log_posterior)
    probabilities[play] = posterior

# Step 6: Format and output the results
# Sort plays by probability (descending)
sorted_plays = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)

# Print probabilities (rounded to nearest whole percentage)
for play, prob in sorted_plays:
    percentage = round(prob * 100)
    print(f"{play}: {percentage}%")