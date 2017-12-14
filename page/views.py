# encoding: utf-8
import simplejson as json
import os

from PIL import Image, ImageFile
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from common.utils.images import uuid_image_path
from page.models import Page, PAGE_STATUS_ACTIVE, PAGE_TYPES

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        file = request.FILES.get('imgFile')
        ext = file.name.split('.').pop()
        max_size = 1048576  # 1MB

        ext_allowed = ['gif', 'jpg', 'jpeg', 'png']
        if ext not in ext_allowed:
            return HttpResponse(json.dumps({'error': 1, 'message': u'上传图片的格式不被允许：%s' % ext}), mimetype='application/json')

        if file.size > max_size:
            return HttpResponse(json.dumps({'error': 1, 'message': u'图片不能超过1MB'}), mimetype='application/json')

        filename = uuid_image_path(file.name, 'page')
        filepath = os.path.join(
            settings.BASE_DIR, settings.MEDIA_ROOT, filename)

        dirpath = os.path.dirname(filepath)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)

        destination = open(filepath, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()

        # to compress image
        tmp = Image.open(filepath)
        # This line avoids problems that can arise saving larger JPEG files
        # with PIL
        ImageFile.MAXBLOCK = tmp.size[0] * tmp.size[1]
        tmp.save(filepath, quality=95, optimize=True)
        # tmp.save(new_image.file.path, 'JPEG', dpi=[300, 300], quality=95)

        return HttpResponse(json.dumps({'error': 0, 'url': settings.MEDIA_URL + filename}))

@permission_required('page.change_page', raise_exception=True)
def preview_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    messages.success(request, u'你正在预览页面【%s】，其状态是【%s】' %
                     (page.title, page.get_status_display()))
    # hots = Page.objects.filter(type=page.type, status=PAGE_STATUS_ACTIVE)[:20]
    return render(request, 'page/detail.html', {'page': page})

def get_page(request, slug, ptype=None):
    page = get_object_or_404(Page, slug=slug, status=PAGE_STATUS_ACTIVE)
    return render(request, 'page/detail.html', {'page': page})
