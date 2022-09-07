from django.shortcuts import render
from django.http import HttpResponse
import datetime
import string


# Create your views here.
def index(request):
    return render(request, 'index.html')


# def removepunc(request):
#   s = request.GET.get("text")
#   s = s.translate(str.maketrans('', '', string.punctuation))
#   return HttpResponse(s)

# def capfirst(request):
#   return HttpResponse("Remove Punc")

# def newlineremove(request):
#   return HttpResponse("Remove Punc")

# def spaceremove(request):
#   return HttpResponse("Remove Punc")

# def charcount(request):
#   return HttpResponse("Remove Punc")


def analyze(request):

    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    spaceRemove = request.GET.get('spaceRemove', 'off')
    print(f"All Caps {djtext}")

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCSE', 'analyzed_text': analyzed}
        print(params)
        return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif spaceRemove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return render(request, '404.html')
