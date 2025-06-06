
# Proyecto Final - Data Engineering


¿Qué se hizo?

- Se creo un entorno virtual.
- Se ordenaron las carpetas en una estructura profesional
- Se creo una base de datos con el script load_data.sql
- En este script se carga la base de datos desde csv
- Se utilizo POO respetando los principios del mismo.
- Estos se pueden ver en la carpeta src/models

**Se utilizaron patrones de diseño:**

-Singleton para la conexion a la base de datos

-Factory para instanciar los modelos

-Builder para crear querys a la base de datos sobre sales

# Justificacion tecnica

- puede ver las justificacion tecnica en los archivos que se encuentran en la raiz

✅ Pruebas unitarias con pytest:
Se implementaron pruebas unitarias para verificar la integridad del codigo, se pueden ver en la carpeta test

# Estructura del proyecto

├── data/                 # Contiene los archivos CSV originales.
├── sql/                  # Scripts SQL para creación y carga de 
│   ├── load_data.sql
│   ├── ctes.sql
│   ├── objets.sql
│   ├── store_procedures.sql
│   ├── views.sql
│   
├── src/                  # Código fuente de Python.
│   ├── builders/         # Patrones de diseño 'Builder'.
│   ├── factories/         # Patrones de diseño 'factory'.
│   ├── models/           # Clases que representan las entidades 
│   └── database/         
├── .env                  # Variables de entorno 
├── .gitignore            # Archivos y carpetas ignorados 
├── main.py               # Script principal 
├── notebook.ipynb        # jupiter notebook
└── requirements.txt      # Dependencias de Python.

##  Configuración e Instalación

Para ejecutar este proyecto, sigue los siguientes pasos:

1.  **Clonar el repositorio**
2.  **Asegúrate de tener Python instalado.**
3.  **Crear un entorno virtual**:
    ```bash
    python -m venv venv
    # En Windows
    venv\Scripts\activate

    ```
4.  **Instalar las dependencias:**
    ```
    pip install -r requirements.txt
    ```
5.  **Crear el archivo de configuración `.env`:**

DB_HOST=

DB_USER=

DB_PASSWORD=

DB_NAME=

DB_PORT=


6.  **ejecutar:**

-puedes utilizar el jupiter notebook que se encuentra en la raiz del proyecto


