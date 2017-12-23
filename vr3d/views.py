#coding: utf-8
from django.shortcuts import render
from vr3d.models import VR3D
from django.http import HttpResponse
import simplejson as json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def vr_show(request):
	title = request.POST.get('title')
	vr = VR3D.objects.get(title=title)
	result = { 'link' : vr.link }
	if vr:
		vr.view_count = vr.view_count + 1
		vr.save()
		result = { 'errcode' : '0', 'link' : vr.link }
	else:
		result = { 'errcode' : '1'}
	return HttpResponse(json.dumps(result), content_type='application/json')

