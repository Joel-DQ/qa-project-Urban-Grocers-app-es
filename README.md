# Proyecto Urban Grocers

## Descripción del proyecto

Este proyecto contiene pruebas automatizadas para comprobar la creación de kits para un usuario en la API de Urban Grocers.

Las pruebas verifican el comportamiento del parámetro `name` al crear un kit, incluyendo diferentes cantidades de caracteres, caracteres especiales, espacios, números, ausencia del parámetro y tipos de datos diferentes.

## Documentación

La documentación de la API utilizada para desarrollar las pruebas se encuentra en la documentación proporcionada para el proyecto Urban Grocers mediante ApiDoc.

## Tecnologías y técnicas utilizadas

- Python
- PyCharm
- Pytest
- Requests
- Git y GitHub
- API REST
- ApiDoc

Las solicitudes HTTP se realizan utilizando la biblioteca `requests` y las pruebas automatizadas se ejecutan mediante `pytest`.

## Estructura del proyecto

- `configuration.py` — contiene las URL y rutas de los endpoints.
- `data.py` — contiene los datos utilizados para las solicitudes y las pruebas.
- `sender_stand_request.py` — contiene las funciones para enviar solicitudes a la API.
- `create_kit_name_kit_test.py` — contiene las pruebas automatizadas para la creación de kits.
- `README.md` — contiene la información y las instrucciones del proyecto.
- `.gitignore` — contiene los archivos y directorios que Git debe ignorar.

## Ejecución de las pruebas

### 1. Instalar las dependencias

Instalar Python y las bibliotecas necesarias:

```bash
pip install pytest
pip install requests