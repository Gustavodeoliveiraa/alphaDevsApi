import json
from category.models import Category
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestRetrieveUpdateDestroyCategory(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('category:get1_update_delete', args=(1,))
        self.client= APIClient()
        Category.objects.create(category_name='teste')
        return super().setUp()
    
    # get retrieve
    def test_get_detail_category_request_with_successful(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_detail_category_request_without_successful(self):
        response =  self.client.get(
            reverse('category:get1_update_delete', args=(2,)), format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # put complete 
    def test_if_all_fields_of_category_is_updated_with_successful(self):
        data = {'category_name': 'teste01'}
        response = self.client.put(self.url, data=data, format='json')
        data = json.loads(response.content)

        self.assertEqual('teste01', data['category_name'])

    def test_category_request_without_successful(self):
        response = self.client.put(self.url, data=None, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # delete Delete

    def test_delete_category_with_successful(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)