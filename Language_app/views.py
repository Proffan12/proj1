from django.shortcuts import render, redirect

def form_view(request):
    # Получаем язык и прогресс из cookies, устанавливаем значения по умолчанию
    language = request.COOKIES.get('language', 'English')
    progress = request.COOKIES.get('progress', 0)

    # Преобразуем прогресс в целое число
    progress = int(progress) if isinstance(progress, str) and progress.isdigit() else 0

    return render(request, 'Language_app/form.html', {'language': language, 'progress': progress})

def save_progress(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        progress = request.POST.get('progress')

        # Создаем редирект
        response = redirect('form_view')
        
        # Устанавливаем cookies
        response.set_cookie('language', language)
        response.set_cookie('progress', progress)
        
        return response

        #DIONBIODNBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBDIO
        



