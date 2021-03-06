from django.db import models
from django.utils import timezone
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your models here.
class Title( models.Model ):

    number = models.IntegerField(
        primary_key = True,
    )

    date = models.DateField(
        blank = False,
    )

    name = models.CharField(
        blank = False,
        max_length = 100,
    )

    def __unicode__(self):
        return "Title %d: %s" % (self.number, self.name)

    def get_absolute_url(self):
        return reverse(
            'legislation.views.view_title',
            args=[str(self.number)]
        )

    class Meta:
        ordering = ['number']

class Chapter( models.Model ):

    number = models.IntegerField(
        blank = False,
    )

    date = models.DateField(
        blank = False,
    )

    name = models.CharField(
        max_length = 100,
        blank = False,
    )

    title = models.ForeignKey(
        Title,
    )

    def __unicode__(self):
        return "Title %d.%d: %s" % (self.title.number,
                                    self.number,
                                    self.name)

    def get_absolute_url(self):
        return reverse(
            'legislation.views.view_title',
            args=[str(self.title.number)]
        )

    class Meta:
        ordering = ['number']

class Section( models.Model ):
 
    number = models.IntegerField(
        blank = False,
    )

    date = models.DateField(
        blank = False,
    )

    name = models.CharField(
        blank = False,
        max_length = 100,
    )

    text = models.TextField(
        blank = False,
    )

    chapter = models.ForeignKey(
        Chapter,
    )

    def __unicode__(self):
        return "Title %d.%d.%d: %s" % (self.chapter.title.number,
                                       self.chapter.number,
                                       self.number,
                                       self.name)

    def get_absolute_url(self):
        return reverse(
            'legislation.views.view_title',
            args=[str(self.chapter.title.number)]
        )

    class Meta:
        ordering = ['number']
