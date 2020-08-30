from sklearn.datasets import fetch_20newsgroups
from top2vec import Top2Vec
import numpy as np

news_groups_train = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
# news_groups_documents = news_groups_train[]


model = Top2Vec(documents=news_groups_train.data[0:2000], use_corpus_file=True, speed='fast-learn', workers=8)
print("Number of Topics:- ", model.get_num_topics())
# Get Topic Sizes
topic_sizes, topic_nums = model.get_topic_sizes()
for i in range(len(topic_nums)):
    print(str(topic_nums[i]) + ":- " + str(topic_sizes[i]))

# Get Topics
topic_words, word_scores, topic_nums = model.get_topics()
for i in range(len(topic_nums)):
    print(str(topic_nums[i]) + ": " + str(topic_sizes[i]) + ": " + str(topic_words[i]))

# topic_words, word_scores, topic_scores, topic_nums = model.search_topics(keywords=["medicine"], num_topics=5)
# for i in range(topic_nums):
#     print

print("Done!!!!")




