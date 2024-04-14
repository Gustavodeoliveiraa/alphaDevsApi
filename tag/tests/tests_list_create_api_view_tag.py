import json
from tag.models import Tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestListCrateTags(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('tag:list_create_tag')
        self.client = APIClient()
        return super().setUp()
    
    # get
    def test_list_tag_request_with_successful(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_tag_request_without_successful(self):
        response = self.client.get(f'{self.url}/')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_if_tag_contains_object_created(self):
        Tag.objects.create(tag_name='teste01')
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual('teste01', data[0]['tag_name'])

    def test_tag_error_on_nonexistent_object(self):
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)
        print(data)

        self.assertNotEqual(len(data), 1)

    def test_tag_list_return_correct_format(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response['content-Type'], 'application/json')

    def test_if_tag_returns_correct_number_of_items_after_creation(self):
        [Tag.objects.create(tag_name=f'teste0{_}') for _ in range(3)]
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertEqual(len(data), 3)

    # post

    def test_creation_of_tag_with_successful(self):
        data = {'tag_name': 'tag01'}
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_creation_of_tag_without_successful(self):
        data = {'tag_name': ''}
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)