from django.db import models
from django.db.models import permalink

class Base(models.Model):
    """
    Useful default fields
    """
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.title

class Tags(Base):
    """
    Tags for the case
    """

    @permalink
    def get_absolute_url(self):
        return ('case_tag', None, {'slug':self.slug})

    class Meta:
        verbose_name_plural = "Tags"

class Justice(Base):
    """
    The Justice writing the case
    """

    # information about the justice

    @permalink
    def get_absolute_url(self):
        return ('justice', None, {'slug':self.slug})

class Opinion(Base):
    """
    One of the opinions for the case
    """

    writtenBy = models.ManyToManyField(Justice)

    @permalink
    def get_absolute_url(self):
        return ('opinion', None, {'slug':self.slug})

class Case(Base):
    """
    The Case
    """

    # decisionDate = models.DateField()
    # citationRank = models.IntegerField()
    tags = models.ManyToManyField(Tags)
    opinions = models.ManyToManyField(Opinion)

    @permalink
    def get_absolute_url(self):
        return '%s' % self.title
