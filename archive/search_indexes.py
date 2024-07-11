from haystack import indexes
from .models import Book

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    world = indexes.CharField(model_attr='world')
    genre = indexes.CharField(model_attr='genre')

    def get_model(self):
        return Book