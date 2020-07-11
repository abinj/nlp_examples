import nltk
import corenlp

nltk.download('punkt')
from nltk import StanfordNERTagger



# NER Using NLTK
st = StanfordNERTagger('/home/abin/my_works/nlp/stanford-ner-4.0.0/ner-model.ser.gz'
                       , '/home/abin/my_works/nlp/stanford-ner-4.0.0/stanford-ner.jar', encoding='utf-8')
#
text = 'Number of glucocorticoid receptors in lymphocytes and their sensitivity to hormone action.'
#
tokenized_text = nltk.word_tokenize(text)
classified_text = st.tag(tokenized_text)

print(classified_text)



# NER using stanford-corenlp library
# Make sure you have set $CORENLP_HOME as environment variable before start to use Stanford CoreNLPClient

# with corenlp.CoreNLPClient(annotators="ner".split(), memory='2G') as client:
#   ann = client.annotate(text)

# print(ann)



