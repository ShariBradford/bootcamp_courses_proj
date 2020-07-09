from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create', views.create_course),
    path('courses/destroy/<int:course_id>', views.destroy_course),
    path('courses/delete/<int:course_id>', views.delete_course),
    path('courses/<int:course_id>/comments', views.show_comments),
    path('courses/<int:course_id>/comments/add', views.add_comment),
]