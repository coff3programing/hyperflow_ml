# Logica de Negocio

### Herramientas

1. **DB**

- PostgreSQL

2. **Backend**

- FastAPI **(Clientes)**
- Django REST Framework **(Admin)**
- Librerías de Python

3. **Ciencia de Datos**

- Polars
- Pandas
- Numpy

### ¿Cuales son las tablas del sistema?

- direcciones
- espectroradiometros (Firmas)
- niveles - subniveles
- errores
- anomalos
- equipamiento
- agronomicos

### Roles

- Clientes
- Admin

### Gestionan

1. Clientes

- espectroradiometros (Firmas)
- niveles - subniveles
- agronomicos

2. Admin

- direcciones
- equipamiento
- errores
- anomalos

### Tablas Clientes

**niveles - subniveles**

- id **(Int serial pk)**
- id_equipamento **(Int serial pk)**
- files **(Varchar)**
- Planta **(Varchar)**
- Hoja **(Varchar)**
- Zona **(Varchar)**
- Toma **(Varchar)**
- Des **(Varchar)**

**espectroradiometros**

- id **(int serial pk)**
- id_niveles **(int serial pk)**
- files **(Varchar)**
- fecha_inicial **(Varchar)**
- fecha_final **(Varchar)**
- hora_inicial **(Varchar)**
- hora_final **(Varchar)**
- temperatura_inicial **(Varchar)**
- temperatura_final **(Varchar)**

- x **(INT)** (Constante)
- y **(INT)** (Variables)

_*agronomicos*_

- agronomico_id **(INT SERIAL PK)**
- niveles_codigo_id **(INT SERIAL PK)**👈👈👈👈👈👈
- agronomico_file **(VARCHAR(125) Remplazar nombre 👆)**

### Tablas Admin

**direcciones** **(EC)**

- id **(int serial pk)**
- archivo **(File)**
- Provincia **(Varchar)**
- Canton **(Varchar)**
- Parroquia **(Varchar)**

**Teams** **(ED)**

- id **(INT SERIAL PK)**
- nombre_proyecto **(VARCHAR(65))**
- descripcion
- direcciones **(Int serial pk)**

**variables**

- id **(INT SERIAL PK)**
- nombre **(VARCHAR(75))**

**_equipamientos_**

- id **(INT SERIAL PK)**
- id_teams **(INT FK)**
- nombre_equipo **(VARCHAR(75))**
- rango_espectral_inicial **(INT)**
- rango_espectral_final **(INT)**
- numero_serie **(TEXT)**
- ancho_banda **(FLOAT)**
- fecha_calibracion **(DATE)**
- variable_id **(INT PK)**

**_errores_** **(ED/EC)**

- error_id **(INT SERIAL PK)**
- error_nombre **(VARCHAR(65))**

**_anomalos_** **(ED)**

- id **(INT SERIAL PK)**
- numero_medicion_atipica **(INT)**
- imagen_anomala **(File Opcional)**
- error_id **(INT SERIAL FK)** (Anomalías)
- error_descripcion **(VARCHAR(255) Opcional)**

## Relaciones

#### **Admin**

**_Equipamientos es la tabla más importante_**

- 1 **Direcciones** pertenecen a 1 o N **Teams**
- 1 **Equipamientos** tiene 1 o N **Teams**
- 1 **Variable** pertenece a 1 **Equipamientos**
- 1 **Errores** pertenece a 1 **Anomalos**

#### **Cliente**

- 1 **Equipamientos** tiene 1 o N **Niveles**
- 1 **Niveles** tiene 1 o N **espectroradiometros**
- 1 **Equipamientos** tiene 1 o N **agronomicos**
