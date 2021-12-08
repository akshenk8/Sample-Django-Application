from django.urls import path
from . import views

app_name = "team"
urlpatterns = [
    # ex: /team/
    path('', views.TeamMemberListView.as_view(), name='index'),
    # /team/add
    path('add/', views.TeamMemberAddView.as_view(), name='add'),
    # ex: /team/5/
    path('<int:pk>/', views.TeamMemberUpdateView.as_view(), name='detail'),
    # ex: /team/5/delete
    path('<int:pk>/delete/', views.TeamMemberDeleteView.as_view(), name='delete'),
]
