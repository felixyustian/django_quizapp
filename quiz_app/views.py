from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm  # Kita akan buat ini di langkah 5
from .models import CustomUser
import requests
import random
from datetime import datetime

# --- DATA KUIS (Sama seperti sebelumnya) ---
QUESTIONS_DB = [
    {
        "question": "Library Python mana yang paling populer untuk Machine Learning?",
        "options": ["Pandas", "Scikit-Learn", "Flask", "Django"],
        "answer": "Scikit-Learn"
    },
    {
        "question": "Apa kepanjangan dari NLP?",
        "options": ["Neuro Linguistic Programming", "Natural Language Processing", "New Learning Protocol", "Neural Language Pathway"],
        "answer": "Natural Language Processing"
    },
    {
        "question": "Fungsi OpenCV dalam Python terutama digunakan untuk?",
        "options": ["Visi Komputer (Computer Vision)", "Pengembangan Web", "Database", "Audio Processing"],
        "answer": "Visi Komputer (Computer Vision)"
    },
    {
        "question": "Algoritma Deep Learning sering menggunakan struktur yang disebut?",
        "options": ["Decision Tree", "Neural Networks", "Linear Regression", "K-Means"],
        "answer": "Neural Networks"
    }
]

# --- FUNGSI BANTUAN CUACA ---
def get_weather(city):
    api_key = "GANTI_DENGAN_API_KEY_ANDA"  # Masukkan API Key OpenWeatherMap
    if api_key == "GANTI_DENGAN_API_KEY_ANDA":
        return None
        
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {'q': city, 'appid': api_key, 'units': 'metric', 'cnt': 24}
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        forecast_list = []
        
        if data.get("cod") == "200":
            seen_dates = set()
            for item in data['list']:
                dt_txt = item['dt_txt']
                date_obj = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
                date_str = date_obj.strftime('%Y-%m-%d')
                
                if date_str not in seen_dates and len(forecast_list) < 3:
                    forecast_list.append({
                        'day': date_obj.strftime('%A'),
                        'date': date_str,
                        'temp_day': round(item['main']['temp'], 1),
                        'temp_night': round(item['main']['temp'] - 2, 1), # Simulasi
                        'desc': item['weather'][0]['description']
                    })
                    seen_dates.add(date_str)
            return forecast_list
        return None
    except:
        return None

# --- VIEWS ---

def home(request):
    weather_data = None
    city = None
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather(city)
    return render(request, 'quiz_app/index.html', {'weather': weather_data, 'city': city})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Langsung login setelah daftar
            messages.success(request, "Registrasi berhasil!")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'quiz_app/register.html', {'form': form})

@login_required
def quiz_view(request):
    if request.method == 'POST':
        user_answer = request.POST.get('answer')
        correct_answer = request.POST.get('correct_answer')
        
        if user_answer == correct_answer:
            request.user.score += 10
            request.user.save()
            messages.success(request, 'Jawaban Benar! +10 Poin')
        else:
            messages.error(request, f'Salah! Jawabannya: {correct_answer}')
        return redirect('quiz') # Refresh halaman untuk soal baru

    # Ambil soal acak
    question_data = random.choice(QUESTIONS_DB)
    options = question_data['options'].copy()
    random.shuffle(options)
    
    return render(request, 'quiz_app/quiz.html', {'q': question_data, 'options': options})

def leaderboard(request):
    # Top 10 High Score
    users = CustomUser.objects.order_by('-score')[:10]
    return render(request, 'quiz_app/leaderboard.html', {'users': users})