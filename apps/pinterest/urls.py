from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.index),
    url(r'^pins/$', views.pin_index, name='pin_index'),
    url(r'^pins/create/$', views.create_pin, name='create'),
<<<<<<< HEAD
    url(r'^pins/(?P<id>)/$', views.show_pin),
    url(r'^pins/(?P<id>)/edit/$', views.edit_pin),
    url(r'^pins/(?P<id>)/delete/$', views.delete_pin),
    url(r'^pins/user/$', views.user_show, name='user_show'),
>>>>>>> dbad000d24464b24171b8d16b7823daeba76aebb
    # url(r'^boards/$', views.board_index),
    # url(r'^boards/create/$', views.create_board),
    # url(r'^boards/(?P<id>)/$', views.show_board),
    # url(r'^boards/(?P<id>)/edit/$', views.edit_board),
    # url(r'^boards/(?P<id>)/delete/$', views.delete_board)
]