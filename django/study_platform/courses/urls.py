from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('list/', views.course_list, name='course_list'),  # 课程列表
    path('detail/<int:course_id>/', views.course_detail, name='course_detail'),  # 课程详情
    path('video/<int:chapter_id>/', views.course_video, name='course_video'),  # 视频播放
]