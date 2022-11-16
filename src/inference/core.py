"""A core module to process input text
"""

from src.inference.coreference_resolution import get_coref_resolution
from src.inference.information_extraction import triple_generation
from src.inference.sentiment_classification import (
    EmbeddingHuggingFacePredictor,
)
from src.inference.custom_ner_spacy import SpacyNerPredictor
from src.inference.elasticsearch_engine import ElasticSearchEngine
from src.inference.topic_modeling import BertTopicModel

topic_modeling = BertTopicModel()
sentiment_classifier = EmbeddingHuggingFacePredictor()
spacy_ner = SpacyNerPredictor()
search_engine = ElasticSearchEngine()


def generate_output(text):
    """A method to generate output

    Args:
        text (str): Input text

    Returns:
        Dataframe: All NLP output
    """

    # Get relevant news articles basedon input queryfrom existing news articles knowledge base
    news_data_df = search_engine.get_model_output(text, search_results_limit=3)

    # Sentiment classification  of a article
    news_data_df["sentiment"] = news_data_df["article_text"].apply(
        sentiment_classifier.get_model_output
    )
    news_data_df["sentiment"] = news_data_df["sentiment"].apply(
        sentiment_classifier.map_output
    )

    # Custom NER
    news_data_df["ner"] = news_data_df["article_text"].apply(
        spacy_ner.get_model_output
    )

    # Coreference REsolution
    news_data_df["resolved_text"] = news_data_df["article_text"].apply(
        get_coref_resolution
    )

    # Relationship Extraction
    news_data_df["relationships"] = news_data_df["resolved_text"].apply(
        triple_generation
    )

    # Topic Modeling
    news_data_df["topics"] = news_data_df["article_text"].apply(
        topic_modeling.get_model_output
    )

    return news_data_df
