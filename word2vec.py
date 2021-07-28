import spacy
nlp = spacy.load("en_core_web_sm", disable=['parser', 'ner'])

# Get w2v representation of the word 'breakfast'
print (nlp('breakfast').vector.size)

# Find cosine similarity between w2v representations of breakfast and universe
nlp('breakfast').similarity(nlp('universe')) 

#to find similarity between two sentences
doc1 = nlp("I like apples")
doc2 = nlp("I like watermelon")
doc1.similarity(doc2)     
