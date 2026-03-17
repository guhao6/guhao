from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from organizations.models import CourseOrg, Teacher

# 用户收藏表
class UserFavorite(models.Model):
    FAV_TYPE = (
        (1, "课程"),
        (2, "机构"),
        (3, "讲师")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    fav_id = models.IntegerField(verbose_name="收藏ID")
    fav_type = models.IntegerField(choices=FAV_TYPE, verbose_name="收藏类型")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.username}收藏了{self.get_fav_type_display()}"

# 用户选课表
class UserLearnCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户选课"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.username}学习了{self.course.name}"