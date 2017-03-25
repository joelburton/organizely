from django.conf.urls import url

from todos import views

urlpatterns = [
    url('^$', views.TaskListListView.as_view(), name='tasklist-list'),
    url('^(?P<pk>\d+)/$', views.TaskListDetailView.as_view(), name='tasklist-detail'),
    url('^(?P<pk>\d+)/add/$', views.TaskCreateView.as_view(), name='task-create'),
    url('^tasks/$', views.TaskListView.as_view(), name='task-list'),
    url('^tasks/(?P<pk>\d+)/$', views.TaskDetailView.as_view(), name='task-detail'),
    url('^tasks/(?P<pk>\d+)/edit/$', views.TaskUpdateView.as_view(), name='task-update'),
]