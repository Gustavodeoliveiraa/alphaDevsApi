import os
import json
import glob
import random
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from model3D.models import Model3D
from utils import create_fake_3d_model

class TestListCreate3DModel(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('3d_model:list')
        self.client = APIClient()
        return super().setUp()
    
    # get requests
    def test_list_3d_model_request_with_successful(self):
        response = self.client.get(self.url, format='json')
        create_fake_3d_model(Model3D)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_3d_model_request_without_successful(self):
        new_url = f'{self.url}/'
        response = self.client.get(new_url)
       
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_3d_model_contain_object_created(self):
        create_fake_3d_model(Model3D, name='Carla', product_price=20.0)
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertEqual('Carla', data[0]['product_name'])
        self.assertEqual(20.0, data[0]['product_price'])

    def test_list_3d_model_error_on_nonexistent_object(self):
        response = self.client.get(self.url, format='json')
        data = json.loads(response.content)

        self.assertNotIn('Carla', data)

    def test_list_3d_return_correct_format(self):
        response = self.client.get(self.url, format='json')
       
        self.assertEqual(response['content-Type'], 'application/json')

    def test_list_3d_returns_correct_number_of_items_after_creation(self):
            random_number= random.randint(1, 10)
            [create_fake_3d_model(Model3D) for _ in range(random_number)]
            response = self.client.get(self.url, format='json')
            data = json.loads(response.content)

            self.assertEqual(len(data), random_number)

    # post requests
    def test_if_3d_model_is_created_with_successfully(self):
        file_name = '200x200.jpg'
        directory_name = 'media/model3d'

        full_path = os.path.abspath(os.path.join(directory_name, file_name))
        with open(full_path, 'rb') as image_file:

            data = {
                'product_name': 'Sonic3D',
                'product_image': image_file,
                'product_description': 'Produto ok',
                'product_price': 100.0,
                'product_height': 1.50,
                'product_width': 1.20,
            }
            response = self.client.post(self.url, data=data)

            self.assertEqual(
                response.status_code, status.HTTP_201_CREATED
            )
        
        #remove the image that was created
        pattern = os.path.join(directory_name, '200x200_*.jpg')
        files_to_remove = glob.glob(pattern)

        for file in files_to_remove:
            if not os.path.basename(file) == '200x200.jpg':
                os.remove(file)

    def test_if_3d_model_with_creation_fail(self):
        data = {
            'product_name': 'Sonic3D',
            'product_image': 'image_file',
            'product_description': 'Produto ok',
            'product_price': 100.0,
            'product_height': 1.50,
            'product_width': 1.20,
        }
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)