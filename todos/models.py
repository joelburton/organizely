from django.db import models
from django.urls import reverse


class TaskList(models.Model):
    """Collection of tasks."""

    title = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.title

    def undone_count(self):
        """Count of undone tasks."""

        return self.task_set.filter(done=False).count()

    def get_absolute_url(self):
        """Return URL of task list."""

        return reverse('tasklist-detail', kwargs={'pk': self.pk})


class Task(models.Model):
    """Task."""

    task_list = models.ForeignKey(
        TaskList
    )

    title = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    info_url = models.URLField(
        blank=True,
        verbose_name="info URL",
    )

    done = models.BooleanField(
        help_text="Is task complete?",
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return URL of task list."""

        return reverse('task-detail', kwargs={'pk': self.pk})
