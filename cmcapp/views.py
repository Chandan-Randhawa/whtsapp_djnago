from django.shortcuts import render , HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.


def index(request):
    pass


def sendwhtsappmessage(request):
    header = {'Authorization': 'Bearer EAAPolYdEp4YBAM520E4U5KWZB5X20FcZBGyClZAZCA9wy1YJYA7qAltVjBtU4rCxoO8DkuMj2LH0c5hxIRXJ5xhcdqvD0ZAjaM9eiBeeURF7rlFGePS9sHEA43S7Iu8Ng4L0ZBceNSz8t2UrhwWPNNIMOMc6rTQZAvHBqE2y3ImqTZCxGnD4E6jIBDZCUyAl1XsKBrFWvtYQ9TAZDZD'}
    payload_2 = { "messaging_product": "whatsapp", "to": "919779922228", "type": "template", "template": { "name": "hello_world", "language": { "code": "en_US" } } }
    pay_3 = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": "919779922228",
            "type": "interactive",
            "interactive":{
                            "type": "list",
                            "header": {
                                "type": "text",
                                "text": "your-header-content"
                            },
                            "body": {
                                "text": "your-text-message-content"
                            },
                            "footer": {
                                "text": "your-footer-content"
                            },
                            "action": {
                                "button": "cta-button-content",
                                "sections":[
                                {
                                    "title":"12",
                                    "rows": [
                                    {
                                        "id":"unique-row-identifier",
                                        "title": "python",
                                        "description": "",           
                                    },
                                    {
                                        "id":"unique-row-identifier-2",
                                        "title": "django ",
                                        "description": "",           
                                    }
                                    ]
                                },
                                {
                                    "title":"34",
                                    "rows": [
                                    {
                                        "id":"unique-row-identifier",
                                        "title": "software",
                                        "description": "",           
                                    }
                                    ]
                                },
                                ]
                            }
                            }
            }
    payload = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": "919779922228",
                "type": "template",
                "template": {
                    "name": "sample_issue_resolution",
                    "language": {
                    "code": "en_US"
                    },
                    "components": [
                    # {
                    #     "type": "header",
                    #     "parameters": [
                    #     {
                    #         "type": "image",
                    #         "image": {
                    #                 "link": "https://i.imgur.com/5NefzrH.png"

                    #         }
                    #     }
                    #     ]
                    # },
                    {
                        "type": "body",
                        "parameters": [
                        {
                            "type": "text",
                            "text": "Zoarwar Singh"
                        },
                        # {
                        #     "type": "text",
                        #     "text": "python"
                        # },
                        # {
                        #     "type": "text",
                        #     "text": "Postgresql"
                        # }
                        ]
                    },
                    {
                        "type": "button",
                        "sub_type": "quick_reply",
                        "index": "0",
                        "parameters": [
                        {
                            "type": "payload",
                            "payload": "PAYLOADdd"
                        }
                        ]
                    }
                    ]
                }
                }
    print('ssssss')
    response = requests.post('https://graph.facebook.com/v15.0/106405205659521/messages' , headers= header ,json=pay_3)
    print('ddddddd')
    ans = response.json()
    print(ans)
    return HttpResponse('ifimvmfii')

@csrf_exempt
def index(request):
    if request.method == "GET":
        verify_token = 'd039741e-7836-4913-9efb-1e95e80d2e9b'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == verify_token:
            return HttpResponse(challenge, status = 200)
        else:
            return HttpResponse('error', status =403)

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)

        return HttpResponse('success', status = 200)


