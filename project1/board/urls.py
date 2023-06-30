from django.conf.urls import include
from django.urls import path
from django.urls import re_path
#from django.conf.urls import url에서 url은 v4.0부터 제거됨

from . import views


#127.0.0.1:8000
#127.0.0.1:8000/board
#127.0.0.1:8000/board_write
#127.0.0.1:8000/board_insert
#127.0.0.1:8000/board_view
#127.0.0.1:8000/board_edit
#127.0.0.1:8000/board_update
#127.0.0.1:8000/board_delete

urlpatterns = [
    path('', views.home, name="home"),
    path('board', views.board, name="board"),
    path('board_write', views.board_write, name="board_write"),
    path('board_insert', views.board_insert, name="board_insert"),
    path('board_view', views.board_view, name="board_view"),
    path('board_edit', views.board_edit, name="board_edit"),
    path('board_update', views.board_update, name="board_update"),
    path('board_delete', views.board_delete, name="board_delete"),
]