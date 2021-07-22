from django.urls import path, include
from todos import views
from django.contrib import admin

app_name = "todos"
# urlpatterns = [
#     path('', views.index,name='index'),
#     path('<int:id>/',views.detail,name='detail'),
#     path('insert/',views.insert,name='insert'),
#     path('db_insert/',views.db_insert,name='db_insert'),
#     path('<int:id>/delete/',views.delete,name='delete'),
#     path('<int:id>/db_update/',views.db_update,name='db_update'),
#     path('<int:id>/update/',views.update,name='update'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.TodoDetail.as_view(),name='todo_detail'),
    path('insert/',views.Insert,name='insert'),
    path('db_insert/',views.db_insert,name='db_insert'),
    path('<int:id>/delete/',views.delete,name='delete'),
    path('<int:id>/db_update/',views.db_update,name='db_update'),
    path('<int:id>/update/',views.Update,name='update'),
]