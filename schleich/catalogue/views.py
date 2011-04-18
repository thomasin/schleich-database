from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from schleich.catalogue.models import Species, Animal, Relationship, Other, Story
from django.db.models import Avg, Max, Min

def story(request, story):
    animals = Animal.objects.all()    
    try:
        story = Story.objects.get(slug = story)
    except Story.DoesNotExist:
        raise Http404
    return render_to_response('story.html', {'story': story, 'animals': animals})

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
    ai = Animal.objects.filter(age = "Infant")
    ae = Animal.objects.filter(age = "Elderly")
    gfy = Animal.objects.filter(age = "Youth", gender = "F")
    gfa = Animal.objects.filter(age = "Adult", gender = "F")
    gmy = Animal.objects.filter(age = "Youth", gender = "M")
    gma = Animal.objects.filter(age = "Adult", gender = "M")
    wstat = Animal.objects.aggregate(average_weight=Avg('weight'), min_weight=Min('weight'), max_weight=Max('weight'))    
    hstat = Animal.objects.aggregate(average_height=Avg('height'), min_height=Min('height'), max_height=Max('height'))
    return render_to_response('stats.html', {'wmax': wstat["max_weight"], 'wmin': wstat["min_weight"], 'wavg': wstat["average_weight"],'hmax': hstat["max_height"], 'havg': hstat["average_height"], 'hmin': hstat["min_height"], 'gfa': gfa, 'gma': gma, 'gmy': gmy, 'gfy': gfy, 'nsp': nsp, 'gf': gf, 'gm': gm, 'ai': ai, 'ae': ae, 'aa': aa, 'ay': ay, 'animals': animals, 'continent_count': continent_count, 'status_count': status_count}) 





