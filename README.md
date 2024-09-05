# API de Procesos ETL 🛠️✨

[![FastAPI](https://img.shields.io/badge/FastAPI-0.88.0+-00a393?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://fastapi.tiangolo.com)
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://pandas.pydata.org/docs/)
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=fastapi&logoColor=white&labelColor=101010)](https://numpy.org)
![Docker](https://img.shields.io/badge/Docker-20.10.8-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-336791?style=for-the-badge&logo=postgresql&logoColor=white)

## Descripción

¡Bienvenido a la API de Procesos ETL, donde FastAPI acelera la manipulación de datos, Pandas, NumPy y Polars son las estrellas detrás del show! 🚀 Esta API está diseñada para manejar grandes volúmenes de datos y transformarlos a tu medida con eficiencia y estilo. 🛠️📊

## Síguenos a Través de Estos Pasos

1. **Preparativos:**
   Asegúrate de tener Python y Docker instalados en tu sistema.
2. **Configuración de la Base de Datos:**
   Configura las variables de entorno en el archivo `.env.template` y cambia el nombre por `.env` para la conexión a PostgreSQL.
3. **Instalación de Dependencias:**
   Ejecuta `pip install -r requirements.txt` para instalar las dependencias necesarias (incluyendo FastAPI, Pandas, NumPy y Polars).
4. **Ejecutar en Docker:**
   Inicia los contenedores de Docker usando `docker-compose up -d`.
5. Levanta el proyecto utilizando `uvicorn main:app --reload`.

## **¡SEED Mágico! 🌱**

¡Inicia tu aventura de procesamiento de datos cargando archivos y ejecutando transformaciones mágicas!

### 🗃️ Subir El Archivo Excel de Direcciones

- **Método:** `POST`
- **Ruta:** `/api/direcciones`
- **Descripción:** Sube archivos 1 en formato Excel y prepárate para llenar la base de datos de información.
- **Observación:**: A este archivo lo vas a poder encontrar en el directorio
  `📂 process/`

### Obtener Datos Procesados 📈

- **Método:** `GET`
- **Ruta:** /api/direcciones
- **Descripción:** Consulta los datos de direcciones en este proceso ETL.

## 🔐 Acceso Mágico a la API

Descubre encantadores endpoints para interactuar con nuestros gatitos:

## Acceder al Portal de Login 🔑

- **URL:** localhost:8000/api/auth/login
- **Descripción:** Protege tus datos mágicos accediendo a través del portal seguro de autenticación.

## Registro de Nuevos Usuarios ✍️

- **URL:** localhost:8000/api/users
- **Descripción:** Regístrate para comenzar a realizar procesos ETL mágicos. ¡El conocimiento del procesamiento de datos está a tu alcance!

### 🔮 Procesar Datos - Transformaciones con Pandas

- **Método:** `POST`
- **Ruta:** `/api/process/pandas`
- **Descripción:** Filtra, agrupa y transforma datos como un hechicero usando el poder de Pandas. Aplica operaciones mágicas como media, mediana, y más.

### ⚡ Procesar Datos con Polars

- **Método:** `POST`
- **Ruta:** `/api/process/polars`
- **Descripción:** ¡Aprovecha la velocidad extrema de Polars para trabajar con grandes volúmenes de datos sin perder un segundo!

### 🔢 Operaciones Matemáticas con NumPy

- **Método:** `POST`
- **Ruta:** `/api/process/numpy`
- **Descripción:** Aplica magia matemática avanzada a tus datos utilizando las poderosas herramientas de NumPy. ¡Perfecto para cálculos complejos!

---

### 📦 Descarga los Datos Transformados

- **Método:** `GET`
- **Ruta:** `/api/download/`
- **Descripción:** Descarga los datos transformados en formato TXT o Excel. ¡Listo para ser compartidos! 🚀

### Descubre nuestros procesos ETL🌟

- **Método:** `GET`
- **Ruta:** `https://colab.research.google.com/drive/1RluuKh9Pv81Wkx1uqQ_M7TRf658tlTFh?hl=es#scrollTo=nlo87x4HG4MU`
- **Descripción:** ¡Descubre los procesos iniciales que llevo a crear la API!

## Ver Imagenes en el Navegador

- **URL:** `http://localhost:8000/api/files/data/{id}`
- **Ejemplo:** `localhost:8000/api/files/data/12345.json`
- **Descripción:** Abre tus datos directamente en el navegador para ver cómo se han transformado con cada hechizo.

---

## 📊 Explora el Modelo ER

Para entender cómo fluye la magia entre las entidades, puedes visualizar el Modelo ER de la base de datos en la carpeta:

`📂 er/db/`

Este diagrama te dará una visión clara de cómo las tablas están conectadas para realizar las transformaciones ETL de manera eficiente. ¡Es la base mágica de todo el proyecto!

## 📚 Documentación API Interactiva

Descubre la magia de cada endpoint y prueba la API con nuestra [documentación en vivo]('http://localhost:8000/docs'). ¡Realiza pruebas, ajusta transformaciones y experimenta con el poder de FastAPI en tiempo real! 🌟

---

![Michi Navideño](https://www.unite.ai/wp-content/uploads/2022/11/ETL-1000x600.png)

¡Que tu API de procesos ETL sea tan mágica como eficiente! ✨🚀
