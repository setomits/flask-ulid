import unittest

from flask import Flask, request
from flask_ulid import FlaskULID


class TestFlaskULID(unittest.TestCase):
    VALID_VALUE = '01D1XGHKZBSDSRZ0NH5MCST2M4'

    INVALID_VALUES = (
        '01D1XGHKZBSDSRZ0NH5MCST2M',   # too short
        '01D1XGHKZBSDSRZ0NH5MCST2M-',  # invalid character
        '01D1XGHKZBSDSRZ0NH5MCST2M4X'  # too long
    )

    def setUp(self):
        self.app = Flask(__name__)
        FlaskULID(self.app)

        @self.app.route('/article/<ulid:val>')
        def article(val):
            return "OK"

        self.client = self.app.test_client()

    def test_article(self):
        with self.client.get('/article/'+self.VALID_VALUE) as resp:
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, b'OK')

        for v in self.INVALID_VALUES:
            with self.client.get('/article/'+v) as resp:
                self.assertEqual(resp.status_code, 404)


if __name__ == '__main__':
    unittest.main()
