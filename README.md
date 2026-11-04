# API de control e inventario de productos y compras

API REST para la gestión de productos, inventario y compras. Permite administrar productos, controlar existencias y registrar compras. Incorpora autenticación mediante tokens JWT, autorización basada en roles y validación de datos con Pydantic. Utiliza PostgreSQL como sistema de almacenamiento y SQLAlchemy como ORM.

## Tecnologías utilizadas

| Tecnología | Versión | Descripción |
|---|---|---|
| Python | — | Lenguaje de programación. |
| FastAPI | 0.162.0 | Framework para desarrollar la API REST. |
| PostgreSQL | — | Sistema de gestión de bases de datos. |
| SQLAlchemy | 2.1.6 | ORM para interactuar con PostgreSQL. |
| Psycopg | 3.3.6 | Controlador de conexión con PostgreSQL. |
| Pydantic | 2.14.2 | Validación y estructuración de datos. |
| PyJWT | 2.15.1 | Gestión de tokens JWT. |
| pwdlib | 0.3.1 | Protección y verificación de contraseñas. |
| python-dotenv | 1.2.4 | Gestión de variables de entorno. |
| Uvicorn | 0.54.0 | Servidor ASGI para ejecutar la aplicación. |
| python-multipart | 0.0.33 | Procesamiento de formularios de autenticación. |

Las versiones de las dependencias están especificadas en `requirements.txt`.

## Estructura del proyecto

```text
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
- **seguridad.py**: gestiona el hash de contraseñas y la generación de tokens JWT.
- **requirements.txt**: contiene las dependencias del proyecto.
- **.env.example**: plantilla de las variables de entorno necesarias para ejecutar el proyecto.
- **.gitignore**: especifica los archivos y carpetas excluidos del control de versiones.

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/ocampodiego123-max/API-inventario-productos.git
cd API-inventario-productos
```

### 2. Crear y activar el entorno virtual

En Windows, utilizando PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto, tomando como referencia `.env.example`.

Completar las variables requeridas:

```env
DATABASE_URL=
SECRET_KEY=
```

### 5. Ejecutar la aplicación

```bash
python -m uvicorn main:app --reload
```

### 6. Acceder a la documentación interactiva

Con el servidor en ejecución, abrir:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Endpoints de la API

La API dispone de endpoints para la gestión de usuarios, productos, inventario y compras.

### Usuarios

| Método | Endpoint | Descripción | Acceso |
|---|---|---|---|
| POST | `/registro` | Registra un usuario nuevo. | Público |
| POST | `/login` | Autentica al usuario y genera un token JWT. | Público |

### Productos

| Método | Endpoint | Descripción | Acceso |
|---|---|---|---|
| GET | `/productos/` | Lista todos los productos. | Autenticado |
| GET | `/productos/{producto_id}` | Consulta un producto por su ID. | Autenticado |
| POST | `/productos/` | Registra un producto. | Administrador |
| PUT | `/productos/{producto_id}` | Actualiza los datos de un producto. | Administrador |
| PATCH | `/productos/{producto_id}` | Actualiza el stock de un producto. | Administrador |
| DELETE | `/productos/{producto_id}` | Elimina un producto. | Administrador |

### Compras

| Método | Endpoint | Descripción | Acceso |
|---|---|---|---|
| POST | `/compras/{producto_id}` | Registra una compra y descuenta existencias. | Administrador |
| GET | `/compras/{producto_id}` | Consulta las compras asociadas a un producto. | Autenticado |

### Códigos de respuesta HTTP

- **201 Created:** registro exitoso.
- **204 No Content:** eliminación exitosa.
- **401 Unauthorized:** credenciales incorrectas.
- **404 Not Found:** recurso no encontrado.
- **409 Conflict:** usuario duplicado o stock insuficiente.
- **500 Internal Server Error:** error interno durante algunas operaciones.

Los endpoints protegidos requieren autenticación mediante un token JWT de tipo Bearer. Las operaciones administrativas requieren además el rol de administrador.

## Funcionalidades principales

### Gestión de usuarios

- Registro de nuevos usuarios.
- Autenticación mediante usuario y contraseña.
- Generación de tokens JWT para acceder a los endpoints protegidos.
- Control de acceso basado en roles.

### Gestión de productos e inventario

- Registro, consulta, actualización y eliminación de productos.
- Actualización de existencias.
- Control de acceso para operaciones administrativas.

### Gestión de compras

- Registro de compras asociadas a productos.
- Validación de existencias antes de registrar una compra.
- Descuento automático de las unidades compradas del inventario.
- Cálculo automático del valor total de la compra.
- Consulta del historial de compras por producto.
- Manejo de transacciones mediante confirmación (`commit`) y reversión (`rollback`).

### Reglas de negocio

- No se permite registrar una compra cuando el stock disponible es inferior a la cantidad solicitada.
- El valor total de una compra se calcula multiplicando la cantidad por el precio del producto.
- El inventario se actualiza al confirmar el registro de la compra.
- Las operaciones de modificación de productos y registro de compras requieren el rol de administrador.

## Modelo de datos

La aplicación utiliza PostgreSQL como sistema de almacenamiento y SQLAlchemy como ORM. La base de datos está organizada en tres entidades principales:

### Productos

Almacena la información de los productos:

- `id`: identificador único.
- `nombre`: nombre del producto.
- `stock`: cantidad disponible.
- `precio`: precio del producto.

Restricciones:
- El stock no puede ser negativo.
- El precio debe ser mayor que cero.

### Compras

Registra las compras realizadas:

- `id`: identificador único.
- `producto_id`: referencia al producto asociado.
- `cantidad`: unidades compradas.
- `total`: valor total de la compra.

Cada compra está asociada a un producto mediante una clave foránea.

### Usuarios

Almacena la información de autenticación y autorización:

- `id`: identificador único.
- `usuario`: nombre de usuario único.
- `password_hash`: contraseña almacenada mediante un hash seguro.
- `rol`: rol asignado al usuario, con valor predeterminado `usuario`.

### Relaciones

- Un producto puede tener múltiples compras.
- Cada compra pertenece a un único producto.
- Los usuarios se gestionan de forma independiente de las tablas de productos y compras en el modelo actual.

## Seguridad y autenticación

La API implementa mecanismos de autenticación y protección de credenciales:

### Protección de contraseñas

- Utiliza `pwdlib` para generar hashes seguros de las contraseñas.
- Emplea `PasswordHash.recommended()` para seleccionar una configuración de hash recomendada.
- Verifica las contraseñas durante el proceso de autenticación sin almacenar contraseñas en texto plano.

### Autenticación mediante JWT

- Utiliza JSON Web Tokens (JWT) para autenticar las solicitudes.
- Emplea el algoritmo de firma HS256.
- Incluye el identificador del usuario en el campo `sub`.
- Establece una expiración de 30 minutos para los tokens.
- Obtiene la clave secreta desde las variables de entorno.

### Control de acceso

- Los endpoints protegidos requieren un token Bearer válido.
- Las operaciones administrativas requieren el rol de administrador.
