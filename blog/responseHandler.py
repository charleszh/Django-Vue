
from django.http import HttpResponse
import json

def response_success(message, data=None, data_list=[]):
    return HttpResponse(json.dumps({
        'code': 200,
        'message': message,
        'data': data,
        'dataList': data_list
    }))
