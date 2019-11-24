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

    words = []
    for bound in response.text_annotations[1:]:
        poly_bounds = list(bound.bounding_poly.vertices)
        base = poly_bounds[0]
        top = poly_bounds[2]

        width = top.x - base.x
        height = top.y - base.y

        words.append((bound.description, base.x, base.y, width, height))

    return words


# word, x, y, width, height
def get_center(bound):
    x_mid = bound[1] + (bound[3] / 2)
    y_mid = bound[2] + (bound[4] / 2)

    return [x_mid, y_mid]
