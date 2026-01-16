from collections import Counter

# -- Theory and explanation --
# streamed_tweets = [
#     {'hashtags': ['#ai', '#python']},
#     {'hashtags': ['#python', '#datascience']},
#     {'hashtags': ['#python']},
#     # ...thousands per minute
# ]

# hashtag_counter = Counter(
#     hashtag
#     for tweet in streamed_tweets
#     for hashtag in tweet['hashtags']
# )

# top_10 = hashtag_counter.most_common(10)
# print(top_10)  # Used for trending bar, analytics dash, alerts

# -- Practice: --
# You’re building a content security dashboard.

# Given a stream of comments, identify:
# The most often reported abusive word(from a set of abusive terms).
# The least frequently reported abusive word.
# If any abusive word crosses 100 mentions, auto-silence related users.

# Input:

# An array of comment dicts: {'user': 'u123', 'text': 'horrible service'}
# A list of abusive words.

# Task:
# 1st
comments = [{'user': 'u123', 'text': 'horrible service'},
            {'user': 'u123', 'text': 'terrible service'},
            {'user': 'u123', 'text': 'bad service'}
            ]
abusive_words = ['horrible', 'terrible', 'bad', 'worst', 'awful']

abusive_counter = Counter(
    val for users in comments for val in users['text'].split() if val in abusive_words
)

print(abusive_counter)
# Second problem solved
if abusive_counter:
    most_common = abusive_counter.most_common(1)[0]  # Tuple (word, count)
    least_common = abusive_counter.most_common()[-1]  # Last tuple
    print('Most common:', most_common)
    print('Least common:', least_common)
else:
    print('No abusive words found.')

# third problem solved
THRESHOLD = 100
# For demo, let's check if any word passed the threshold (real values are small now)
for word, count in abusive_counter.items():
    if count > THRESHOLD:
        print(f"Word '{word}' exceeded {THRESHOLD}! Silencing users...")
