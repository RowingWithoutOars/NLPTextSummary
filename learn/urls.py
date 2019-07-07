from django.conf.urls import url, include
import learn.views as views

urlpatterns = [
    url('testPost/', views.testPost, name='testPost')
]