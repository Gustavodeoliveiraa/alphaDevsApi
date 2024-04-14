from django.test import TestCase
from django.urls import reverse

class Model3DUrlTest(TestCase):
    def test_url_list_3d_model(self):
        self.assertEqual(reverse('3d_model:list'), '/api/v1/model/3d_model')
    
    def test_url_list_detail_3d_model(self):
        self.assertEqual(reverse('3d_model:create', args=(1,)), '/api/v1/model/3d_model/1/')

    def test_url_model_3d_get_by_name(self):

        self.assertEqual(
            reverse('3d_model:get_by_name', kwargs={'name': 'teste01'}),
            '/api/v1/model/search_3d_model/teste01'
        )