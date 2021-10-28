from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    stext = request.POST.get('text', 'default')

    removepunc = request.POST.get('remove', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newline = request.POST.get('newline', 'off')
    extraspace = request.POST.get('extraspace', 'off')
    charcount = request.POST.get('charcount', 'off')

    punctutations = '''/[-[\]{}()*+?.,\\^$|#\s]/g,!';@"\\$&"'''
    if removepunc == "on":
        analyzed = ""
        for char in stext:
            if char not in punctutations:
                analyzed = analyzed+char
        param = {'purpose': 'Removed Punctutations', 'analyze_text': analyzed}
        return render(request, 'analyze.html', param)

    elif uppercase == "on":
        analyzed = ""
        for char in stext:
            analyzed = analyzed+char.upper()
        param = {'purpose': 'Changed To UpperCase', 'analyze_text': analyzed}
        return render(request, 'analyze.html', param)

    elif newline == "on":
        analyzed = ""
        for char in stext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        param = {'purpose': 'New Line Remover', 'analyze_text': analyzed}
        return render(request, 'analyze.html', param)

    elif extraspace == "on":
        analyzed = ""
        for index, char in enumerate(stext):
            if not(stext[index] == " " and stext[index+1] == " "):
                analyzed = analyzed+char
        param = {'purpose': 'Space Remover', 'analyze_text': analyzed}
        return render(request, 'analyze.html', param)

    elif charcount == "on":
        val = 0
        for char in stext:
            val = val+1
        param = {'purpose': 'No of characters', 'analyze_text': val}
        return render(request, 'analyze.html', param)

    else:
        return render(request, 'error.html')
