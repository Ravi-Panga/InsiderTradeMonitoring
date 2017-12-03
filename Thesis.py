import nltk
from nltk.corpus import stopwords, state_union
from nltk.tokenize import word_tokenize,PunktSentenceTokenizer
   # unsupervised ml sentence tokenizer
from nltk.stem import PorterStemmer 
from nltk.tag import StanfordPOSTagger
from nltk.data import find



example_sent = "Larsen & Toubro Ltd has informed BSE regarding a Press Release dated March 15, 2016 titled L&T Construction Wins Orders Valued Rs. 1672 Crores."
# Tokenizing
words = word_tokenize(example_sent)
print("Tokensized words =",words)
# stop words elimination
stop_words = set(stopwords.words("english"))
filtered_sentence = [w for w in words if not w in stop_words]
print("Filtering stop words =", filtered_sentence)

ps = PorterStemmer()
example_words =["inform", "informing","informed","information"]

for w in example_words:
    print(ps.stem(w))

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)
# Chunking using regualr expressions
def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # If i want to look for a specific chunk 
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            #print(chunked)
            chunked.draw() # Chunking is grouping of things and Chinking is removal of things

            print(tagged)

    except Exception as e:
        print(str(e))


process_content()
