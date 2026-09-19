from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Status(models.TextChoices):
        NEW = 'NEW', 'Новое'
        IN_PROGRESS = 'In Progress', 'В выполнении'
        COMPLETED = 'Completed', 'Выполнено'

class Task(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
        category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
        tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.title



