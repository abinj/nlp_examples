import nltk
import corenlp

# nltk.download('punkt')
from nltk import StanfordNERTagger, word_tokenize



# NER Using NLTK
# st = StanfordNERTagger('/home/abin/my_works/nlp/stanford-ner-4.0.0/classifiers/english.all.3class.distsim.crf.ser.gz'
#                        , '/home/abin/my_works/nlp/stanford-ner-4.0.0/stanford-ner.jar', encoding='utf-8')
#
text = 'While in France, Christine Lagarde discussed short-term stimulus efforts in a recent interview with the Dexlock.'
#
# tokenized_text = word_tokenize(text)
# classified_text = st.tag(tokenized_text)
#
# print(classified_text)



# NER using stanford-corenlp library
# Make sure you have set $CORENLP_HOME as environment variable before start to use Stanford CoreNLPClient

with corenlp.CoreNLPClient(annotators="ner".split(), memory='2G') as client:
  ann = client.annotate(text)

print(ann)



