# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('list/', views.org_list, name='org_list'),
# ]

from django.urls import path
from . import views

app_name = 'orgs'

urlpatterns = [
    path('list/', views.org_list, name='org_list'),
    path('teacher/list/', views.teacher_list, name='teacher_list'),  # 添加讲师列表路由
]