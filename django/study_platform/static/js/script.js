// 等待DOM加载完成后执行脚本
document.addEventListener('DOMContentLoaded', function() {
    // 1. 轮播图自动播放（增强：鼠标悬停暂停，离开继续）
    const carousel = document.getElementById('bannerCarousel');
    if (carousel) {
        const bsCarousel = new bootstrap.Carousel(carousel, {
            interval: 5000, // 5秒自动切换
            ride: 'carousel'
        });

        // 鼠标悬停暂停轮播
        carousel.addEventListener('mouseenter', () => bsCarousel.pause());
        // 鼠标离开继续轮播
        carousel.addEventListener('mouseleave', () => bsCarousel.cycle());
    }

    // 2. 搜索框回车提交
    const searchInput = document.querySelector('input[name="search"]');
    if (searchInput) {
        searchInput.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                this.closest('form').submit();
            }
        });
    }

    // 3. 课程卡片点击效果（可选：添加点击反馈）
    const courseCards = document.querySelectorAll('.card');
    courseCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // 排除按钮点击（避免重复触发）
            if (!e.target.closest('a')) {
                const link = this.querySelector('a');
                if (link) window.location.href = link.href;
            }
        });
    });

    // 4. 提示框自动关闭（若后续添加alert提示可使用）
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            setTimeout(() => alert.remove(), 300);
        }, 3000); // 3秒后自动关闭
    });
});

// 工具函数：格式化时间（后续扩展视频时长等功能可用）
function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}分${secs}秒`;
}

// 工具函数：本地存储学习进度（后续扩展课程学习功能可用）
function saveLearnProgress(courseId, videoId, progress) {
    const key = `learn_${courseId}_${videoId}`;
    localStorage.setItem(key, progress);
}

// 工具函数：获取学习进度
function getLearnProgress(courseId, videoId) {
    const key = `learn_${courseId}_${videoId}`;
    return localStorage.getItem(key) || 0;
}