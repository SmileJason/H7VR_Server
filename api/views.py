#coding: utf-8

import simplejson as json
from django.http import HttpResponse

def test(request):
    result = {'status':1, 'message': u'Test'}
    return HttpResponse(json.dumps(result), content_type='application/json')
