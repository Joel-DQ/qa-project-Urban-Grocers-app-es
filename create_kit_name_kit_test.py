import sender_stand_request
import data

def get_token_user():
    return sender_stand_request.post_new_user(data.user_body).json()["authToken"]

def get_kit_name(name):
    current_kit=data.kit_body.copy()
    current_kit["name"]=name
    return current_kit

def positive_assert(name):
    kit_body=get_kit_name(name)

    kit_response = sender_stand_request.post_new_kit(kit_body, get_token_user())

    assert kit_response.status_code == 201

def negative_assert(name):
    kit_body=get_kit_name(name)

    kit_response = sender_stand_request.post_new_kit(kit_body, get_token_user())

    assert kit_response.status_code == 400
    #assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

# 1.El número permitido de caracteres (1): kit_body = { "name": "a"}
# def test_kit_body_name_1_letter():
#     positive_assert("a")

# 2.El número permitido de caracteres (511):
#   kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}
#   Ocupar data.kit_body_name_511 como valor Name
# def test_kit_body_name_511_letter():
#     positive_assert(data.kit_body_name_511["name"])

# 3.El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }
# def test_kit_body_name_empty():
#     negative_assert("")