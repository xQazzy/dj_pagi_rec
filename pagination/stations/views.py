import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    csv_file_path = settings.BUS_STATION_CSV

    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        bus_stations_list = list(reader)

    paginator = Paginator(bus_stations_list, 10)

    page = request.GET.get('page', 1)

    try:
        bus_stations_page = paginator.page(page)
    except PageNotAnInteger:
        bus_stations_page = paginator.page(1)
    except EmptyPage:
        bus_stations_page = paginator.page(paginator.num_pages)

    context = {
        'bus_stations': bus_stations_page,
        'page': bus_stations_page,
    }
    return render(request, 'stations/index.html', context)
