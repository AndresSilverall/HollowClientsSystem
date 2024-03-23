from django.test import TestCase
from tasks.models import TasksManagement


# Clase para testear la gestion de tareas de los usuarios - Unit Testing
class TestTasksManagementModel(TestCase):
    def setUp(self) -> None:

        # Tarea de prueba: 1
        self.new_task = TasksManagement.objects.create(
            title = "Actualizar registro del nuevo cliente.",
            description = "Actualizar el estado actual del nuevo cliente",
            priority = "ALTA",
            is_finished = False,
            status = "En proceso",
            due_date = "2024-04-10",
            created_at = "2024-03-23"
        )

        self.new_task.save()

        # Tarea de prueba: 2
        self.new_task_two = TasksManagement.objects.create(
            title = "Acodar reunion con los stakeholders",
            description = "Llevar a cabo una reunion con el equipo y los stakeholders para debatir sobre los requerimientos del cliente ",
            priority = "ALTA",
            is_finished = False,
            status = "En proceso",
            due_date = "2024-05-13",
            created_at = "2024-03-23"
        )

        self.new_task_two.save()

        # Tarea de prueba: 2
        self.new_task_three = TasksManagement.objects.create(
            title = "Reporte de ventas de los ultimos 7 dias",
            description = "Generar el reporte de ventas de las ventas de los productos de hardware de comunicacion.",
            priority = "MEDIA",
            is_finished = False,
            status = "En proceso",
            due_date = "2024-03-30",
            created_at = "2024-03-23"
        )

        self.new_task_three.save()



    def test_number_of_tasks(self):
        # El numero total de tareas agregadas a la base de datos: 3
        self.show_all_tasks = TasksManagement.objects.all()
        self.assertEquals(self.show_all_tasks.count(), 3, msg="Verificar el numero de tareas agregadas a la base de datos.")


    def test_task_length(self):
        # La longitud maxima para el campo "title" es de 50.
        self.length_title = self.new_task.title
        self.length_title
        self.assertEquals(self.new_task, 37, msg="Comprobar que la longitud del titulo de la tarea es correcta." )
        

    def test_task_length_fail(self):
        pass
  

    """def test_get_task_by_id(self):
        self.assertEquals(self.new_task_three.pk,3)"""
        
        

    """def test_length_of_a_task(self):
        pass"""