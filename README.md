# Hollow Customers system

Aplicación web para el proyecto final de ADSO la cual consiste en administrar, gestionar y mejorar las relaciones entre una empresa y sus clientes, desarrollada con el framework Django de Python, y otras tecnologías como JavaScript, CSS, Jquery, sBootstrap y MySQL.

<img src="assets/logo.png" width="220" height="220" alt="logo.png">


## Tecnologías usadas

- Python versión 3.8.5
- JavaScript
- Framework Django versión 4.2.5
- Bootstrap versión 5.3
- CSS
- HTML5
- MySQL
- jQuery
- IDE (Visual studio code)
- GIT versión 2.37.2.windows.2


## Instalación y configuración

1. Clona este repositorio: ` git clone https://github.com/AndresSilverall/HollowClientsSystem.git`
2. Instale un administrador de entornos virtuales desde el gestor de paquetes de Python con el siguiente comando desde la terminal:  `pip install pipenv`
3. Una vez ya instalado navegue a la carpeta del proyecto: `cd HollowClientsSystems`
4. Ingrese el siguiente comando desde la terminal para activar el entorno viirtual e instalar todas las dependencias del proyecto que se encuentran alojadas en el archivo `Pipfile` del directorio raiz: `pipenv install`


## Configuración de la base de datos y correo electrónico 

Se utilizó el sistema de gestor de base de datos `MySQL Workbench` para el procesamiento y almacenamiento de los datos, paso a paso para la configuración:

1. Primero debe crear una base de datos de manera local desde `MySQL Workbench` de la siguiente forma:

```sql
-- Recomiendo crear una base de datos con el nombre del proyecto.
CREATE DATABASE HollowCustomersSystem;

```
2. Una vez creada la base de datos debe agregar las credenciales de acceso en el archivo `.env` del directorio raiz del proyecto:

```python

DB_NAME=HollowCustomersSystem # Nombre de la base de datos creada en la plataforma del cliente.
DB_HOST=localhost # El localhost donde de la base de datos (es decir la maquina en la que corre la db)
DB_USER=root # Los privilegios de usuarios
DB_PASSWORD= # La ontraseña de la base de datos del cliente
DB_PORT=3306 # El puerto en el que corre la base de datos

```

El siguiente codigo se encuentra en el archivo `settings.py` de la carpeta `config`, este codigo almacena las credenciales alojadas en el archivo `.env`.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'), # Lama a la variable DB_NAME alojada en .env
        'HOST': os.getenv('DB_HOST'), # Lama a la variable DB_HOST alojada en .env
        'USER': os.getenv('DB_USER'), # Lama a la variable DB_USER alojada en .env
        'PASSWORD': os.getenv('DB_PASSWORD'), # Lama a la variable DB_PASSWORD alojada en .env
        'PORT': os.getenv('DB_PORT'), # Lama a la variable DB_PORT alojada en .env
    }
}

```

3. Una vez ya configurada las credenciales que se encuentra almacenadas en `.env`, debe ejecutar los siguientes comandos de atajos dentro del entorno virtual para realizar las migraciones de la base de datos ya creada:

Primero ejecuta: `pipenv run make`
Luego: `pipenv run migrate`

Comando `pipenv run make`: Este comando se utiliza para crear archivos de migración que describen los cambios que se realizarán en la estructura de la base de datos. Django examina los cambios en los modelos y genera archivos de migración en función de esos cambios.

Comando `pipenv run migrate`: Después de crear los archivos de migración, debes aplicar esos cambios a la base de datos utilizando el comando `pipenv run migrate`, rste comando ejecuta las migraciones pendientes y actualiza la estructura de la base de datos según las especificaciones de los archivos de migración generados. 


## Configuración de las credenciales de Email

Para configurar las credenciales de Email se hace de la misma forma que las credenciales de la base de datos que se encuentran alojadas en el archivo `.env`

```python
# Credenciales de correo electronico

EMAIL="emailexample@gmail.com" # Ingrese su correo electronico 
PASSWORD="emailpassword" # Contraseña 

```

El siguiente codigo almacena las credenciales de email el cual se encuentra alojado en el archivo `settings.py`de la carpeta config.

```python

# Configuracion de correo electronico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL") # Variable que almacena el correo del usuario 
EMAIL_HOST_PASSWORD = os.getenv("PASSWORD") # Variable que almacena la contraseña

```


## Ejecución de la aplicación

Una vez ya realizadas las migraciones de la base de datos ejecute el siguiente comando para correr el servidor en el puerto 8000: 

```python
pipenv run server

```

luego abra su navegador web e ingrese la siguiente dirección: `127.0.0.1:8000` y podrá hacer uso del funcionamiento de la aplicación.


## Pruebas software (Unit testing)

La aplicación cuenta con diferentes módulos (apps), cada uno encargado de realizar una función en específico, para comprobar que cada módulo realiza una acción esperada fue necesario implementar pruebas unitarias, ya que dentro de cada módulo se encuentran bloques de código, el objetivo es comprobar que cada bloque de código funcione correctamente para luego comprobar que todo el código en su conjunto funciona como es debido.

# Ejemplo caso de prueba

| ID  | Nombre de la prueba                  | Tipo de prueba  | Descripción                                                                           | Entorno de prueba   | Fecha      | Autor          | Entrada esperada                                                                                                   | 233321312323 |
|-----|--------------------------------------|-----------------|---------------------------------------------------------------------------------------|---------------------|------------|----------------|--------------------------------------------------------------------------------------------------------------------|--------------|
| 001 | test_if_form_is_valid                | Prueba unitaria | Comprobar que todos los campos del formulario de registro son validos.                | Prueba automatizada | 15/03/2024 | Andres Silvera | {"username": "andressilvera12", "email": "andres12@gmail.com", "password1": "3144300Ua", "password2": "3144300Ua"} |              |
| 002 | test_if_form_is_not_valid            | Prueba unitaria | Comprobar que los datos ingresados en el formulario de registro son invalidos.        | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |
| 003 | test_send_data_form                  | Prueba unitaria | Comprobar que el codigo de estado recibido desde el servidor es 200.                  | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |
| 004 | test_send_data_form_error_404        | Prueba unitaria | Comprobar que los datos enviados son incorrectos y el servidor devuelve un error 404. | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |
| 005 | test_home_view_returns_200_ok        | Prueba unitaria | La vista "home" debe retornar un codigo de estado 200.                                | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |
| 006 | test_home_view_fail                  | Prueba unitaria | La vista "home" debe retornar un codigo de estado 400.                                | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |
| 007 | test_template_associated_to_url_pass | Prueba unitaria | Comprobar el template y la url asociada a la vista                                    | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |
| 008 | test_template_associated_to_url_fail | Prueba unitaria | Comprobar que la url no esta asociada al template "menu.html"                         | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |
| 009 | test_context_template_register       | Prueba unitaria | Comprobar el context dentro del template de registro.                                 | Prueba automatizada | 15/03/2024 | Andres Silvera |                                                                                                                    |              |

```python
pipenv run test

```