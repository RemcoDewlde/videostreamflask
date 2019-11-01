import unittest
from main import app


class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as client:
            response = client.get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)

    def test_video_feed(self):
        with app.test_client() as client:
            response = client.get('/video_feed', content_type='html/text')
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
