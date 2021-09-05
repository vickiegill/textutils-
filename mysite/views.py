# i have created this file - dark coder
from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html', )


def analyze(request):

    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        analyzed = ""
        punc = '''!@#$%^&*()_-~.<>,?[]'''
        for char in djtext:
            if char not in punc:
                analyzed = analyzed + char

        params = {'purpose': 'Remove punchtion ', 'analyzer_text': analyzed}
        djtext = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'change to uppercase ', 'analyzer_text': analyzed}
        djtext = analyzed


    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'removed new line', 'analyzer_text' : analyzed }
        djtext = analyzed

    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'space remover', 'analyzer_text': analyzed}

    if( removepunc != 'on' and extraspaceremover != "on" and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Please select any operation and try again!")

    return render(request, 'analizer.html', params)

