from django.shortcuts import render
from . models import Art, ReporterForm, ArtForm, CATEGORY_CHOICES, Reporter
# Create your views here.

def index(request):
    context = {}
    arts = Art.objects.all().order_by("-id")
    for art in arts :
        art.cat_str = getModelChoice(art.category, CATEGORY_CHOICES)

    context["arts"] = arts
    return render(request, "index.html", context)


def details(request, id):
    context = {}
    arts = Art.objects.filter(id=id)
    
    for art in arts:
        context["art"] = art
    
    return render(request, "details.html", context)  

def about(request,slug):
    context = {}
    reporter = Reporter.objects.filter(first_name=slug)
    for i in reporter:
        i.counter = Art.objects.filter(reporter=i).count()
        context["rd"] = i
    return render(request, "about.html", context)

def reporter(request):
    context = {}
    reporter = Reporter.objects.all().order_by("id")
    for i in reporter:
        i.counter = Art.objects.filter(reporter=i).count()
    context["reporter"] = reporter
    return render(request, "reporter.html", context)

def reporterregis(request):
    context = {}
    if request.method == "POST":
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
        else :
            print('Erro')
        
    context['form'] = ReporterForm()
    return render(request, 'regis_reporter.html', context)

def articelregis(request):
    context = {}
    if request.method == "POST":
        form = ArtForm(request.POST)
        if form.is_valid():
            form.save()
        else :
            print('Erro')
        
    context['form'] = ArtForm()
    return render(request, 'regis_art.html', context)


def getModelChoice(num, choices):
    for choice in choices:
        if choice[0] == num:
            return choice[1]