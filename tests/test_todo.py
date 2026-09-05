import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import todo  # noqa: E402


class TestTodo(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        tasks.append({"text": "buy milk", "done": False})
        self.assertEqual(tasks, [{"text": "buy milk", "done": False}])

    def test_complete_task(self):
        tasks = [{"text": "buy milk", "done": False}]
        tasks[0]["done"] = True
        self.assertTrue(tasks[0]["done"])

    def test_remove_task(self):
        tasks = [{"text": "buy milk", "done": False}, {"text": "walk dog", "done": False}]
        removed = tasks.pop(0)
        self.assertEqual(removed["text"], "buy milk")
        self.assertEqual(len(tasks), 1)

    def test_clear_tasks(self):
        tasks = [{"text": "buy milk", "done": False}, {"text": "walk dog", "done": False}]
        tasks.clear()
        self.assertEqual(tasks, [])

    def test_count_remaining_excludes_done_tasks(self):
        tasks = [
            {"text": "buy milk", "done": True},
            {"text": "walk dog", "done": False},
            {"text": "pay rent", "done": False},
        ]
        self.assertEqual(todo.count_remaining(tasks), 2)

    def test_parse_index_valid(self):
        tasks = [{"text": "buy milk", "done": False}]
        self.assertEqual(todo.parse_index("0", tasks), 0)

    def test_parse_index_out_of_range(self):
        tasks = [{"text": "buy milk", "done": False}]
        self.assertIsNone(todo.parse_index("99", tasks))

    def test_parse_index_negative(self):
        tasks = [{"text": "buy milk", "done": False}]
        self.assertIsNone(todo.parse_index("-1", tasks))

    def test_parse_index_non_numeric(self):
        tasks = [{"text": "buy milk", "done": False}]
        self.assertIsNone(todo.parse_index("abc", tasks))


if __name__ == "__main__":
    unittest.main()
