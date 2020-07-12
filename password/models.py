from django.db import models


class Password(models.Model):
    web_url = models.URLField()
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=35, null=True)
    

    def __str__(self):
        return self.web_url

    class Meta:
        ordering = ('web_url',)
