from django.test import TestCase
from http import HTTPStatus
from django.contrib.auth import get_user_model
from model_bakery import baker

from posts.models import Post


User=get_user_model()

class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_representation_of_objects(self):

        post = baker.make(Post)

        self.assertEqual(str(post), post.title)
        self.assertTrue(isinstance(post, Post))


class HomepageTest(TestCase):
    def setUp(self) -> None:
        self.post1 = baker.make(Post)
        self.post2 = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")  # client included in django.test

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = baker.make(Post)

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertContains(response, self.post.created_at.strftime('%b. %d, %Y'))


class PostAuthorTest(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(User)
        self.post = Post.objects.create(
            title = "Test title",
            body = "Test body of post",
            author = self.user #Todo
        )

    def test_post_belongs_to_user(self):
        self.assertTrue(hasattr(self.post, 'author'))

    def test_author_is_instance_of_user_model(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.post.author, self.user)
    
