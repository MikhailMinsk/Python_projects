from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class BlogPostQS(models.QuerySet):
    def published(self):
        now = timezone.now()
        # Blog.objects.all().filter(...
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(slug__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__username__icontains=query)
        )
        return self.filter(lookup)


class BlogPostManager(models.Manager):
    def get_queryset(self):
        return BlogPostQS(self.model, using=self._db)

    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().published().search(query)


class Blog(models.Model):
    user = models.ForeignKey(User, default=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, unique=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = BlogPostManager()

    def __str__(self):
        return '{}.{}'.format(self.user, self.title)

    def get_absolute_url(self):
        return '{}'.format(self.slug)

    # def get_edit_url(self):
    #     return '{}/update/'.format(self.get_absolute_url())
    #
    # def get_delete_url(self):
    #     return '{}/delete/'.format(self.get_absolute_url())

    class Meta:
        ordering = ['-publish_date', '-updated', 'time_stamp']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
