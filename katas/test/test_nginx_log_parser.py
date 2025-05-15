import unittest
from typing import Dict
from katas.nginx_log_parser import parse_log

class TestParseLog(unittest.TestCase):

    def setUp(self):
        self.sample_log = (
            '127.0.0.1 - - [12/Mar/2023:12:34:56 +0000] '
            '"GET /index.html HTTP/1.1" 200 1024 '
            '"-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"'
        )

    def test_parse_log_valid(self):
        expected = {
            "client_ip": "127.0.0.1",
            "date": "12/Mar/2023:12:34:56 +0000",
            "http_method": "GET",
            "path": "/index.html",
            "http_version": "1.1",
            "status": "200",
            "response_bytes": "1024",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        result = parse_log(self.sample_log)
        self.assertEqual(result, expected)

    def test_parse_log_partial_missing(self):
        # Missing user agent
        log = (
            '192.168.0.1 - - [10/Apr/2024:08:00:00 +0000] '
            '"POST /submit HTTP/2.0" 404 512 "-" "-"'
        )
        expected = {
            "client_ip": "192.168.0.1",
            "date": "10/Apr/2024:08:00:00 +0000",
            "http_method": "POST",
            "path": "/submit",
            "http_version": "2.0",
            "status": "404",
            "response_bytes": "512",
            "user_agent": "-"
        }
        result = parse_log(log)
        self.assertEqual(result, expected)

    def test_parse_log_invalid(self):
        # Completely malformed log
        log = "This is not a log line"
        result = parse_log(log)
        for value in result.values():
            self.assertIsNone(value)

    def test_parse_log_different_method(self):
        log = (
            '10.0.0.1 - - [01/Jan/2025:01:23:45 +0000] '
            '"DELETE /api/resource HTTP/1.0" 204 0 "-" "curl/7.68.0"'
        )
        expected = {
            "client_ip": "10.0.0.1",
            "date": "01/Jan/2025:01:23:45 +0000",
            "http_method": "DELETE",
            "path": "/api/resource",
            "http_version": "1.0",
            "status": "204",
            "response_bytes": "0",
            "user_agent": "curl/7.68.0"
        }
        result = parse_log(log)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

