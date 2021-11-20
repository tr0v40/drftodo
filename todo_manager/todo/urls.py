from django.conf.urls import url
from todo import views


urlpatterns = [
    url(r'^', views.TodoList.as_view(), name='todo-list'),
]