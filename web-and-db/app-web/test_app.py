import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()