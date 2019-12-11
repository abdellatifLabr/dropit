from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.http import JsonResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import File

@csrf_exempt
def drop(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        file_hash = get_random_string(length=32)
        _file = File(_hash=file_hash, _file=myfile)
        _file.save()
        resp = {
            'url': request.build_absolute_uri(reverse('lift', args=(file_hash,)))
        }
        return JsonResponse(resp)

    return HttpResponse('hii, im drop')

def lift(request, file_hash):
    try:
        myfile = File.objects.get(_hash=file_hash)
        if myfile.is_expired():
            myfile.delete()
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        return JsonResponse({
            'error': 'File does not exist or expired'
        })

    return FileResponse(open(myfile._file.path, 'rb'))
