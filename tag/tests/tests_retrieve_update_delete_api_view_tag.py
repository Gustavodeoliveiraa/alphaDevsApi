import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from tag.models import Tag


class TestRetrieveUpdateDestroyTag(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('tag:retrieve_update_delete_tag', args=(1,))
        self.client = APIClient()
        Tag.objects.create(tag_name='tag01')
        return super().setUp()
    
    # get retrieve
    def test_retrieve_tag_with_successful(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_tag_without_successful(self):
        response = self.client.get(
            reverse('tag:retrieve_update_delete_tag', kwargs={'pk':2}), format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    # patch 
    def test_if_fields_of_tag_is_update_with_successful(self):
        data = {'tag_name': 'tag_edited'}
        response = self.client.patch(self.url, data=data, format='json')
        response_data = json.loads(response.content)

        print(response_data)
        self.assertEqual(response_data['tag_name'], 'tag_edited')
        # TODO:CONTINUAR TESTAR SE FOI ATUALIADO ESSA COISA