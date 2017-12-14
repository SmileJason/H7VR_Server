#coding: utf-8
import simplejson as json

from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.template import RequestContext
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.db import transaction
from django.utils.timezone import now as django_now

from common import LOG
from page.models import Page
from comment.models import PageComment


@transaction.atomic
def comment_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        content = request.POST.getlist('content')
        try:
            comment = PageComment(user=request.user, content=content)
        except Exception, e:
            LOG.exception(e)
            messages.error(request, _(u'输入错误，请重新输入'))
        else:
            for c in comments:
                c.save()
            order.comment_time = django_now()
            order.save()
            messages.success(request, _(u'评论完成，已经添加到产品详细页面中。'))
            return redirect('/order/%s/' % order_id)

    item_ids = [oi.product_item_id for oi in order.orderitem_set.all()]
    product_ids = set()
    for item_id in item_ids:
        product_ids.add(ProductItem.objects.get(id=item_id).product_id)

    return render(request, 'comment/form.html', {'order': order, 'products':[Product.objects.get(id=pid) for pid in product_ids]})
