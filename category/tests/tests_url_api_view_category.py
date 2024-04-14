from django.test import TestCase
from django.urls import reverse

class CategoryUrlTest(TestCase):
    def test_url_list_tag(self):
        self.assertEqual(reverse('category:list_create'), '/api/v1/category/')

    def test_url_list_detail(self):
        self.assertEqual(
            reverse('category:get1_update_delete', args=(1,)),
            '/api/v1/category/1'
    )   