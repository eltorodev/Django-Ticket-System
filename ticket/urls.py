from django.urls import path
from ticket import views

app_name = 'ticket'
urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/show/<int:id>/', views.show, name='show_ticket'),
    path('ticket/create/', views.create, name='create_ticket'),

    path('panel/', views.panel_index, name='panel_index')
]
