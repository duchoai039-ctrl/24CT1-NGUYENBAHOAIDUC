import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Blog.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from devBlog.models import Tag

tags = [
    'Công nghệ',
    'Giải trí',
    'Thể thao',
    'Du lịch',
    'Ẩm thực',
    'Giáo dục',
    'Sức khỏe',
    'Âm nhạc',
    'Phim ảnh',
    'Game',
]

for t in tags:
    Tag.objects.get_or_create(name=t)

print(f'Done! Created {Tag.objects.count()} tags.')
