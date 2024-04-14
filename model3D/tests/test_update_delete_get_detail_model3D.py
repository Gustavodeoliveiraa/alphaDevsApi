import os
import json
import glob
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from  model3D.models import Model3D
from utils import create_fake_3d_model

class TestRetrieveUpdateDestroy3dModel(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('3d_model:create', args=(1,))
        self.client = APIClient()
        create_fake_3d_model(Model3D)
        return super().setUp()
    
    # get retrieve
    def test_get_detail_3d_model_request_with_successful(self):
        response = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_detail_3d_model_request_without_successful(self):
        response = self.client.get(reverse('3d_model:create', args=(2,)))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    #put complete update
    def test_if_all_fields_of_3d_model_is_updated_with_successful(self):
        file_name = '200x200.jpg'
        directory_name = 'media/model3d'

        full_path = os.path.abspath(os.path.join(directory_name, file_name))
        with open(full_path, 'rb') as image_file:
            file = SimpleUploadedFile('teste.jpg', image_file.read(), content_type='image/jpeg')
            data = {
                'product_name': 'nome_atualizado',
                'product_image': file,
                'product_description': 'Produto atualizado',                      
                'product_price': 999,
                'product_height': 99.9,
                'product_width': 99.9,
            }
        
            response = self.client.put(self.url, data=data, format='multipart')
            response_data = json.loads(response.content)

            self.assertEqual(response_data['product_name'], 'nome_atualizado')
            self.assertEqual(response_data['product_image'], 'http://testserver/media/model3d/teste.jpg')
            self.assertEqual(response_data['product_description'], 'Produto atualizado')
            self.assertEqual(response_data['product_price'], 999)
            self.assertEqual(response_data['product_height'], 99.9)
            self.assertEqual(response_data['product_width'], 99.9)

        # remove the image that was created
        pattern = os.path.join(directory_name, 'test*.jpg')
        files_to_remove = glob.glob(pattern)

        for file_path in files_to_remove:
            os.remove(file_path)
    
    def test_3d_model_request_without_successful(self):

        response = self.client.put(self.url, data=None, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_3d_model_fields_validation_with_invalid_data(self):
        data = {
            'product_name': '',
            'product_image': '',
            'product_description': '',                      
            'product_price': None,
            'product_height': None,
            'product_width': '',
        }
        response = self.client.put(self.url, data=data, format='json')
        data_response = json.loads(response.content)
        self.assertEqual(data_response['product_name'][0], 'This field may not be blank.')
        self.assertEqual(
            data_response['product_image'][0], 'The submitted data was not a file. Check the encoding type on the form.'
        )
        self.assertEqual(data_response['product_description'][0], 'This field may not be blank.')
        self.assertEqual(data_response['product_price'][0], 'This field may not be null.')
        self.assertEqual(data_response['product_height'][0], 'This field may not be null.')
        self.assertEqual(data_response['product_width'][0], 'A valid number is required.')


    
    #patch parcial update
    def test_partial_3d_model_update_with_successful(self):
        data = {
            'product_name': 'nome_atualizado',
            'product_price': 0,
        }
        response = self.client.patch(self.url, data=data, format='json')
        data_response = json.loads(response.content)
        self.assertEqual(data_response['product_name'], 'nome_atualizado')
        self.assertEqual(data_response['product_price'], 0)

    def test_partial_3d_model_update_without_successful(self):
        data = {
            'product_name': '',
            'product_price': '',
        }
        response = self.client.patch(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #delete Delete
    
    def test_delete_a_3d_model_with_successful(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)