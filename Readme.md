* Prerequisites

1) Download Stanford CORENLP stable release jar file from
https://stanfordnlp.github.io/CoreNLP/index.html

# Start the CoreNLP server
2) java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000

# To train a new NER model
# The dataset can be download from
http://www.geniaproject.org/shared-tasks/bionlp-jnlpba-shared-task-2004
# To refer more about model training, go to:
https://stanfordnlp.github.io/CoreNLP/ner.html
java -mx4g -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -prop <path/to/.prop/file/for/training>

# To evaluate the trained model
java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier <path/to/trained/model> -testFile <path/to/test/file>