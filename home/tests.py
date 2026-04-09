from django.test import TestCase
from django.urls import reverse


class HomeTestCase(TestCase):
    
    def test_home(self):
        response = self.client.get(reverse('articles:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_page(self):
        response = self.client.get(reverse('articles:create'))
        self.assertEqual(response.status_code, 200)  
        response = self.client.post(reverse('articles:create'), {
            'title': 'New Article', 
            'content': 'This is another test article.'
        })
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('articles:detail', kwargs={'slug': 'new-article'}))
        self.assertEqual(response.status_code, 200)

    