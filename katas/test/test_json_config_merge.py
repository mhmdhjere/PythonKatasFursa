import unittest
import tempfile
import json
import os
from typing import Any

from katas.json_config_merge import json_merge, json_configs_merge
class TestJsonMergeFunctions(unittest.TestCase):

    def test_json_merge_basic(self):
        j1 = {"a": 1, "b": {"x": 10}}
        j2 = {"b": {"y": 20}, "c": 3}
        result = json_merge(j1.copy(), j2)
        expected = {"a": 1, "b": {"x": 10, "y": 20}, "c": 3}
        self.assertEqual(result, expected)

    def test_json_merge_overwrite(self):
        j1 = {"a": 1, "b": 2}
        j2 = {"b": 3, "c": 4}
        result = json_merge(j1.copy(), j2)
        expected = {"a": 1, "b": 3, "c": 4}
        self.assertEqual(result, expected)

    def test_json_merge_nested(self):
        j1 = {"a": {"b": {"c": 1}}}
        j2 = {"a": {"b": {"d": 2}}}
        result = json_merge(j1.copy(), j2)
        expected = {"a": {"b": {"c": 1, "d": 2}}}
        self.assertEqual(result, expected)

    def test_json_configs_merge(self):
        # Create temporary JSON files
        with tempfile.TemporaryDirectory() as tmpdir:
            file1 = os.path.join(tmpdir, "file1.json")
            file2 = os.path.join(tmpdir, "file2.json")

            data1 = {"a": 1, "b": {"x": 10}}
            data2 = {"b": {"y": 20}, "c": 3}

            with open(file1, "w") as f1:
                json.dump(data1, f1)
            with open(file2, "w") as f2:
                json.dump(data2, f2)

            result = json_configs_merge(file1, file2)
            expected = {"a": 1, "b": {"x": 10, "y": 20}, "c": 3}
            self.assertEqual(result, expected)

    def test_json_configs_merge_empty(self):
        result = json_configs_merge()
        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()

