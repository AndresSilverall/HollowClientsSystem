from django.db import models


# Create your models here.
class TasksManagement(models.Model):

    class Priority(models.TextChoices):
        NORMAL = "N", "NORMAL"
        MEDIANA = "M", "MEDIANA"
        ALTA = "A", "ALTA"


    name = models.CharField("task name", max_length=20, null=False)
    author = models.CharField("author", max_length=20, null=False)
    description = models.TextField("description", max_length=50)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    status = models.BooleanField("status", null=False, default=True)
    created_at = models.DateField("date", null=True)


    def __str__(self):
        return self.name
