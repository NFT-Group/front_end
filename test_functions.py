import pytest
import requests

import firebase_admin
from firebase_admin import credentials, firestore, db

firebase_key = {
  "type": "service_account",
  "project_id": "allcollections-6e66c",
  "private_key_id": "903f6873f9f77f0c779a1f3de218f84d641c3e17",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDI0SIZAxQhL/D6\naFtiSvXB+h9fjeM5LydC003CFHlmPlIc8SEy0ialBvHjzzM/LDRwRUopI5LdO60G\n4xJ7iPrdTl5JoB85JHe++VXFuj4aUMPUIGO4xhLXWPfO8dr6We9WJ4ebGcO7HL9N\nlu0JhCFLERC21MNGidnnr/VM0La0PyuxhtDtdrKjjsyVzvmIhuSFR34gW+1F1O/a\noCR7iCH7YaSxxFODkLlllpJ6KrCkbYzFEH04j4r4aNV/ZSweYwZoM+PjgnfoYp1u\nOgXUi2N/Y8Ynx6CWNiW/51RwG+t5FqMKhOFHtaFVk0IKvg4FVWiL/QDqtiPY2Tc0\nJe5R05KNAgMBAAECggEAJHAKC1bLKsBrrcwMtNecIx/S3IA+2AvtyErWA566bmpl\ndNnt565JE82gS3E3v8EyHKL981wAlIL1ANhn7KFsv4YuRpa2w6QR1EWioheKmDTK\na62a2paaKZf7kwHAdYenDU9r5CE3KjbroVT+2qiub9P/X+VYL27o6oi7bj46wJaZ\nekCeYvOqQ8tlnzcorRYzG8UV6fe1kyz0PHgH6q8yR5/OUtAhxm9hdIC+VKNvJah+\npyvMd+9mN1uTtnxkmPxR9Sv3GJJ4wOLsn2Wgvuydq453dGRaN+u6DCnVipOTPUvt\n6MxiwXPur6FgnpY5QDiMNHMJeMCH+NKJq7plHPqg4QKBgQDk7Hk7LbUwF845OeTs\nSZUAqhj2Rh91Q70/fQ5aiS9HV39na8ZLNT7VjA5sT3uEm7SJ7A6CVQjXkT2EiOcp\nRk+4NKhktaesnZXpVnW2bTNJOd2K0wnvcagn6RccYjBDH+SrQoFL27Zv3+/GePFb\ncdf73cobSUme1iW6MIjEmvUr3QKBgQDgkZ7ilLWndN1ROQAnDXnr0nrzeD+6txEf\n8lq5BWLaxfBtaw2++CwcXPo3+9KqXnny71gUBIVJlmJv6HFk1499qPMNJ8WEd9qW\nvkfHSrnF5lMdAwvj1da5ergdLbnCfHRSzravP4bZSlKsCmGWrVPuUnD8QtGyPnZs\nouine8eucQKBgF8UqLWfomW7PXgfR6msVirUe1GuhlpaLDw2YMPRvsVO3ifCZ7XN\nA7AGX+c0jATj9vRiCxSu5OFD/d0ST5ChF3NWy6oomN/lA+LKelGuwWJkmlOSm8nL\n1x/cfDDZx1nZ4UwQb0tmkjudMyWoDfcBLcf6snrq0Z0bLMhMaEHganwxAoGAd/OQ\niLqiJSY5KS9nM3TxUNOGtRHgCJ3MWeIcL4P+/5iHCgsKtpzdAvFu/gRWzIXWYbsS\nsu6PO3VGczwXhaPWk2pxGO/Lgyx559cPhBYYEOssLez4puQL49r3CS7pcEcF401j\nK0ylfN9ENXz+D3vZvwzuKPCQDcNrgi+qUfu99yECgYEApEwuUUkvZnqRmUqJqlrI\nUO6SfjgluVZyqQku+44sWTj8YjgpX//wvEhJpNzSkqYMjDDYtCuhfHJoY+WgVvHt\nUCVrxZmXZ7b/tNVT+0SjMGFsZIKLfuyVyqrXeFSHtLMMxcepobF44kxzSGLvdn1i\ndL2GMhkNW5gSwstAuetsf+E=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-ofrcq@allcollections-6e66c.iam.gserviceaccount.com",
  "client_id": "111391958965295617135",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ofrcq%40allcollections-6e66c.iam.gserviceaccount.com"
}

def test_firebase():
  cred = credentials.Certificate(firebase_key)
  transactions_app = firebase_admin.initialize_app(cred, { 'databaseURL': "https://allcollections-6e66c-default-rtdb.europe-west1.firebasedatabase.app/" } )
  ref = db.reference('/')
  first_firebase_object = ref.order_by_child('timestamp').limit_to_first(1).get()
  print(first_firebase_object)
  assert(first_firebase_object == None)
  
def test_back_end():
  request_json = {"collection":"boredapekennel","tokenid":"55"}
  r = requests.post('https://nft-back-end-py.herokuapp.com/', data = request_json)
  print(r.text)
  assert(r.text != None)
  
