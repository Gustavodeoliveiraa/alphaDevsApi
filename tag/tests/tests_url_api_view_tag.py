from django.test import TestCase
from django.urls import reverse

class TagUrlTest(TestCase):
    def test_url_list_tag(self):
        self.assertEqual(reverse('tag:list_create_tag'), '/api/v1/tags/')
        