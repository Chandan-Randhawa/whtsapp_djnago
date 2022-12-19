from django.shortcuts import render , HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def sendwhtsappmessage(request):
    # x = 'Bearer'
    # y = 'EAAPolYdEp4YBAH6tThgF91vgJ9FMCJGwEhyCOZBtyN6LyTWBILAxX15DYHo0DkyLEJolGh18eWmHPsZAB8q37tAZBLRsa4HmemtCbmRzZB8CkpeJMzi2osCPbQbdDOomBczz2uX28O4GIursMZB90pSGud7zZANLgLjjwuXZATkCyWvQGm6aWpco5YDD3YagrnUBxYDOZAdVno2hd8ZCdk0eQ'
    # header = {'Authorization': f'{x} {y}'}
    # payload_2 = { "messaging_product": "whatsapp", "to": "919779922228", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }
    # pay_3 = {
    #         "messaging_product": "whatsapp",
    #         "recipient_type": "individual",
    #         "to": "919779922228",
    #         "type": "interactive",
    #         "interactive":{
    #                         "type": "list",
    #                         "header": {
    #                             "type": "text",
    #                             "text": "your-header-content"
    #                         },
    #                         "body": {
    #                             "text": "your-text-message-content"
    #                         },
    #                         "footer": {
    #                             "text": "your-footer-content"
    #                         },
    #                         "action": {
    #                             "button": "cta-button-content",
    #                             "sections":[
    #                             {
    #                                 "title":"12",
    #                                 "rows": [
    #                                 {
    #                                     "id":"unique-row-identifier",
    #                                     "title": "python",
    #                                     "description": "",           
    #                                 },
    #                                 {
    #                                     "id":"unique-row-identifier-2",
    #                                     "title": "django ",
    #                                     "description": "",           
    #                                 }
    #                                 ]
    #                             },
    #                             {
    #                                 "title":"34",
    #                                 "rows": [
    #                                 {
    #                                     "id":"unique-row-identifier",
    #                                     "title": "software",
    #                                     "description": "",           
    #                                 }
    #                                 ]
    #                             },
    #                             ]
    #                         }
    #                         }
    #         }
    # payload = {
    #             "messaging_product": "whatsapp",
    #             "recipient_type": "individual",
    #             "to": "919779922228",
    #             "type": "template",
    #             "template": {
    #                 "name": "sample_issue_resolution",
    #                 "language": {
    #                 "code": "en_US"
    #                 },
    #                 "components": [
    #                 {
    #                     "type": "header",
    #                     "parameters": [
    #                     {
    #                         "type": "image",
    #                         "image": {
    #                                 "link": "https://i.imgur.com/5NefzrH.png"

    #                         }
    #                     }
    #                     ]
    #                 },
    #                 {
    #                     "type": "body",
    #                     "parameters": [
    #                     {
    #                         "type": "text",
    #                         "text": "Zoarwar Singh"
    #                     },
    #                     # {
    #                     #     "type": "text",
    #                     #     "text": "python"
    #                     # },
    #                     # {
    #                     #     "type": "text",
    #                     #     "text": "Postgresql"
    #                     # }
    #                     ]
    #                 },
    #                 {
    #                     "type": "button",
    #                     "sub_type": "quick_reply",
    #                     "index": "0",
    #                     "parameters": [
    #                     {
    #                         "type": "payload",
    #                         "payload": "PAYLOADdd"
    #                     }
    #                     ]
    #                 }
    #                 ]
    #             }
    #             }
    # print('ssssss')
    # response = requests.post('https://graph.facebook.com/v15.0/106405205659521/messages' , headers= header ,json=pay_3)
    # print('ddddddd')
    # ans = response.json()
    # print(ans)
    return HttpResponse('ifimvmfii')

@csrf_exempt
def indexx(request):
    if request.method == "GET":
        VERIFY_TOKEN = 'd039741e-7836-4913-9efb-1e95e80d2e9b'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status = 200)
        else:
            return HttpResponse('error', status =403)

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)

        return HttpResponse('success', status = 200)


