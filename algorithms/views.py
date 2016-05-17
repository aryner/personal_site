from django.shortcuts import render

def euclid(request):
  return render(request, 'algorithms/euclid.html',None)

