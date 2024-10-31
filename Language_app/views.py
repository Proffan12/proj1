import json
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Путь для хранения JSON файлов
ALBUMS_FOLDER = os.path.join(settings.BASE_DIR, 'albums')

# Убедимся, что папка для JSON файлов существует
if not os.path.exists(ALBUMS_FOLDER):
    os.makedirs(ALBUMS_FOLDER)

def index(request):
    return render(request, 'Language_app/form.html')

def save_album(request):
    if request.method == "POST":
        album_data = {
            "title": request.POST.get("title"),
            "artist": request.POST.get("artist"),
            "year": request.POST.get("year"),
            "genre": request.POST.get("genre")
        }

        # Сохранение данных в JSON файл
        album_filename = f"{album_data['title']}_{album_data['artist']}.json"
        album_filepath = os.path.join(ALBUMS_FOLDER, album_filename)
        
        with open(album_filepath, 'w', encoding='utf-8') as json_file:
            json.dump(album_data, json_file, ensure_ascii=False, indent=4)

        return redirect('index')
    return render(request, 'Language_app/form.html')

def load_albums(request):
    # Загрузка всех файлов JSON из папки
    albums = []
    for filename in os.listdir(ALBUMS_FOLDER):
        if filename.endswith('.json'):
            filepath = os.path.join(ALBUMS_FOLDER, filename)
            with open(filepath, 'r', encoding='utf-8') as json_file:
                album_data = json.load(json_file)
                albums.append(album_data)
    
    return render(request, 'Language_app/album_list.html', {"albums": albums})

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        if uploaded_file.name.endswith('.json'):
            # Сохраняем загруженный файл
            file_path = os.path.join(ALBUMS_FOLDER, uploaded_file.name)
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return redirect('load_albums')
        else:
            return JsonResponse({"error": "Недопустимый формат файла. Пожалуйста, загрузите файл JSON."})
    return render(request, 'Language_app/upload_form.html')
