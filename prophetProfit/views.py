from django.shortcuts import render

def profit(request):
    return render(request, 'prophetProfit/pyprofits.html')

def thegoods(request):
    return render(request, 'prophetProfit/thegoods.html')

