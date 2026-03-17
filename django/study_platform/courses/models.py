from django.db import models
from organizations.models import Teacher, CourseOrg

# 课程分类表
class CourseCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="分类名称")
    desc = models.TextField(blank=True, null=True, verbose_name="分类描述")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 广告轮播图表
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="广告标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="广告图片", max_length=200)
    url = models.URLField(max_length=200, verbose_name="跳转链接")
    index = models.IntegerField(default=0, verbose_name="排序（数字越大越靠前）")
    is_active = models.BooleanField(default=True, verbose_name="是否启用")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "广告轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

# 课程表
class Course(models.Model):
    DEGREE = (
        ("cj", "初级"),
        ("zj", "中级"),
        ("gj", "高级")
    )
    name = models.CharField(max_length=100, verbose_name="课程名称")
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, verbose_name="课程分类")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="授课老师")
    desc = models.CharField(max_length=300, verbose_name="课程简介")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=DEGREE, max_length=2, verbose_name="难度")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟）")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="课程封面", max_length=200)
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    is_recommend = models.BooleanField(default=False, verbose_name="是否推荐")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 课程章节表
class CourseChapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="所属课程")
    name = models.CharField(max_length=100, verbose_name="章节名称")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟）")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.course.name} - {self.name}"

# 课程视频表
class CourseVideo(models.Model):
    chapter = models.ForeignKey(CourseChapter, on_delete=models.CASCADE, verbose_name="所属章节")
    name = models.CharField(max_length=100, verbose_name="视频名称")
    video_url = models.FileField(upload_to="videos/%Y/%m", verbose_name="视频文件", max_length=200)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟）")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name