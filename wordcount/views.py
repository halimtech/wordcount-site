import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

        sortedword = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'words': len(wordlist),
                                          'worddif': sortedword})


def about(request):
    return render(request, 'about.html')

