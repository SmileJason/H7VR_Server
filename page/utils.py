#coding: utf-8

from .models import Page
from common import LOG
import random
import string


def create_slug():
    ran_str = ''.join(random.sample(
        string.ascii_letters + string.digits, 8))
    LOG.info(ran_str)
    if check_slug(ran_str):
        return create_slug()
    else:
        return ran_str

def check_slug(slug):
    if slug:
        pages = Page.objects.filter(slug=slug)
        if pages.exists() and pages.count > 0:
            return True
        else:
            return False
    else:
        return True