from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic

from todos.models import Task, TaskList


##############################################################################
# Views for listing and seeing details of task lists and tasks.
#
# These demonstrate the "generic views" system, which lets use build views
# for common tasks quickly.


class TaskListListView(generic.ListView):
    """List of task lists."""

    model = TaskList
    template_name = "todos/tasklist_list.html"
    paginate_by = 10


class TaskListDetailView(generic.DetailView):
    """Detail view of a task list."""

    model = TaskList
    template_name = "todos/tasklist_detail.html"


class TaskListView(generic.ListView):
    """List of tasks."""

    model = Task
    template_name = "todos/task_list.html"
    paginate_by = 10


class TaskDetailView(generic.DetailView):
    """Detail view of a task."""

    model = Task
    template_name = "todos/task_detail.html"


##############################################################################
# Views for creating and editing a task.
#
# These demonstrate even more powerful "generic views". They also show how
# you can use the permission system -- only users that have the
# "Can add tasks" permission can run these views -- otherwise, they're
# taken to the login form.


class TaskCreateView(PermissionRequiredMixin, generic.CreateView):
    """Create a new task."""

    model = Task
    fields = "__all__"
    template_name = "todos/task_form.html"
    permission_required = "todos.add_task"

    def get_initial(self):
        """Have the default list for this task be the one in the URL."""

        return {"task_list": self.kwargs['pk']}


class TaskUpdateView(PermissionRequiredMixin, generic.UpdateView):
    """Update existing task."""

    model = Task
    fields = "__all__"
    template_name = "todos/task_form.html"
    permission_required = "todos.change_task"
