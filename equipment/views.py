from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Equipment


# View for list of posts on home page


class EquipmentList(generic.ListView):
    model = Equipment
    queryset = Equipment.objects.filter(status=1).order_by("-created_on")
    template_name = "equipment.html"
    paginate_by = 6


# View for full post in detail


class EquipmentDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Equipment.objects.filter(status=1)
        equipment = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "equipment_detail.html",
            {"equipment": equipment},
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Equipment.objects.filter(status=1)
        equipment = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "equipment_detail.html",
            {"equipment": equipment},
        )
