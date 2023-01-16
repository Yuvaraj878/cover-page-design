from django.shortcuts import render

def coverpage(request):
     return render(request,"cover_app/coverpage.html")