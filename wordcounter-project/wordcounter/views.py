
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

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
  

  sortedwords = sorted(words.items(), key=operator.itemgetter(1), reverse = True)
  mostword = sortedwords[0][0]
  mostwordcount = sortedwords[0][1]

  # for word in words:
  #   if words[word] > mostwordcount:
  #     mostwordcount = words[word]
  #     mostword = word
  return render(request, 'count.html', {'fulltext': fulltext, 'wordcount': len(wordcount), 'mostword': mostword, 'mostwordcount': mostwordcount, 'sortedwords': sortedwords })