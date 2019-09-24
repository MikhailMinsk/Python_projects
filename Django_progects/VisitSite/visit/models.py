from django.db import models


class Skills(models.Model):
    title = models.CharField(max_length=100, verbose_name='title')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
