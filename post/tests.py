from rest_framework.test import APIRequestFactory, APITestCase, force_authenticate
from .views import *
from django.contrib.auth import get_user_model
from .models import *
from collections import OrderedDict


User = get_user_model()


class TestPost(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email='test@gmail.com',
            password='123456',
            is_active=True,
            name='Test'
        )
        self.user2 = User.objects.create_user(
            email='test2@gmail.com',
            password='123456',
            is_active=True,
            name='Test'
        )
        tag = Tag.objects.create(title='tag1')
        self.tags = (tag,)
        self.category = Category.objects.create(title='cat1')
        posts = [
            Post(author=self.user, body='test', title='post1', slug='post1'),
            Post(author=self.user, body='test', title='post2',  category=self.category, slug='post2')
        ]
        Post.objects.bulk_create(posts)

    def test_list(self):
        request = self.factory.get('posts/')
        view = PostViewset.as_view({'get': 'list'})
        response = view(request)
        # print(response.data)
        # print(len(response.data))

        assert type(response.data) == OrderedDict
        # assert len(response.data) == 2


    def test_update(self):
        data = {
            'body': 'update body'
        }
        post = Post.objects.all()[0]
        request = self.factory.patch(f'posts/{post.slug}/', data, format='json')
        force_authenticate(request, self.user)
        view = PostViewset.as_view({'patch': 'partial_update'})
        reponse = view(request, pk=post.slug)

        # print(reponse.data)
        assert Post.objects.get(slug=post.slug).body == data['body']


    def test_create(self):
        data = {
            'body': 'test create',
            'title': 'post3',
            'category': 'cat1',
        }

        request = self.factory.post('posts/', data, format='json')
        force_authenticate(request, self.user)
        view = PostViewset.as_view({'post': 'create'})

        response = view(request)
        # print(response.data)
        assert Post.objects.filter(author=self.user, title=data['title']).exists()




