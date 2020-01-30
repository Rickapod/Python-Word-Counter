
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  return render(request, 'home.html')

def count(request):
  fulltext = request.GET['fulltext']
  
  wordcount = fulltext.split()

  words = {}

  for word in wordcount:
    if word in words:
      #increase count
      words[word] += 1
    else:
      #add to the dictionare
      words[word] = 1
  mostword = ''
  mostwordcount = 0
  for word in words:
    if words[word] > mostwordcount:
      mostwordcount = words[word]
      mostword = word
  return render(request, 'count.html', {'fulltext': fulltext, 'wordcount': len(wordcount), 'mostword': mostword })