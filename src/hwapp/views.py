from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def hw17(request):
    word_1 = request.POST.get('word_1')
    word_2 = request.POST.get('word_2')
    word_3 = request.POST.get('word_3')
    if len(word_1) > len(word_2) and len(word_1) > len(word_3):
        return HttpResponse(word_1)
    elif len(word_2) > len(word_1) and len(word_2) > len(word_3):
        return HttpResponse(word_2)
    elif len(word_3) > len(word_1) and len(word_3) > len(word_2):
        return HttpResponse(word_3)


def hw17_2(request):
    date = request.POST.get('date')

    if date == 01.01:
        return HttpResponse('С новым '.format(date))
    else:
        return HttpResponse(date)

