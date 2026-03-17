from django.contrib import admin
from .models import CourseCategory, Banner, Course, CourseChapter, CourseVideo

# 课程分类管理
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    # 列表显示的字段
    list_display = ["name", "desc", "add_time"]
    # 搜索字段
    search_fields = ["name"]
    # 筛选字段
    list_filter = ["name", "add_time"]
    # 只读字段（自动生成的时间不允许编辑）
    readonly_fields = ["add_time"]

# 广告轮播图管理
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "url", "index", "is_active", "add_time"]
    search_fields = ["title"]
    list_filter = ["index", "is_active", "add_time"]
    # 列表页直接编辑的字段（原生Admin也支持）
    list_editable = ["is_active", "index"]
    readonly_fields = ["add_time"]

# 课程管理
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "org", "teacher", "degree", "students", "is_recommend", "add_time"]
    search_fields = ["name", "desc", "detail"]
    list_filter = ["category", "org", "teacher", "degree", "is_recommend", "add_time"]
    list_editable = ["is_recommend"]
    readonly_fields = ["add_time"]
    # 字段分组（详情页更清晰）
    fieldsets = (
        ("基础信息", {"fields": ("name", "category", "org", "teacher", "degree")}),
        ("课程描述", {"fields": ("desc", "detail")}),
        ("统计信息", {"fields": ("learn_times", "students", "fav_nums", "click_nums")}),
        ("媒体与状态", {"fields": ("image", "is_recommend")}),
        ("时间", {"fields": ("add_time",)}),
    )

# 课程章节管理
@admin.register(CourseChapter)
class CourseChapterAdmin(admin.ModelAdmin):
    list_display = ["course", "name", "learn_times", "add_time"]
    search_fields = ["course__name", "name"]  # 跨表搜索
    list_filter = ["course", "add_time"]
    readonly_fields = ["add_time"]

# 课程视频管理
@admin.register(CourseVideo)
class CourseVideoAdmin(admin.ModelAdmin):
    list_display = ["chapter", "name", "learn_times", "add_time"]
    search_fields = ["chapter__name", "name"]
    list_filter = ["chapter", "add_time"]
    readonly_fields = ["add_time"]