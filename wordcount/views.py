from django.http import HttpResponse
from django.shortcuts import render  #
import operator

def home(request):
#    return render(request,'home.html',{'hi':'Great weather'}) #goes to home.html
    return render(request,'home.html') #goes to home.html

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext'].lower()
    wordlist = fulltext.split()
    word_dict = {}
    for word in wordlist:
        if word in word_dict:
            #Increase
            word_dict[word] += 1
        else:
            #Add to dictionary
            word_dict[word] = 1

    sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request,'count.html',{'fulltext':fulltext, 'count': len(wordlist), 'sortedwords': sorted_words}) #goes to count.html