from django.shortcuts import render
from explore.models import Wisdom
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST

n = 0
def my(request):
  wisdom = Wisdom.objects.all()[n]
  context = {
    'wisdom': wisdom
  }

  return render(request, 'my/my.html', context)

@require_GET
def wisdom_prev(request):
    global n
    n -= 1
    wisdom = Wisdom.objects.all()[n]
    return JsonResponse({'wisdom': wisdom.text, 'n': n})

@require_GET
def wisdom_next(request):
    global n
    n += 1
    wisdom = Wisdom.objects.all()[n]
    return JsonResponse({'wisdom': wisdom.text, 'n': n})