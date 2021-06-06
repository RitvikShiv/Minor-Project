from django.shortcuts import render

def showcovid(request):
    return render(request,'app/home.html')

def showIndia(request):
    return render(request,'app/india.html')

def showState(request):
    return render(request,'app/state.html')

def showVaccine(request):
    return render(request,'app/vaccine.html')





