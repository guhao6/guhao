from django.db import models

# 课程机构表（不变，保留原有代码）
class CourseOrg(models.Model):
    ORG_TYPE = (
        ("pxjg", "培训机构"),
        ("gx", "高校"),
        ("gr", "个人")
    )
    name = models.CharField(max_length=100, verbose_name="机构名称")
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(choices=ORG_TYPE, max_length=20, verbose_name="机构类型")
    address = models.CharField(max_length=200, verbose_name="机构地址")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="机构封面", max_length=200)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 讲师表（添加头像字段 image）
class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="所属机构")
    name = models.CharField(max_length=50, verbose_name="讲师姓名")
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_company = models.CharField(max_length=100, verbose_name="就职公司")
    work_position = models.CharField(max_length=100, verbose_name="公司职位")
    points = models.CharField(max_length=100, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    # 新增讲师头像字段：上传到 media/teacher/年/月 目录
    image = models.ImageField(
        upload_to="teacher/%Y/%m",
        verbose_name="讲师头像",
        max_length=200,
        blank=True,  # 允许空值
        null=True    # 数据库中允许为NULL
    )
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = "讲师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name