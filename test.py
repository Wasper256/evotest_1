"""Testing."""
from app import app
import unittest


class FlaskTestCase(unittest.TestCase):
    """Simple unittest class."""

    def test_index_page(self):
        """Ensure that Flask was set up correctly and main page works."""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_input_name(self):
        """Ensure correct name input."""
        tester = app.test_client()
        response = tester.post(
            '/',
            data=dict(name="ThisIsJustVeryMegaSuperLongTestName"),
            follow_redirects=True
        )
        self.assertIn(b'New name successfully added!', response.data)

    def test_delete_name(self):
        """Ensure correct name delete."""
        tester = app.test_client()
        response = tester.post(
            '/',
            data=dict(delname="ThisIsJustVeryMegaSuperLongTestName"),
            follow_redirects=True
        )
        self.assertIn(b'Selected name was deleted', response.data)

    def test_random(self):
        """Ensure correct randomizer."""
        tester = app.test_client()
        response = tester.post(
            '/',
            data=dict(lucky="action"),
            follow_redirects=True
        )
        self.assertIn(b'Winners is:', response.data)
if __name__ == '__main__':
    unittest.main()
