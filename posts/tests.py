from django.test import TestCase
from http import HTTPStatus
from model_bakery import baker

from posts.models import Post


# Create your tests here.


class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_representation_of_objects(self):

        post = baker.make(Post)

        self.assertEqual(str(post), post.title)


class HomepageTest(TestCase):
    def setUp(self) -> None:
        post1 = Post.objects.create(
            title="post title 1",
            body="post body 1",
        )
        post2 = Post.objects.create(
            title="post title 2",
            body="post body 2",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")  # client included in django.test

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, "post title 1")
        self.assertContains(response, "post title 2")


class DetailPageTest(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title="Learn Python in this course",
            body="Somebody once told me that Python is the best for learning",
        )

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())  # client is TestCase class

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertContains(response, self.post.created_at)



