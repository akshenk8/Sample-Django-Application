from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import TeamMember
from .forms import TeamMemberForm


class TeamMemberListView(LoginRequiredMixin, ListView):
    template_name = 'TeamApplication/TeamMember/list.html'
    model = TeamMember
    context_object_name = 'members'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TeamMemberAddView(LoginRequiredMixin, CreateView):
    template_name = 'TeamApplication/TeamMember/form.html'
    model = TeamMember
    form_class = TeamMemberForm
    success_url = reverse_lazy('team:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TeamMemberAddView, self).form_valid(form)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        kwargs['update_only'] = False
        context = super(TeamMemberAddView, self).get_context_data(**kwargs)
        return context


class TeamMemberUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'TeamApplication/TeamMember/form.html'
    model = TeamMember
    form_class = TeamMemberForm
    success_url = reverse_lazy('team:index')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        kwargs['update_only'] = True
        context = super(TeamMemberUpdateView, self).get_context_data(**kwargs)
        return context


class TeamMemberDeleteView(LoginRequiredMixin, DeleteView):
    model = TeamMember
    form_class = TeamMemberForm
    success_url = reverse_lazy('team:index')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
