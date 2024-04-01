from django.db import models
from contacts.models import CustomersManagement


# Modelos para la gestion de tickets
class Tickets(models.Model):

    class Priority(models.TextChoices):
        NORMAL = "NORMAL", "N"
        MEDIANA = "MEDIANA", "M"
        ALTA = "ALTA", "A"

    subject = models.CharField("Asunto", max_length=30, null=False, blank=False)
    customer = models.ForeignKey(CustomersManagement, on_delete=models.CASCADE)
    asigned_to = models.CharField("Asignacion",max_length=30, null=False, blank=False)
    agent = models.CharField("Agente", max_length=20, null=False,blank=False)
    description = models.TextField("Descripcion", max_length=600)
    priority = models.CharField("Prioridad", choices=Priority.choices ,max_length=10, null=False)
    ticket_type = models.CharField("Tipo", max_length=17, null=True, blank=True)
    chanel = models.CharField("Canal", max_length=15, null=True)
    created_at = models.DateField("Fecha de creacion", auto_now_add=True)


    def __str__(self):
        return self.subject
    
    class Meta:
        ordering = ["-subject"]
        verbose_name_plural = "Tickets"

