from django.db import models
from django.db.models import permalink
from django.core.urlresolvers import reverse
# from django.template.defaultfilters import slugify

class Base(models.Model):
    """
    Useful default fields
    """
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50, unique=True)
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.name

    # def save(self):
        # self.slug = slugify(self.name)
        # super(Base, self).save()

class Tags(Base):
    """
    Tags for the case
    """

    @permalink
    def get_absolute_url(self):
        return reverse(
            'courts.views.tags',
            args=[str(self.slug)]
        )

    class Meta:
        verbose_name_plural = "Tags"

class Justice(Base):
    """
    The Justice writing the case
    """

    # information about the justice

    @permalink
    def get_absolute_url(self):
        return reverse(
            'courts.views.justice',
            args=[str(self.slug)]
        )

class Opinion(Base):
    """
    One of the opinions for the case
    """

    writtenBy = models.ManyToManyField(Justice, related_name="opinions")
    contents = models.TextField()
    case = models.ForeignKey( 'Case' )

    @permalink
    def get_absolute_url(self):
        return reverse(
            'courts.views.opinion',
            args=[str(self.slug)]
        )

class Case(Base):
    """
    The Case
    """

    decisionDate = models.DateField(blank=False)
    # citationRank = models.IntegerField()
    tags = models.ManyToManyField(Tags)

    @permalink
    def get_absolute_url(self):
        return reverse(
            'courts.views.case',
            args=[str(self.slug)]
        )
