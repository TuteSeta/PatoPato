# TP4: Integración Continua

## Introducción
Este proyecto es parte del TP4 de la asignatura "Ingeniería y Calidad de Software" y se centra en la implementación de integración continua utilizando GitHub Actions.

## Objetivo
El objetivo principal es garantizar que las diferentes funcionalidades del sistema sean probadas automáticamente mediante GitHub Actions cada vez que se realice un cambio en el repositorio.

## Estructura del Proyecto
### Archivos principales:
- `main.py`: Contiene las funciones principales del sistema relacionadas con especies, usuarios y simulaciones.
- `requirements.txt`: Lista las dependencias necesarias, como `pytest`.
- Archivos de test:
  - `test_du14.py`: Pruebas para búsqueda de especies por nombre.
  - `test_du27.py`: Pruebas para obtención de datos de comportamiento.
  - `test_du9.py`: Pruebas para obtener ficha completa de especies.
  - `test_du16.py`: Pruebas para autenticación de usuarios.
  - `test_du35.py`: Pruebas para comparación entre especies.
  - `test_du11.py`: Pruebas para filtrar especies por tipo de vuelo.
  - `test_du15.py`: Pruebas para filtrar especies por hábitat.
  - `test_du1.py`: Simulación de comportamientos de especies bajo ciertas condiciones.

## Instrucciones para ejecutar
1. **Clonar repositorio**
   ```bash
   git clone <URL_del_repositorio>
   cd <nombre_del_directorio>
   ```

2. **Instalar dependencias**
   Asegúrate de tener Python instalado. Luego ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar los tests manualmente**
   Para ejecutar los tests manualmente, utiliza:
   ```bash
   pytest
   ```

## Integración Continua con GitHub Actions
El proyecto utiliza GitHub Actions para automatizar la ejecución de los tests. Cada vez que se realiza un cambio en el repositorio, los tests definidos en los archivos de test se ejecutan automáticamente.

### Cómo funciona
1. Un archivo YAML en `.github/workflows/` define el proceso de testeo.
2. Cuando se realiza un `push` o `pull request`, se ejecuta el flujo de trabajo.
3. Los resultados de los tests se muestran directamente en la interfaz de GitHub.


## Información adicional
- Lenguaje: Python
- Framework de testing: Pytest

## TestOk OK
