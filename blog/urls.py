from django.urls import path
from . import views
from .views import PostCreatView, PostUpdateView, PostDeleteView


app_name = 'blog'


urlpatterns =[
    
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('new_post/', PostCreatView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    
]