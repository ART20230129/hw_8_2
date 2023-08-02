from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    CONTENT = []
    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        reader = list(csv.reader(file))

    for row in reader:
        if row[0] != 'ID':
            element = {'Name': row[1], "Street": row[4], "District": row[6]}
            CONTENT.append(element)

    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT,7)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        # 'page': page,
    }
    return render(request, 'stations/index.html', context)
