Django 在线学习平台 (Study Platform)
基于 Python + Django 开发的模块化在线教育学习平台，适用于个人设计、毕业设计、课程设计等场景。

项目简介
本项目是一款轻量化、模块化的在线学习平台系统，采用 Django MTV 架构模式开发。
系统实现了课程管理、教育机构管理、用户交互及后台数据管理等完整功能，界面简洁、结构清晰、易于部署与扩展。

核心功能模块
课程管理模块（courses）
- 课程列表展示与分页
- 课程分类、搜索、筛选
- 课程详情页面展示
- 课程热度、学习人数统计

教育机构模块（organizations）
- 教育机构信息展示
- 机构列表与详情页
- 机构所属讲师展示

用户操作模块（operations）
- 用户注册、登录、退出
- 课程收藏、评论功能
- 用户学习记录管理

后台管理系统
- 基于 Django Admin 后台
- 课程、机构、用户、评论统一管理
- 数据可视化操作

技术栈
- 后端：Python 3.x + Django 4.2.x
- 前端：HTML5、CSS3、JavaScript、Bootstrap
- 数据库：SQLite3（开发环境）
- 图片处理：Pillow
- 开发工具：PyCharm / VS Code

快速运行指南
进入项目目录
bash
cd study_platform

创建虚拟环境（推荐）
bash
运行
python -m venv venv

激活虚拟环境
Windows：
bash
运行
venv\Scripts\activate
Mac/Linux：
bash
运行
source venv/bin/activate

安装依赖
bash
运行
pip install -r requirements.txt

数据库迁移
bash
运行
python manage.py makemigrations
python manage.py migrate

创建超级管理员
bash
运行
python manage.py createsuperuser

启动项目
bash

运行
python manage.py runserver

访问地址
前台页面：http://127.0.0.1:8000
后台管理：http://127.0.0.1:8000/admin

项目结构
study_platform/
├── courses/          # 课程模块
├── operations/       # 用户操作模块
├── organizations/    # 教育机构模块
├── study_platform/   # 项目配置
├── templates/        # 页面模板
├── static/           # 静态资源（CSS/JS/图片）
├── media/            # 上传文件
├── db.sqlite3        # 数据库
└── manage.py         # 启动文件
设计说明
项目采用 Django 经典 MTV 架构，实现前后端分离式开发，代码结构清晰、模块划分合理，便于维护与二次开发。整体界面采用响应式布局，适配电脑端与移动端访问，符合现代 Web 设计规范。
作者信息
姓名：孤浩
项目类型：个人设计 / 毕业设计
开发环境：Python + Django
用途：学习实践、课程设计、毕业设计展示

依赖库
Django==4.2.16
django-ckeditor==6.7.1
django-crispy-forms==2.0
crispy-bootstrap4==2023.1
Pillow==10.2.0
mysqlclient==2.2.1
python-dotenv==1.0.1
