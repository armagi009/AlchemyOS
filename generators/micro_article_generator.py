from generators.chaos_score import generate_tags

def create_micro_article(text):
    """
    Placeholder function to generate a micro-article from text.
    In a real implementation, this would use an AI API to summarize
    and format the text into a micro-article.
    """
    print(f"Generating micro-article from: {text}")
    tags = generate_tags(text)
    return {
        "content": f"This is a micro-article based on the text: '{text}'",
        "tags": tags
    }

def weave_knowledge_graph(articles):
    """
    Weaves a knowledge graph by linking related articles.
    """
    for i, article in enumerate(articles):
        article['related_articles'] = []
        for j, other_article in enumerate(articles):
            if i == j:
                continue
            shared_tags = set(article['tags']) & set(other_article['tags'])
            if len(shared_tags) > 0:
                article['related_articles'].append(other_article['id'])
    return articles
