from django.db import models


# Create your models here.
class TasksManagement(models.Model):

    class Priority(models.TextChoices):
        NORMAL = "NORMAL", "N"
        MEDIANA = "MEDIANA", "M"
        ALTA = "ALTA", "A"


    title = models.CharField("task title", max_length=50, null=False)
    description = models.TextField("description", max_length=200)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    is_finished = models.BooleanField(default=False)
    status = models.CharField(max_length=15, null=True, blank=True)
    due_date = models.DateField(null=True)
    created_at = models.DateField("date", null=True, auto_now_add=True)


    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ["-created_at", "-title"]
        verbose_name_plural = "Tasks"
