# Formulario Coordinación

Este proyecto pretende resolver y automatizar procesos en la coordinación de industriales.

## Requisitos

- Python 3.x
- PostgreSQL

## Configuración del Entorno

1. **Clonar el Repositorio:**

   ```bash
   git clone https://github.com/BrialexMaga/coordinacion.git
   cd coordinacion
2. [RECOMENDADO] Configurar un entorno virtual

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows, use "venv\Scripts\activate"

    -(Si ya ha creado el entorno virtual anteriormente, solo activelo con la segunda linea)
3. Instalar Dependencias

    ```bash
    pip install -r requirements.txt
## Configurar Base de Datos
1. Acceder a PostgreSQL desde SQL Shell

    Despues de instalar PostgreSQL, entramos a SQL Shell.
    Damos intro hasta llegar a la contraseña, que es la puesta durante la instalación.

    ```bash
    Server [localhost]:
    Database [postgres]:
    Port [5432]:
    Username [postgres]:
    Contraseña para usuario postgres: my_contraseña
2. Crear la Base de Datos

    ```bash
    CREATE DATABASE coordinacion;
3. Crear un usuario para la app

    ```bash
    CREATE USER django WITH PASSWORD 'django';
4. Dar privilegios al usuario creado

    ```bash
    GRANT ALL PRIVILEGES ON DATABASE coordinacion TO django;
5. En caso de no tener los privilegios necesarios para Django, usar:

    ```bash
    ALTER USER django SUPERUSER;

## Iniciar el servidor de Desarrollo
1. En la terminal, accede a la raiz del proyecto:

    ```bash
    cd coordinacion
2. En caso de usar el ambiente virtual, hay que activarlo:

    ```bash
    source venv/bin/activate  # En Windows, use "venv\Scripts\activate"
3. Ejecuta la siguiente linea:

    ```bash
    python manage.py runserver
4. En tu navegador, abre localhost:8000