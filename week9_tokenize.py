from  nltk.tokenize import sent_tokenize, word_tokenize, WordPunctTokenizer
input_text = "Many researchers investigated the effects of enough sleep. As demonstrated by studies, enough sleep change the quality of life in a good way."
print("\nSentence Tokenizer:")
print(sent_tokenize(input_text)) 
print("\nWord tokenizer : ")
print(word_tokenize(input_text)) 
print("\nWord Punct Tokenizer : ")
print(WordPunctTokenizer().tokenize(input_text))
