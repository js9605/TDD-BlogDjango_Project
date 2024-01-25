from django.test import TestCase

from posts.models import Post

# Create your tests here.


class PostModelTest(TestCase):
    
    def test_post_model_exist(self):
        posts = Post.objects.count()

        self.assertEqual(posts, 0)
