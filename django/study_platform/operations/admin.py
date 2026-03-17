from django.contrib import admin
from .models import UserFavorite, UserLearnCourse

# 用户收藏管理
@admin.register(UserFavorite)
class UserFavoriteAdmin(admin.ModelAdmin):
    list_display = ["user", "fav_id", "fav_type", "add_time"]
    search_fields = ["user__username"]
    list_filter = ["fav_type", "add_time"]
    readonly_fields = ["add_time"]

# 用户选课管理
@admin.register(UserLearnCourse)
class UserLearnCourseAdmin(admin.ModelAdmin):
    list_display = ["user", "course", "add_time"]
    search_fields = ["user__username", "course__name"]
    list_filter = ["add_time"]
    readonly_fields = ["add_time"]