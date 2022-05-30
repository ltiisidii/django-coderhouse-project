# Pre Entrega

## Equipo: 

jonatanw-jhersvinq-jhanr

### Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/ltiisidii/django-coderhouse-project.git

cd django-coderhouse-project

```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

- Instalar Django
```bash
pip install Django
```

- Ejecutar proyecto
```bash
python manage.py runserver
```

- Usuario administrador:
usuario: admin
password: test123

### Funcionalidades: 

- Inicio: Cuenta con un buscador para productos y clientes, para productos la busqueda se realiza por Nombre, precio o una busqueda general de ambas; para clientes la busqueda se realiza por Nombre, Apellido, Email o una busqueda general de ambas.

- Solapa Productos: Contiene una lista de productos con un CRUD que permite: alta, detalle, modificacion y eliminacion de productos, para el alta de un nuevo producto es necesario clickear en el boton "Crear Nuevo Producto" donde nos solicitara un nombre de producto y un precio para darlo de alta

- Solapa Clients: Contiene una lista de clientes con un CRUD que permite: alta, detalle, modificacion y eliminacion de clientes, para el alta de un nuevo cliente es necesario clickear en el boton "Crear Nuevo Producto" donde nos solicitara un nombre de cliente, un apellido y un correo de contacto para darlo de alta

- Solapa Consultas: Contiene un formulario para guardar consultas realizadas para poder verlas desde el panel de administrador, este formulario solicita: Nombre, Pregunta, Telefono, Email.

### Para facilitar la prueba del sitio se proporciona el archivo db.sqlite3 ya cargado

En caso de querer utilizar una base de datos de cero los pasos:

* Eliminar la carpeta migrations dentro de la carpeta app_coder

* Eliminar el archivo db.sqlite3 de la carpeta principal del proyecto

* Ejecutar lo siguiente:

Crear base de datos con los Modelos (hacer migraciones y migrar)

```bash

python manage.py makemigrations app_coder

python manage.py migrate

```

Crear super-usuario
```bash

python manage.py createsuperuser

```

```bash

Ejecutar proyecto

python manage.py runserver

```