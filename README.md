# Hollow Customers system

Aplicación web para el proyecto final de ADSO la cual consiste en administrar, gestionar y mejorar las relaciones entre una empresa y sus clientes, construida con el framework Django de Python, y otras tecnologías como JavaScript y CSS, Bootstrap y MySQL.

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

1. Clona este repositorio: `https://github.com/AndresSilverall/HollowClientsSystem.git`
2. Instale un gestor de entornos virtuales desde el gestor de paquetes de Python con el siguiente comando desde la terminal:  `pip install pipenv`
3. Una vez ya instalado navegue a la carpeta del proyecto: `cd HollowClientsSystems`
4. Ingrese el siguiente comando desde la terminal para activar el entorno viirtual e instalar todas las dependencias del proyecto que se encuentran alojadas en el archivo `Pipfile` del directorio raiz: `pipenv install
`


## Configuración de la base de datos 

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


3. Luego configurar dichas credenciales en el archivo `settings.py` alojada en la carpeta `config` de la siguiente forma:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'HOST': os.getenv('DB_HOST'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'PORT': os.getenv('DB_PORT'),
    }
}

```

El codigo anterior lo encuentra en `settings.py` y a traves de `os.getenv` se accede a las credenciales almacenadas en la variable de entorno `.env`.


4. Una vez ya configurada las credenciales que se encuentra almacenadas en `.env`, debe ejecutar los siguientes comandos de atajos dentro del entorno virtual para realizar las migraciones de la base de datos ya creada:

Primero ejecuta: `pipenv run make`
Luego: `pipenv run migrate`

Comando `pipenv run make`: Este comando se utiliza para crear archivos de migración que describen los cambios que se realizarán en la estructura de la base de datos. Django examina los cambios en los modelos y genera archivos de migración en función de esos cambios.

Comando `pipenv run migrate`: Después de crear los archivos de migración, debes aplicar esos cambios a la base de datos utilizando el comando `pipenv run migrate`, rste comando ejecuta las migraciones pendientes y actualiza la estructura de la base de datos según las especificaciones de los archivos de migración generados. 


## Ejecución de la aplicación

Una vez ya realizadas las migraciones de la base de datos ejecute el siguiente comando para correr el servidor en el puerto 8000: 

```python
pipenv run server

```

luego abra su navegador web e ingrese la siguiente dirección: `127.0.0.1:8000` y podrá hacer uso del funcionamiento de la aplicación.
