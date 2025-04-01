import copy, os.path, shutil

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, FileResponse
from django.contrib.auth.decorators import login_required

from . import models, forms
from base import settings

# Create your views here.
def get_exhibit_by_id(request, id: int):
    
    exhibit = models.Exhibit.objects.filter(id=id)

    if exhibit:
        exhibit = exhibit[0]
        data = {'name': exhibit.name, 
                'description': exhibit.description, 
                'average_rank': exhibit.average_rank, 
                'count_rank': exhibit.count_rank, 
                'section': exhibit.section.name,
                'type_game': exhibit.type_game}
    else:
        data = {'error': "don't find"}

    return JsonResponse(data)


def get_section_by_id(request, id: int):

    section = models.Section.objects.filter(id=id)

    if section:
        section = section[0]
        data = {'name': section.name, 
                'description': section.description,
                }
    else:
        data = {'error': "don't find"}

    return JsonResponse(data)


#не нужен пока что
def select_exh_by_sec(section_id: int):

    section = models.Section.objects.filter(id=section_id)
    data = {}
    if section:
        exhibits = models.Exhibit.objects.filter(section=section[0])
        
        if exhibits:
            for e in exhibits:
                data[e.name] = e.toJSON()
        else:
            data = {'error': "don't find"}
    else:
        data = {'error': "don't find"}

    return data

def get_exhibit_by_section(request, section_id: int): 
    return JsonResponse(select_exh_by_sec(section_id))


def get_all_sections(request):

    data = {}

    sections = models.Section.objects.all()

    if sections:
        for sec in sections:
            data[sec.name] = select_exh_by_sec(sec.id)

    return JsonResponse(data)


def index(request):
    context = {}
    template_name = 'index.html'

    context['sections'] = {}

    sections = models.Section.objects.all()

    for sec in sections:
        exhibits_section = models.Exhibit.objects.filter(section=sec)
        context['sections'][sec] = list(exhibits_section) 

    return render(request=request, template_name=template_name, context=context)


def get_image_for_exh(id: int):
    for f in settings.ALLOWED_UPLOAD_IMAGES:
        filename = str(id)+f
        filepath = settings.MEDIA_ROOT+'/imgs/'+filename
        if os.path.exists(filepath):
            return filepath
    else:
        return False


@login_required
def edit(request, type:str, id:int):
    context = {}
    template_name = 'edit.html'

    if type == 'sec':
        section = models.Section.objects.filter(id=id)
        if section:
            section = section[0]
            context['section'] = section
            if request.method == 'POST':
                old_sec = copy.deepcopy(section)
                form = forms.EditSectionForm(request.POST, instance=section)
                if form.is_valid():
                    sec = form.save(commit=False)                
                    sec.save()
                    return redirect(f'/api/index/')
            else:
                default_values = {
                    'name': section.name,
                    'description': section.description
                }
                form = forms.EditSectionForm(initial=default_values)
                context['form'] = form

    elif type == 'exh':
        exhibit = models.Exhibit.objects.filter(id=id)
        if exhibit:
            exhibit = exhibit[0]
            context['exhibit'] = exhibit
            if request.method == 'POST':
                old_exh = copy.deepcopy(exhibit)
                
                form = forms.EditExhibitForm(request.POST, request.FILES, instance=exhibit)
                if form.is_valid():
                    exh = form.save(commit=False)

                    try:
                        old_img_path = get_image_for_exh(old_exh.id)
                        if old_img_path:
                            os.remove(old_img_path)
                        request.FILES['image'].name = str(old_exh.id) + '.' + request.FILES['image'].name.split(".")[-1]
                        exh.image = request.FILES['image']
                    except Exception:
                        pass

                    exh.average_rank = old_exh.average_rank
                    exh.count_rank = old_exh.count_rank
                
                    exh.save()
                    return redirect(f'/api/index/')
            else:
                default_values = {
                    'name': exhibit.name,
                    'description': exhibit.description,
                    'section': exhibit.section,
                    'type_game': exhibit.type_game,
                    'image': exhibit.image
                }
                form = forms.EditExhibitForm(initial=default_values)
                context['form'] = form
    
    return render(request, template_name=template_name, context=context)


@login_required
def create(request, type:str):
    context = {}
    template_name = 'create.html'

    if type == 'sec':
        if request.method == 'POST':
            
            form = forms.CreateSectionForm(request.POST)
            if form.is_valid():
                sec = form.save(commit=False)
            
            sec.save()
            return redirect(f'/api/index/')
        else:
            form = forms.CreateSectionForm()
            context['form'] = form
            context['section'] = 'section'

    elif type == 'exh':
        if request.method == 'POST':
            form = forms.CreateExhibitForm(request.POST, request.FILES)
            if form.is_valid():
                print(request.FILES)
                exh = form.save(commit=False)
                last_exh = models.Exhibit.objects.last()
                try:
                    if last_exh:
                        request.FILES['image'].name = str(last_exh.id) + '.' + request.FILES['image'].name.split(".")[-1]
                    else:
                        request.FILES['image'].name = '1' + '.' + request.FILES['image'].name.split(".")[-1]
                    exh.image = request.FILES['image']
                except Exception:
                    pass
                exh.average_rank = 0.0
                exh.count_rank = 0
            
                exh.save()
                return redirect('/api/index/')
        else:
            form = forms.CreateExhibitForm()
            context['form'] = form
            context['exhibit'] = 'exhibit'
    
    return render(request, template_name=template_name, context=context)


@login_required
def delete(request, type:str, id:int):

    if type == 'sec':
        section = models.Section.objects.filter(id=id)
        section.delete()

    elif type == 'exh':
        exhibit = models.Exhibit.objects.filter(id=id)
        exhibit.delete()
        filepath = get_image_for_exh(id)
        if filepath:
            os.remove(filepath)

    return redirect('index')


def rank(request, id:int, rank:int):  
    exhibit = models.Exhibit.objects.filter(id=id)
    if exhibit:
        exhibit = exhibit[0]
        exhibit.average_rank = (exhibit.average_rank*exhibit.count_rank+rank)/(exhibit.count_rank+1)
        exhibit.count_rank += 1
        exhibit.save(update_fields=['average_rank', 'count_rank'])
        return HttpResponse({})
    else:
        return HttpResponse({})


def get_image(request, id):
    filepath = get_image_for_exh(id)
    return FileResponse(open(filepath, 'rb'), as_attachment=False)


def backup(request, key:str):
    if key == 'ERwc5sir6PM1r2Zcj7F5GbccYVvXPh':
        return FileResponse(open(settings.BASE_DIR / 'db.sqlite3', 'rb'), as_attachment=True)
    return redirect('/')


def backup_images(request, key:str):
    if key == 'ERwc5sir6PM1r2Zcj7F5GbccYVvXPh':
        filepath = shutil.make_archive('imgs', 'zip', settings.MEDIA_ROOT+'/imgs/')
        return FileResponse(open(filepath, 'rb'), as_attachment=True)
    return redirect('/')