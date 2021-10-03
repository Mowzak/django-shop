from django import forms
from app.models import checkout
from url_filter.filtersets import ModelFilterSet
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class checkfilter(ModelFilterSet):
    class Meta(object):
        model = checkout

class is_super(UserPassesTestMixin):
    login_url = 'home'
    def test_func(self):
        return self.request.user.is_superuser