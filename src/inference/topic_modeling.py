"""A module to load model and get topics.

"""


from bertopic import BERTopic


class BertTopicModel:
    """A class to load model and get output"""

    model = None

    def get_model(self):
        """A method to load model

        Returns:
            model: trained model
        """

        if self.model is None:
            self.model = BERTopic.load("src/models/BERTopic_model")
        return self.model

    def get_model_output(self, input_data):
        """A method to get model output from given text input
        Args:
            input_data (text):input text data

        Returns:
            topic_words: model prediction
        """
        topics, _ = self.get_model().transform(input_data)
        # Get top topic
        words_tf_idf = self.get_model().get_topic(topics[0])

        topic_words = [word for word, _ in words_tf_idf]

        return topic_words
