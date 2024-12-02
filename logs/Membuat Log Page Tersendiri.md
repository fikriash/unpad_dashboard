3. Buat Halaman Khusus untuk Melihat Log
Jika Anda ingin pengguna tertentu (misalnya, admin non-teknis) bisa melihat log tanpa harus masuk ke admin Django, Anda dapat membuat halaman khusus untuk menampilkan log.

Langkah-Langkah:

## ---
Tambahkan view baru di logs/views.py:

from django.shortcuts import render
from .models import UserActivityLog

def log_list(request):
    logs = UserActivityLog.objects.all().order_by('-timestamp')
    return render(request, 'logs/log_list.html', {'logs': logs})
## ---

Tambahkan URL di logs/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('logs/', views.log_list, name='log_list'),
]

## ---
Buat template logs/log_list.html:

<!DOCTYPE html>
<html>
<head>
    <title>Log Aktivitas Pengguna</title>
</head>
<body>
    <h1>Log Aktivitas Pengguna</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Pengguna</th>
                <th>Aktivitas</th>
                <th>Waktu</th>
                <th>Alamat IP</th>
            </tr>
        </thead>
        <tbody>
            {% for log in logs %}
            <tr>
                <td>{{ log.user }}</td>
                <td>{{ log.activity }}</td>
                <td>{{ log.timestamp }}</td>
                <td>{{ log.ip_address }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

## ---
Akses halaman log:

http://127.0.0.1:8000/logs/