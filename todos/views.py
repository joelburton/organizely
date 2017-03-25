from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic

from todos.models import Task, TaskList


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


class TaskCreateView(PermissionRequiredMixin, generic.CreateView):
    """Create a new task."""

    model = Task
    fields = "__all__"
    template_name = "todos/task_form.html"
    permission_required = "todos.add_task"

    def get_initial(self):
        return {"task_list": self.kwargs['pk']}


class TaskUpdateView(PermissionRequiredMixin, generic.UpdateView):
    """Update existing task."""

    model = Task
    fields = "__all__"
    template_name = "todos/task_form.html"
    permission_required = "todos.change_task"
