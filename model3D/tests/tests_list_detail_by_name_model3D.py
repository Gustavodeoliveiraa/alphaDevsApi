import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from model3D.models import Model3D
from utils import create_fake_3d_model

class TestList3dModelByName(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('3d_model:get_by_name', kwargs={'name': 'Test01'})
        return super().setUp()
    
    def test_list_3d_model_by_name_request_with_successful(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_3d_model_by_name_filter_correctly(self):
        create_fake_3d_model(Model3D)
        
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertIn('Test01', data[0]['product_name'])

    def test_list_multiples_3d_models_filtered_by_name(self):
        [create_fake_3d_model(Model3D, f'prod0{_}') for _ in range(1, 4)]

        url = reverse('3d_model:get_by_name', kwargs={'name': 'prod'})
        response = self.client.get(url, format='json')
        data = json.loads(response.content)

        self.assertEqual(len(data), 3)
        self.assertIn(data[0]['product_name'], 'prod01')
        self.assertIn(data[1]['product_name'], 'prod02')
        self.assertIn(data[2]['product_name'], 'prod03')