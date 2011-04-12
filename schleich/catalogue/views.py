from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from schleich.catalogue.models import Species, Animal, Relationship, Other

def name(request, name):
    try:
        animal = Animal.objects.get(slug = name)
    except Animal.DoesNotExist:
        raise Http404
    first_rs = list(Relationship.objects.filter(first_animal = animal))
    second_rs = list(Relationship.objects.filter(second_animal = animal))
    return render_to_response('name.html', {'animal': animal, 'first_rs': first_rs, 'second_rs': second_rs})

def home(request):
    animals = Animal.objects.all()
    return render_to_response('home.html', {'animals': animals})

def lists(request):
    animals = Animal.objects.all()
    return render_to_response('lists.html', {'animals': animals})

def gallery(request):
    animals = Animal.objects.all()
    table = []
    row = []
    for a in animals:
        if a.image:
            if len(row) < 3:
                row.append(a)
            else:
                table.append(row)
                row = [a]
    table.append(row)
    return render_to_response('gallery.html', {'table': table})

def statistics(request):
    animals = Animal.objects.all()
    nsp = len(set([a.species for a in animals]))
    continents = [a.species.global_home for a in animals]
    continent_count = {}
    for continent in continents:
        continent_count[continent] = continent_count.setdefault(continent, 0) + 1 
    status = [a.species.status for a in animals]
    status_count = {}
    for s in status:
        status_count[s] = status_count.setdefault(s, 0) + 1 
    gf = Animal.objects.filter(gender = "F")
    gm = Animal.objects.filter(gender = "M")
    aa = Animal.objects.filter(age = "Adult")
    ay = Animal.objects.filter(age = "Youth")
    gfy = Animal.objects.filter(age = "Youth", gender = "F")
    gfa = Animal.objects.filter(age = "Adult", gender = "F")
    gmy = Animal.objects.filter(age = "Youth", gender = "M")
    gma = Animal.objects.filter(age = "Adult", gender = "M")
    return render_to_response('stats.html', {'gfa': gfa, 'gma': gma, 'gmy': gmy, 'gfy': gfy, 'nsp': nsp, 'gf': gf, 'gm': gm, 'aa': aa, 'ay': ay, 'animals': animals, 'continent_count': continent_count, 'status_count': status_count})





