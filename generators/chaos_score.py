import random
import nltk

def calculate_chaos_score(text):
    """
    Placeholder function to calculate a chaos score for a given text.
    In a real implementation, this would use a more sophisticated
    algorithm to determine the novelty/risk of the content.
    """
    print(f"Calculating chaos score for: {text}")
    return random.randint(1, 10)

def generate_tags(text):
    """
    Generates tags for a given text using NLTK.
    """
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)
    tags = [word for word, pos in tagged if pos in ('NN', 'NNP', 'NNS', 'NNPS')]
    return tags
