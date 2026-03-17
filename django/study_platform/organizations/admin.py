from django.contrib import admin
from .models import CourseOrg, Teacher

# 课程机构管理
@admin.register(CourseOrg)
class CourseOrgAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "address", "click_nums", "fav_nums", "add_time"]
    search_fields = ["name", "address"]
    list_filter = ["category", "click_nums", "add_time"]
    readonly_fields = ["add_time"]
    fieldsets = (
        ("机构信息", {"fields": ("name", "desc", "category", "address")}),
        ("统计信息", {"fields": ("click_nums", "fav_nums")}),
        ("媒体与时间", {"fields": ("image", "add_time")}),
    )

# 讲师管理
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    # 列表页显示头像字段
    list_display = ["name", "org", "work_years", "work_position", "image", "click_nums", "fav_nums", "add_time"]
    search_fields = ["name", "work_company", "work_position"]
    list_filter = ["org", "work_years", "add_time"]
    readonly_fields = ["add_time"]
    # 详情页分组展示，添加头像字段
    fieldsets = (
        ("基本信息", {"fields": ("name", "org", "work_years", "work_company", "work_position")}),
        ("教学信息", {"fields": ("points", "click_nums", "fav_nums")}),
        ("媒体信息", {"fields": ("image",)}),  # 头像上传区域
        ("时间", {"fields": ("add_time",)}),
    )