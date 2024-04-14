import json
from category.models import Category
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestListCrateCategory(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('category:list_create')
        self.client = APIClient()
        return super().setUp()
    
    # get requests
    def test_list_category_with_successful(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_category_request_without_successful(self):
        new_url = f'{self.url}/'
        response = self.client.get(new_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_category_contain_object_created(self):
        Category.objects.create(category_name='teste01')
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertEqual('teste01', data[0]['category_name'])

    def test_list_category_error_on_nonexistent_object(self):
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertNotIn('none', data)
        self.assertEqual(len(data), 0)

    def test_list_category_return_correct_format(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response['content-type'], 'application/json')

    def test_list_category_returns_correct_number_of_items_after_creation(self):
        [Category.objects.create(category_name=f'teste0{_}') for _ in range(3)]
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertEqual(len(data), 3)


    # post requests
    def test_if_category_is_created_with_fail(self):
        response = self.client.post(self.url, data={})
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
