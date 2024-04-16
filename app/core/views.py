from django.http import JsonResponse
from django.views.generic.base import View
from django.shortcuts import render
from django.template.loader import render_to_string

from .forms import BusForm
from .models import Bus


class BusView(View):
    """
    View for list bus in inventory and
    add bus to inventory.
    """
    def get(self, request, *args, **kwargs):
        context = {}
        context["form"] = BusForm()
        context["bus_list"] = Bus.objects.filter(is_active=True).order_by("-id")
        return render(request, "bus.html", context=context)

    def post(self, request, *args, **kwargs):
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
        context = {}
        context["bus_list"] = Bus.objects.filter(is_active=True).order_by("-id")
        html = render_to_string("bus_list.html", request=request, context=context)
        data = {}
        data["status"] = True
        data["template"] = html
        return JsonResponse(data)

class BusDeleteView(View):
    """
    View for list bus in inventory and
    add bus to inventory.
    """
    def delete(self, request, *args, **kwargs):
        id = kwargs["id"]
        bus = Bus.objects.get(id=id)
        bus.delete()
        context = {}
        context["bus_list"] = Bus.objects.filter(is_active=True).order_by("-id")
        html = render_to_string("bus_list.html", request=request, context=context)
        data = {}
        data["status"] = True
        data["template"] = html
        return JsonResponse(data)
