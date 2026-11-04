## API de control e inventario de productos y compras

API REST para la gestión de productos, inventario y compras. Permite administrar productos, controlar existencias y registrar compras. Incorpora autenticación mediante tokens JWT, autorización basada en roles y validación de datos con Pydantic. Utiliza PostgreSQL como sistema de almacenamiento y SQLAlchemy como ORM.

## Tecnologias utilizadas:
Python: lenguaje de programación.
FastAPI: framework para la construcción de la API REST.
PostgreSQL: sistema de gestión de bases de datos.
SQLAlchemy: ORM para interactuar con la base de datos.
JWT (JSON Web Tokens): autenticación y gestión de tokens.
Pydantic: validación y estructuración de datos.

## Estructura del proyecto

API Productos/
│
├── rutas/
│   ├── compras.py
│   ├── productos.py
│   └── usuarios.py
│
├── servicios/
│   ├── compras.py
│   ├── productos.py
│   └── usuarios.py
│
├── .env.example
├── .gitignore
├── base_datos.py
├── configuracion.py
├── dependencias.py
├── esquemas.py
├── main.py
├── modelos.py
├── requirements.txt
├── seguridad.py
└── README.md
```

### Descripción de los módulos

- **rutas/**: contiene los endpoints de la API para gestionar compras, productos y usuarios.
- **servicios/**: contiene la lógica de negocio relacionada con compras, productos y usuarios.
- **base_datos.py**: configura la conexión con PostgreSQL y las sesiones de SQLAlchemy.
- **configuracion.py**: centraliza la lectura de las variables de entorno.
- **dependencias.py**: gestiona las dependencias de autenticación y autorización.
- **esquemas.py**: define los esquemas de validación de datos mediante Pydantic.
- **main.py**: crea la aplicación FastAPI e incorpora las rutas.
- **modelos.py**: define los modelos de datos mediante SQLAlchemy.
- **seguridad.py**: gestiona el cifrado de contraseñas y la generación y validación de tokens JWT.
- **requirements.txt**: contiene las dependencias del proyecto.
- **.env.example**: plantilla de las variables de entorno necesarias para ejecutar el proyecto.
- **.gitignore**: especifica los archivos y carpetas excluidos del control de versiones.
