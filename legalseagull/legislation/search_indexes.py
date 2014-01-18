from haystack import indexes
from django.utils import timezone
from legislation.models import Title, Chapter, Section

class TitleIndex(indexes.SearchIndex, indexes.Indexable):

    # search results
    # there can be only one document=True per model
    text = indexes.CharField( document=True, use_template=True )
    # the use_template is in the app directory, just a text file
    # with the fields that we want to display when returning results

    # search filtering
    name = indexes.CharField( model_attr = 'name' )

    def get_model(self):
        return Title

    def index_queryset(self, using=None):
        """When the entire index for model is updated."""
        return self.get_model().objects.all()

class ChapterIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField( document=True, use_template=True )
    name = indexes.CharField( model_attr = 'name' )

    def get_model(self):
        return Chapter

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

class SectionIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField( document=True, use_template=True )
    name = indexes.CharField( model_attr = 'name' )
    contents = indexes.CharField( model_attr = 'text' )

    def get_model(self):
        return Section
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
