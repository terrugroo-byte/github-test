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


if __name__ == "__main__":
    unittest.main()
