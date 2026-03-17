# TuxCount - Aplicación de Finanzas Personales

TuxCount es una aplicación web para la gestión de finanzas personales y del hogar. Permite registrar ingresos, gastos, deudas, ahorros y visualizar la evolución económica mediante dashboards interactivos. El backend está desarrollado con **FastAPI**, **SQLAlchemy** y **MySQL**, y el frontend se construirá con **React** y **TypeScript**.

Este documento describe el estado actual del proyecto (backend) y los pasos para continuar su desarrollo.

---

## 📋 Estado actual del proyecto

Se ha completado la configuración inicial del backend y se han implementado los dos primeros modelos de datos: **Usuario** y **Cuenta**. La base de datos MySQL está operativa y las migraciones con Alembic funcionan correctamente.

### ✅ Hitos alcanzados

- [x] Entorno virtual de Python configurado.
- [x] Dependencias instaladas (FastAPI, SQLAlchemy, PyMySQL, Alembic, python-dotenv, passlib, python-jose).
- [x] Estructura de carpetas del backend creada.
- [x] Variables de entorno definidas en `.env`.
- [x] Archivo `main.py` con configuración de CORS y rutas de prueba.
- [x] Archivo `database.py` con conexión a MySQL y base declarativa.
- [x] Inicialización y configuración de Alembic para migraciones.
- [x] Modelo `Usuario` (tabla `usuarios`) creado.
- [x] Modelo `Cuenta` (tabla `cuentas`) creado.
- [x] Primera migración aplicada con éxito.

---

## 🛠️ Tecnologías utilizadas

- **Backend**: Python 3.13+, FastAPI, SQLAlchemy, PyMySQL, Alembic.
- **Base de datos**: MySQL (o MariaDB).
- **Autenticación**: JWT (a implementar).
- **Frontend** (futuro): React, TypeScript, Vite, TanStack Query, Recharts.

---

## 📁 Estructura del proyecto (backend)

```text 
backend/
├── app/
│ ├── init.py
│ ├── main.py # Punto de entrada de la API
│ ├── database.py # Configuración de BD y sesión
│ └── models/ # Modelos SQLAlchemy
│ ├── init.py # Exporta los modelos
│ ├── usuario.py
│ └── cuenta.py
├── alembic/ # Migraciones
│ ├── versions/
│ ├── env.py
│ └── script.py.mako
├── alembic.ini # Configuración de Alembic
├── .env # Variables de entorno (no versionado)
├── requirements.txt
└── venv/ # Entorno virtual
```

---

## ⚙️ Configuración para desarrollo

### 1. Clonar el repositorio

```bash
git clone <url-del-repo>
cd tuxcount/backend
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```text
DATABASE_URL=mysql+pymysql://usuario:contraseña@localhost:3306/tuxcount_db
SECRET_KEY=clave_secreta_para_jwt
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5. Crear la base de datos

```sql
CREATE DATABASE tuxcount_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 6. Ejecutar migraciones

```bash
alembic upgrade head
```

### 7. Iniciar el servidor

```bash
uvicorn app.main:app --reload
```

La API estará disponible en http://localhost:8000. La documentación interactiva en /docs.

#### 📦 Modelos actuales
Usuario (app/models/usuario.py)

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| **id** | Integer | Clave primaria |
| **nombre** | String | Nombre completo |
| **email** | String | Correo único, indexado |
| **password_hash** | String | Contraseña cifrada |
| **fecha_registro** | DateTime | Fecha de creación (por defecto ahora) |
| **activo** | Boolean | Indica si la cuenta está activa |

**Relaciones:** Un usuario puede tener muchas cuentas, categorías, transacciones, etc.

**Cuenta** (app/models/cuenta.py)


| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| **id** | Integer | Clave primaria |
| **usuario_id** | Integer | FK a usuarios.id (obligatorio) |
| **nombre** | String | Nombre descriptivo (ej. "Banco Santander") |
| **tipo** | Enum | efectivo, cuenta_corriente, ahorro, tarjeta_credito, inversion |
| **saldo_inicial** | Numeric | Saldo inicial de la cuenta |
| **moneda** | String | Código ISO (por defecto COP) |
| **fecha_apertura** | Date | Fecha de apertura |
| **notas** | Text | Comentarios adicionales (opcional) |
| **incluir_en_patrimonio** | Boolean | Si se incluye en el patrimonio |


**Relaciones:** Pertenece a un usuario; tiene transacciones; puede ser destino de transferencias; asociada a deudas y metas.

#### 📝 Próximos pasos

Continuar con la implementación de los modelos restantes (en el orden sugerido):

1. **Categoría** (`app/models/categoria.py`)
2. **Transacción** (`app/models/transaccion.py`)
3. **PlantillaFijo** (`app/models/plantilla_fijo.py`)
4. **Deuda** (`app/models/deuda.py`)
5. **PagoDeuda** (`app/models/pago_deuda.py`)
6. **MetaAhorro** (`app/models/meta_ahorro.py`)
7. **AporteAhorro** (`app/models/aporte_ahorro.py`)
8. **Presupuesto** (`app/models/presupuesto.py`)


Después de cada modelo, se generará la correspondiente migración con Alembic.


#### 🧪 Comandos útiles


| Acción | Comando |
| :--- | :--- |
| **Crear una migración automática** | `alembic revision --autogenerate -m "mensaje"` |
| **Aplicar todas las migraciones pendientes** | `alembic upgrade head` |
| **Revertir la última migración** | `alembic downgrade -1` |
| **Ver historial de migraciones** | `alembic history` |
| **Ver estado actual de la BD** | `alembic current` |
| **Iniciar servidor FastAPI** | `uvicorn app.main:app --reload` |
| **Acceder a MySQL** | `mysql -u usuario -p` |


#### 🤝 Contribuciones

Este proyecto es de carácter personal, pero si deseas colaborar o tienes sugerencias, eres bienvenido.

#### 📄 Licencia

MIT (o la que prefieras).

```text

Este es el contenido listo para copiar y pegar en tu archivo `README.md`.
```