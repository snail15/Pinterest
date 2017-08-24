from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.index),
    url(r'^pins/$', views.pin_index, name='pin_index'),
    url(r'^pins/create/$', views.create_pin, name='create'),
    url(r'^pins/(?P<id>)/$', views.show_pin),
    url(r'^pins/(?P<id>)/edit/$', views.edit_pin),
    url(r'^pins/(?P<id>)/delete/$', views.delete_pin),
    url(r'^pins/user/$', views.user_show, name='user_show'),
    url(r'^pins/logout$', views.logout, name='logout'),
    url(r'^pins/user/user_pins$', views.show_user_pins, name='show_user_pins'),
    url(r'^boards/create/$', views.create_board, name='create_board'),
    url(r'^boards/$', views.board_index, name='board_index'),
    url(r'^pins/create_topic/$', views.create_topic, name="create_topic")
  
    # url(r'^boards/(?P<id>)/$', views.show_board),
    # url(r'^boards/(?P<id>)/edit/$', views.edit_board),
    # url(r'^boards/(?P<id>)/delete/$', views.delete_board)
]