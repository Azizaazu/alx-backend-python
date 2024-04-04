#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map function.
"""


import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function."""

    @parameterized.expand([
        ({}, ("a",), KeyError, "Key not found: 'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "Key not found: 'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception, expected_message):
        """Test access_nested_map method for raising KeyError."""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)

class TestGetJson(unittest.TestCase):
    """Test case for get_json function."""

    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json method."""
        mock_get.return_value = Mock(json=lambda: test_payload)
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator."""

    class TestClass:
        """Class to test memoize decorator."""

        def a_method(self):
            """Method to be memoized."""
            return 42

        @memoize
        def a_property(self):
            """Property memoized with memoize decorator."""
            return self.a_method()

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_method):
        """Test memoize decorator."""
        test_instance = self.TestClass()

        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        mock_method.assert_called_once()

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

if __name__ == "__main__":
    unittest.main()
