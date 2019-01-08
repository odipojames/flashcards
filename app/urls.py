from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url(r'^card/(\d+)', views.card, name='card'),
    url(r'^new/card$', views.new_card, name='new-card'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)