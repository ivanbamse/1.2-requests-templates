from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv

from pprint import pprint

def index(request):
    return redirect(reverse('bus_stations'))


def get_bus_stations_info():
    with open(BUS_STATION_CSV, 'r', encoding='utf-8') as info_file:
        stations = csv.DictReader(info_file)
        result = list(stations)
    return result

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    bus_stations = get_bus_stations_info()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': bus_stations,
        'page': page
    }
    return render(request, 'stations/index.html', context)
