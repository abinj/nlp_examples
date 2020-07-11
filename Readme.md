* Prerequisites

1) Download Stanford CORENLP stable release jar file from https://stanfordnlp.github.io/CoreNLP/index.html

# Start the CoreNLP server
2) java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

# To train a new NER model
# The dataset can be download from http://www.geniaproject.org/shared-tasks/bionlp-jnlpba-shared-task-2004
# To refer more about model training, go to: https://stanfordnlp.github.io/CoreNLP/ner.html
java -mx4g -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop /home/abin/my_works/github_works/nlp_examples/train/genia4er.prop

