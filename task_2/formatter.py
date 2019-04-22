import re
from task_2.stemmer import Stemmer
from pymystem3 import Mystem


class Formatter(object):

    def __init__(self, database_handler):
        self.database_handler = database_handler
        words = self.clear_words(self.gather_words())
        porter_words = self.porter_words(words)
        mystem_words = self.mystem_words(words)
        print(1)

    def gather_words(self):
        words = set()
        articles = self.database_handler.get_articles()
        reg = re.compile('[^A-Za-z0-9А-Яа-я- ]')
        for article in articles:
            article = reg.sub('', article[0])
            article_words = set([
                word.strip().lower() for word in article.split()])
            words.update(article_words)
        return words

    @staticmethod
    def gather_stopwords():
        with open('stopwords.txt', 'r') as stopwords:
            stopwords = set([word.strip() for word in stopwords.readlines()])
        return stopwords

    def clear_words(self, words):
        stopwords = self.gather_stopwords()
        words.difference_update(stopwords)
        return words

    @staticmethod
    def porter_words(words):
        stemmer = Stemmer()
        return list(map(stemmer.stem, words))

    @staticmethod
    def mystem_words(words):
        mystem = Mystem()
        words = ' '.join(words)
        words = mystem.lemmatize(words)
        return [w for w in words if w != ' ']
