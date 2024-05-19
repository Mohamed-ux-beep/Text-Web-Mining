from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def my_nltk_tokenizer(doc):
    stopwörter = list(set(stopwords.words('english')))
    ps = PorterStemmer()
    tokens_lis = word_tokenize(doc, language='english') 
    tokens_lis = [element.lower() for element in tokens_lis if element.isalnum()]
    tokens_lis = [element for element in tokens_lis if element not in stopwörter]
    tokens_lis = [ps.stem(element) for element in tokens_lis]
    return  tokens_lis