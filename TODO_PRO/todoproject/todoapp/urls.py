from django.urls import path
from todoapp import views
app_name='todoapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:t_id>/', views.delete, name='delete'),
    path('update/<int:t_id>/', views.update, name='update'),
    path('classlistview/',views.listview.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.detailview.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.updateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.deleteview.as_view(),name='deleteview'),
]