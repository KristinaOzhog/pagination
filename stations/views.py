import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def get_content():
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as f:
        adress_list = []
        read_f = csv.DictReader(f)
        for row in read_f:
            adress_list.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            })

    return adress_list


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    content = get_content()
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(content, 10)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
