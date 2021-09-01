from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse, resolve
from blog.views import PostDetailView, about
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User
# Create your tests here.


class URLTests(TestCase):

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_aboutpage(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
    
    def test_about(self):
        url = reverse('blog-about')
        print(resolve(url))
        self.assertEqual(resolve(url).func, about)

class TestViews(TestCase):
    
    def setUp(self):
        self.client=Client()
        self.home_url=reverse('blog-home')
        self.post_detail_url=reverse('post-detail',kwargs={'pk':1})
        user=User.objects.create(username="unittest_user", password="zh000000")
        Post.objects.create(
            title='unittest',
            content='I am doing unittest',
            author=user
        )

    def test_project_home_GET(self):
        response=self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_project_post_detail_GET(self):
        print(self.post_detail_url)
        response=self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')