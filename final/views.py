from django.shortcuts import render

def recommended(request):
	return render(request, 'recommended/recommended.html')

