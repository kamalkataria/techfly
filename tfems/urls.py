from django.conf.urls import url
from tfems import views
from . import views
urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'logintosys/$',views.logintosys,name='logintosys'),
    url(r'addemp/$', views.addemp, name='addemp'),
    url(r'delEmp/(?P<empname>.+)/(?P<uname>.+)/$', views.delEmp, name='delemp'),
    url(r'editemp/(?P<empname>.+)/(?P<uname>.+)/$', views.editEmp, name='editemp'),

]

