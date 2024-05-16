from django.test import TestCase
from django.utils import timezone
from .models import Category, Post, Comment
from django.contrib.auth.models import User
from users.models import Person

class CategoryModelTest(TestCase):
    def test_category_str_representation(self):
        category = Category.objects.create(name='Test Category', description='Test Description')
        self.assertEqual(str(category), 'Test Category')

class PostModelTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(user=User.objects.create(username='testuser'))
        self.category = Category.objects.create(name='Test Category')

    def test_post_str_representation(self):
        post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.person,
            category=self.category,
            is_published=True
        )
        self.assertEqual(str(post), 'Test Post')

    def test_post_published_at_default(self):
        post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.person,
            category=self.category
        )
        self.assertIsNotNone(post.published_at)
        self.assertLess(post.published_at, timezone.now())

class CommentModelTest(TestCase):
    def setUp(self):
        self.person = Person.objects.create(user=User.objects.create(username='testuser'))
        self.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=self.person
        )

    def test_comment_str_representation(self):
        comment = Comment.objects.create(
            content='Test Comment',
            author=self.person,
            post=self.post
        )
        expected_str = f"{self.person.user.first_name} {self.person.user.last_name} - {comment.date_published}"
        self.assertEqual(str(comment), expected_str)

    def test_comment_reply_to_relationship(self):
        comment1 = Comment.objects.create(
            content='Test Comment 1',
            author=self.person,
            post=self.post
        )
        comment2 = Comment.objects.create(
            content='Test Comment 2',
            author=self.person,
            post=self.post,
            reply_to=comment1
        )
        self.assertEqual(comment2.reply_to, comment1)
        self.assertEqual(list(comment1.replies.all()), [comment2])

    def test_comment_is_approved_default(self):
        comment = Comment.objects.create(
            content='Test Comment',
            author=self.person,
            post=self.post
        )
        self.assertFalse(comment.is_approved)