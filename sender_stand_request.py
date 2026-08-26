import configuration
import requests
import data

def post_new_user(body):
    header = data.headers.copy()
    header.pop("Authorization",None)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=header)

def post_new_kit(body,authToken):
    header = data.headers.copy()
    header["Authorization"] = "Bearer " + authToken

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                  json=body,
                  headers=header)