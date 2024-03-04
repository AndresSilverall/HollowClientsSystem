from django.db import models


# Create your models here.
class TasksManagement(models.Model):

    class Priority(models.TextChoices):
        NORMAL = "N", "NORMAL"
        MEDIANA = "M", "MEDIANA"
        ALTA = "A", "ALTA"


    title = models.CharField("task title", max_length=20, null=False)
    description = models.TextField("description", max_length=150)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    status = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateField("date", null=True, auto_now_add=True)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ["-created_at", "-title"]
        verbose_name_plural = "Tasks"
