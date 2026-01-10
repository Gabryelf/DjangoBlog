from django.core.management.base import BaseCommand
from posts.models import Category, Post
from django.contrib.auth.models import User
from django.utils import timezone


class Command(BaseCommand):
    help = 'Создает тестовые данные для блога'

    def handle(self, *args, **kwargs):
        # Создаем пользователя
        user, created = User.objects.get_or_create(
            username='testuser',
            defaults={'email': 'test@example.com'}
        )
        if created:
            user.set_password('testpass123')
            user.save()

        # Создаем категории
        categories = []
        for cat_name in ['Новости', 'Технологии', 'Спорт', 'Разное']:
            category, created = Category.objects.get_or_create(name=cat_name)
            categories.append(category)
            self.stdout.write(f'Создана категория: {cat_name}')

        # Создаем посты
        posts_data = [
            {
                'title': 'Мой первый пост',
                'content': 'Это содержание моего первого поста в блоге.',
                'category': categories[0],
                'author': user,
            },
            {
                'title': 'Новые технологии',
                'content': 'Обзор последних технологических новинок.',
                'category': categories[1],
                'author': user,
            },
            {
                'title': 'Спортивные новости',
                'content': 'Свежие новости из мира спорта.',
                'category': categories[2],
                'author': user,
            },
            {
                'title': 'Интересный факт',
                'content': 'Сегодня я узнал кое-что интересное!',
                'category': categories[3],
                'author': user,
            },
        ]

        for post_data in posts_data:
            post = Post.objects.create(**post_data)
            self.stdout.write(f'Создан пост: {post.title}')

        self.stdout.write(self.style.SUCCESS('Тестовые данные созданы успешно!'))
