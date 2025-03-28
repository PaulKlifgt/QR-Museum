from django.shortcuts import render
from django.http import JsonResponse

from . import models

# Create your views here.
def get_exhibit_by_id(request, id: int):
    
    exhibit = models.Exhibit.objects.filter(id=id)

    if exhibit:
        exhibit = exhibit[0]
        data = {'name': exhibit.name, 
                'description': exhibit.description, 
                'average_rank': exhibit.average_rank, 
                'count_rank': exhibit.count_rank, 
                'section': exhibit.section.name}
    else:
        data = {'error': "don't find"}

    return JsonResponse(data)


def get_section_by_id(request, id: int):

    section = models.Section.objects.filter(id=id)

    if section:
        section = section[0]
        data = {'name': section.name, 
                'description': section.description, 
                'average_rank': section.average_rank, 
                'count_rank': section.count_rank, 
                'type_game': section.type_game}
        
    else:
        data = {'error': "don't find"}

    return JsonResponse(data)


def select_exh_by_sec(section_id: int):

    section = models.Section.objects.filter(id=section_id)
    
    if section:
        exhibits = models.Exhibit.objects.filter(section=section[0])
        
        if exhibits:
            data = {'exhibits': list([x.toJSON() for x in exhibits])}
        else:
            data = {'error': "don't find"}
    else:
        data = {'error': "don't find"}

    return data



def get_exhibit_by_section(request, section_id: int): 
    return JsonResponse(select_exh_by_sec(section_id))


def get_all_sections(request):

    data = {}

    section = models.Section.objects.all()

    if section:
        for sec in section:
            data[sec.name] = select_exh_by_sec(sec.id)

    return JsonResponse(data)


def index(request):
    context = {}
    template_name = 'index.html'
    return render(request=request, template_name=template_name, context=context)