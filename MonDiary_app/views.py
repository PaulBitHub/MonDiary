from django.shortcuts import render

def index(request):
    context = {'title': '"Money Diary" — приложение для ведения финансов для прозрачного управления ими.'}
    return render(request, 'MonDiary_app/index.html', context)
