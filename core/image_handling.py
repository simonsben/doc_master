from google.cloud import vision
from google.oauth2 import service_account
from io import open


def get_input(base, scanned):
    return scanned - base


def perform_ocr(path, cred_file='credentials.json'):
    creds = service_account.Credentials.from_service_account_file(cred_file)
    client = vision.ImageAnnotatorClient(credentials=creds)

    with open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.document_text_detection(image=image)

    # words = []
    # for index, entry in enumerate(response.text_annotations[1:]):
    #     words.append((entry.description, ))
    return response.text_annotations[1:]