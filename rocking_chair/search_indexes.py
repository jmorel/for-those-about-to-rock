import datetime
from haystack import indexes
from rocking_chair.models import RockingChair


class RockingChairIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # manufacturer = indexes.CharField(model_attr='manufacturer')
    # designers = indexes.CharField(model_attr='designers')
    published_at = indexes.DateTimeField(model_attr='published_at')

    def get_model(self):
        return RockingChair

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published_at__lte=datetime.datetime.now())