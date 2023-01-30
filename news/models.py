from django.db import models


# from django_quill.fields import QuillField


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.name
        super(Category, self).save(force_insert=False, force_update=False, using=None, update_fields=None)


class News(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # content = QuillField()
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
