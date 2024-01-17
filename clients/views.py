from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Clients


# View for list of posts on home page


class ClientsList(generic.ListView):
    model = Clients
    queryset = Clients.objects.filter(status=1).order_by("-created_on")
    template_name = "clients.html"
    paginate_by = 6

# View for full post in detail


class ClientsDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Clients.objects.filter(status=1)
        clients = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "clients_detail.html",
            {
                "clients": clients
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Equipment.objects.filter(status=1)
        equipment = get_object_or_404(queryset, slug=slug)


        return render(
            request,
            "clients_detail.html",
            {
                "clients": clients
            },
        )
