from django.shortcuts import render

from tagging.models import TaggedItem, Tag
def edittags(request):
    context = {}
    
    tags =  [tag.name for tag in Tag.objects.all()]
    context['tags'] = tags
    
    return render(request, 'edittags/edittags.html', context)