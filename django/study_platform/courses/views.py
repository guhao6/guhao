from django.shortcuts import render
from .models import Banner, Course, CourseChapter, CourseVideo

# 首页
def index(request):
    banners = Banner.objects.filter(is_active=True).order_by("-index")  # 广告轮播图
    recommend_courses = Course.objects.filter(is_recommend=True)[:4]   # 推荐课程
    return render(request, 'index.html', {
        'banners': banners,
        'recommend_courses': recommend_courses
    })

# 课程列表页
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {
        'courses': courses
    })

# 课程详情页
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    chapters = CourseChapter.objects.filter(course=course)
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'chapters': chapters
    })

# 视频播放页
def course_video(request, chapter_id):
    chapter = CourseChapter.objects.get(id=chapter_id)
    videos = CourseVideo.objects.filter(chapter=chapter)
    return render(request, 'courses/course_video.html', {
        'chapter': chapter,
        'videos': videos
    })