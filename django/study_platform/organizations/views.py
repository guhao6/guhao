# from django.shortcuts import render
# from .models import CourseOrg  # 导入机构模型
#
# def org_list(request):
#     all_orgs = CourseOrg.objects.all()  # 查询所有机构
#     return render(request, '/organizations/org_list.html', {
#         'orgs': all_orgs  # 传递给模板
#     })

from django.shortcuts import render
from .models import CourseOrg, Teacher  # 根据您的模型调整

def org_list(request):
    try:
        all_orgs = CourseOrg.objects.all()
        return render(request, 'organizations/org_list.html', {'orgs': all_orgs})
    except Exception as e:
        print(f"org_list error: {e}")
        raise

def teacher_list(request):
    try:
        all_teachers = Teacher.objects.all()  # 确保Teacher模型存在
        return render(request, 'organizations/teacher_list.html', {'teachers': all_teachers})
    except Exception as e:
        print(f"teacher_list error: {e}")
        raise