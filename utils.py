import os
import sys
import requests
import json
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "join_main.settings")
django.setup()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

TOKEN = "136f930530291876ee2db04c892fc956d3b934b2"

# to generate a Guest Acc on Server
def create_guest_account():
    username = "Guest"
    token_key = TOKEN 

    print("Generate a Guest Acc")
    user, created = User.objects.get_or_create(username = username, defaults={"is_active": True})
    token, created = Token.objects.get_or_create(user = user)
    if token.key != token_key:
        token.delete() 
        token = Token.objects.create(user=user, key=token_key)
        print("set A Token for Guest")
    print("Guest is ready for work.")
    print(f"Guest Token: {token.key}" )


# to generate a Test Contact and Tasks on Server
def send_put_request():
    tasks, contacts = load_test_data()
    content = [tasks, contacts]
    url_main = "http://127.0.0.1:8000/api/"
    url_for_tasks = "tasks/"
    url_for_contacts = "contacts/"
    path = [url_for_tasks, url_for_contacts]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {TOKEN}'
    }
    for each in range(len(path)):
        url = f"{url_main}{path[each]}"
        payload = content[each]
        response = requests.put(url, json=payload, headers=headers)
        if response.status_code == 201 or response.status_code == 200:
            print(f"Daten {path[each]}Daten wurden erfolgreich aktualisiert!")
        else:
            print(f"Fehler: {response.status_code} - {response.text} - {url}")

def load_test_data():
    file = os.path.join(os.path.dirname(__file__), 'testdata.json')
    with open(file, "r", encoding='utf-8') as file:
        data = json.load(file)
    contacts = data.get("contacts")
    tasks = data.get("tasks")
    return tasks, contacts

if __name__ == "__main__":
   create_guest_account()
   send_put_request()