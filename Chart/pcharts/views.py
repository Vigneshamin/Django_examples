from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club

# Create your views here.
class ClubChartView():
    template_name = "pcharts/chart.html"

    def get_context_date(selfself, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Club.objects.all()
        return context