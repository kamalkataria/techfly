from django.conf.urls import url
from tfems import views
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'logintosys/$',views.logintosys,name='logintosys'),

]

