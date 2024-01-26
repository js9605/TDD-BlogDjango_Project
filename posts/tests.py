from django.test import TestCase
from http import HTTPStatus

from posts.models import Post

# Create your tests here.


class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)

    def test_string_representation_of_objects(self):
        
        post = Post.objects.create(
            title="post title",
            body="post body",
        )

        self.assertEqual(str(post), post.title)

class HomepageTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(
            title="post title 1",
            body="post body 1",
        )
        Post.objects.create(
            title="post title 2",
            body="post body 2",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get('/') # client included in django.test 

        self.assertTemplateNotUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)