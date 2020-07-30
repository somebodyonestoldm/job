from django.db import models

# Create your models here.


class Article(models.Model):
    name= models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)
    visible = models.BooleanField(default=1)
    text = models.TextField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" % (self.id)


class Meta:
    ordering = ["-id", "-timestamp"]
