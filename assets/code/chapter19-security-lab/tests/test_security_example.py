"""Independent positive and negative expectations, all synthetic data."""
import importlib.util
from pathlib import Path
import sqlite3
import sys
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "security_example.py"
spec = importlib.util.spec_from_file_location("chapter19_example", SOURCE)
example = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = example
spec.loader.exec_module(example)


class OwnershipTests(unittest.TestCase):
    def setUp(self):
        self.owner = example.Actor("user-a", True)
        self.other = example.Actor("user-b", True)
        self.task = example.Task("task-1", "user-a")

    def test_active_owner_can_access(self):
        self.assertIs(example.may_access_task(self.owner, self.task), True)

    def test_other_active_user_cannot_access(self):
        self.assertIs(example.may_access_task(self.other, self.task), False)

    def test_inactive_owner_cannot_access(self):
        self.assertIs(example.may_access_task(example.Actor("user-a", False), self.task), False)

    def test_anonymous_cannot_access(self):
        self.assertIs(example.may_access_task(None, self.task), False)

    def test_completion_returns_new_completed_task(self):
        result = example.complete_task(self.owner, self.task)
        self.assertEqual(result, example.Task("task-1", "user-a", "completed"))
        self.assertEqual(self.task.status, "open")

    def test_denied_completion_preserves_source(self):
        for actor in (self.other, example.Actor("user-a", False), None):
            with self.subTest(actor=actor):
                with self.assertRaisesRegex(PermissionError, "Task access denied"):
                    example.complete_task(actor, self.task)
                self.assertEqual(self.task, example.Task("task-1", "user-a", "open"))

    def test_invalid_state_rejected_for_owner(self):
        with self.assertRaisesRegex(ValueError, "Invalid task state"):
            example.complete_task(self.owner, example.Task("task-1", "user-a", "invalid"))

    def test_completed_task_remains_completed(self):
        task = example.Task("task-1", "user-a", "completed")
        self.assertEqual(example.complete_task(self.owner, task), task)


class QueryTests(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.addCleanup(self.connection.close)
        self.connection.execute("CREATE TABLE tasks (id TEXT PRIMARY KEY, owner_id TEXT, title TEXT)")
        self.connection.executemany("INSERT INTO tasks VALUES (?, ?, ?)", [
            ("task-a", "user-a", "Ada'nın görüşmesi"),
            ("task-b", "user-b", "Ada'nın görüşmesi"),
            ("task-c", "user-a", "İzleme"),
        ])
        self.actor = example.Actor("user-a", True)

    def test_apostrophe_is_data_and_owner_scope_is_preserved(self):
        self.assertEqual(example.find_own_tasks(self.connection, self.actor, "Ada'nın görüşmesi"),
                         [("task-a", "Ada'nın görüşmesi")])

    def test_query_shaped_text_does_not_expand_results(self):
        self.assertEqual(example.find_own_tasks(self.connection, self.actor, "' OR 1=1 --"), [])
        self.assertEqual(self.connection.execute("SELECT COUNT(*) FROM tasks").fetchone(), (3,))

    def test_anonymous_and_inactive_are_rejected(self):
        for actor in (None, example.Actor("user-a", False)):
            with self.subTest(actor=actor):
                with self.assertRaises(PermissionError):
                    example.find_own_tasks(self.connection, actor, "Ada'nın görüşmesi")

    def test_second_user_only_receives_own_row(self):
        self.assertEqual(example.find_own_tasks(self.connection, example.Actor("user-b", True),
                                              "Ada'nın görüşmesi"),
                         [("task-b", "Ada'nın görüşmesi")])


class OutputTests(unittest.TestCase):
    def test_markup_is_encoded_as_text(self):
        self.assertEqual(example.render_note_text('<b>Merhaba</b> & "not"'),
                         '<p>&lt;b&gt;Merhaba&lt;/b&gt; &amp; &quot;not&quot;</p>')

    def test_unicode_is_preserved(self):
        self.assertEqual(example.render_note_text("İğdır görüşmesi"), "<p>İğdır görüşmesi</p>")


if __name__ == "__main__":
    unittest.main()
