# Text-Vectorization-using-Word2Vec

Word vectorization is used for the following cases:

Word prediction
To find word similarities/semantics

After converting into corresponding vectors, we use cosine similarities to identify the similar words.We wont use Euclidean distance here because in Euclidean distance, we can only find similar words in a single document whereas we use cosine similarity to find the similarity of words in different documents.

Word2Vec is used to create word embeddings in the field of Natural Language Processing (NLP).It was developed at Google in 2013 by Tomas Mikolov and his team.Word2vec takes in words from a large corpus of texts as input and learns to give out their vector representation.
Word2Vec works in the same way as CNN, like they extract features from images, Word2Vec creates vectors that represent a word in the vector space.We use the help of cosine similarity function .similarity()

If the cosine similarity is 1, it means that the angle between the words is zero hence the words are same.If the cosine similarity is close to 1, say 0.7–0.9 we can conclude that the words are similar.

The algorithm uses a neural network architecture that consists of two learning models:

Continuous Bag-of-Words model (CBOW)
In this approach, the model uses context words to predict the target words. The input may be a group of words or a single word. It predicts a missing word given a window of context words or word sequence.

Suppose we have the sentence: An apple is green in color. If we remove the word “green” from the sentence and leave it blank, the model should predict the missing word.

Skip-gram model
Predict vector representation of window of context words based on center/target word
Use python’s spacy package since it provides pre-trained models so that we can see how Word2Vec works.
