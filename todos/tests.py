from django.test import TestCase

from todos.models import TaskList


class TaskListTestCase(TestCase):
    def test_make_task_list(self):
        tl = TaskList.objects.create(title="TL")
        self.assertEqual(TaskList.objects.first().title, "TL")
        self.assertEqual(tl.undone_count(), 0)