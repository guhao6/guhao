"""study_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.static import serve
from study_platform.settings import MEDIA_ROOT
from courses.views import index  # 首页视图

urlpatterns = [
    path('admin/', admin.site.urls),  # 恢复Django原生Admin路由（核心修改）
    path('', index, name='index'),  # 首页
    path('courses/', include('courses.urls')),  # 课程模块路由
    path('orgs/', include('organizations.urls')), # 机构模块路由
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),  # 媒体文件访问

]