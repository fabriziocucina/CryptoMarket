VENV = venv

# Python bin del entorno virtual
PYTHON = $(VENV)/Scripts/python

# ----------------------------
# Crear entorno virtual
# ----------------------------
venv:
	python -m venv $(VENV)

# ----------------------------
# Instalar dependencias
# ----------------------------
install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

# ----------------------------
# Congelar dependencias
# ----------------------------
freeze:
	$(PYTHON) -m pip freeze > requirements.txt

# ----------------------------
# Ejecutar la aplicación
# ----------------------------
run:
	$(PYTHON) -m src.main

# ----------------------------
# Inicializar la base de datos
# (crear tablas si no existen)
# ----------------------------
init-db:
	$(PYTHON) -c "from src.database.connection import init_db; init_db()"

# ----------------------------
# Limpiar cachés y basura
# ----------------------------
clean:
	rm -rf __pycache__
	rm -rf */__pycache__
	rm -rf .pytest_cache
	rm -rf *.pyc
	rm -rf */*.pyc

# -------------------
# Pruebas unitarias
# -------------------
test:
	$(PYTHON) -m pytest -vv
