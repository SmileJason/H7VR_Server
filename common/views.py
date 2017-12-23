#coding: utf-8
from django.shortcuts import render

# def index(request):
#     if request.is_mobile:
#         return render(request, 'home.html')

#     hots = Product.readonly.filter(status=PRODUCT_STATUS_ACTIVE).order_by('-sales_volume')[50:55]
#     sliders = Slider.objects.filter(status='1', type='31').order_by('order')
#     topbanners = TopBanner.objects.filter(status='1')
#     floors = IndexFloor.objects.filter(status='1').order_by('order')
#     floor_list = []
#     for floor in floors:
#         floor_list.append({
#             'name': floor.name,
#             'name_en': floor.name_en,
#             'color': floor.color,
#             'id': floor.id,
#             'tags': floor.collections.all()[:10],
#             'category': floor.category,
#             'tags2': floor.category.tag_set.all()[:10],
#             'big_images': floor.indexfloorimage_set.filter(type='1'),
#             'middle_image': floor.indexfloorimage_set.filter(type='2').first(),
#             'small_images': floor.indexfloorimage_set.filter(type='3'),
#             'headers': floor.indexfloorimage_set.filter(type='5'),
#             })
#     data = {'latests': latest_tags, 'hots':hots, 'panes': IndexTag.objects.all().order_by('order'),
#             'sliders': sliders,  'topbanners': topbanners, 'floors': floor_list}
#     return render(request, 'index.html', data)
