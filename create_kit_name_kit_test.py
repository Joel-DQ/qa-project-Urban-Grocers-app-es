import sender_stand_request
import data

token = None

def get_token_user():
    global token

    if not token:
        token = sender_stand_request.post_new_user(data.user_body).json()["authToken"]
    return token

def get_kit_name(name):
    current_kit=data.kit_body.copy()
    current_kit["name"]=name
    return current_kit

def positive_assert(name):
    kit_body=get_kit_name(name)

    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_token_user())

    assert kit_response.status_code == 201

def negative_assert(name):
    kit_body=get_kit_name(name)

    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_token_user())

    assert kit_response.status_code == 400

def negative_assert_no_body(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, get_token_user())

    assert kit_response.status_code == 400
    assert kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

# 1.El número permitido de caracteres (1): kit_body = { "name": "a"}
#Resultado: PASSED
def test_kit_body_name_1_letter():
    positive_assert("a")

# 2.El número permitido de caracteres (511):
#   kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
#   Ocupar data.kit_body_name_511 como valor Name
#Resultado: PASSED
def test_kit_body_name_511_letter():
    positive_assert(data.kit_body_name_511["name"])

# 3.El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
#Resultado:     Expected :400
#(FAILED)       Actual   :201
def test_kit_body_name_empty():
    negative_assert("")

# 4.El número de caracteres es mayor que la cantidad permitida (512):
#   kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }
#   Ocupar data.kit_body_name_512 como valor Name
#Resultado:     Expected :400
#(FAILED)       Actual   :201
def test_kit_body_name_512_letter():
    negative_assert(data.kit_body_name_512["name"])

# 5.Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }
#Resultado: PASSED
def test_kit_body_name_symbol():
    positive_assert('""№%@","')

# 6.Se permiten espacios: kit_body = { "name": " A Aaa " }
#Resultado: PASSED
def test_kit_body_name_space():
    positive_assert(" A Aaa ")

# 7.Se permiten números: kit_body = { "name": "123" }
#Resultado: PASSED
def test_kit_body_name_number():
    positive_assert("123")

# 8.El parámetro no se pasa en la solicitud: kit_body = { }
#Resultado:     Expected :400
#(FAILED)       Actual   :500
def test_no_body_kit():
    negative_assert_no_body({})

# 9.Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }
#Resultado:     Expected :400
#(FAILED)       Actual   :201
def test_kit_body_name_other_type():
    negative_assert(123)