from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
import pandas as pd
from io import BytesIO
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def powerbi_faculty_view(request):
    return render(request, 'dashboards/powerbi_dashboard.html', {
        'title': 'Dashboard Fakultas dan Prodi',
        'embed_url': 'https://app.powerbi.com/view?r=eyJrIjoiNGRmOWVhODgtNjNjNi00NzA5LWE3NjYtZTE1ZTU0N2QzYmMyIiwidCI6ImVjOWFlNGY3LTI1MDQtNDYxYy1iMDZkLTE0ZWI3ODQ2OTFjMiIsImMiOjEwfQ%3D%3D'
    })

@login_required
def powerbi_iku_view(request):
    return render(request, 'dashboards/powerbi_dashboard.html', {
        'title': 'Dashboard IKU',
        'embed_url': 'https://app.powerbi.com/view?r=eyJrIjoiYTU2MTdmNWUtYTI4ZC00NDdiLWEwYzgtNzVmZjRjMDJlMzI4IiwidCI6ImVjOWFlNGY3LTI1MDQtNDYxYy1iMDZkLTE0ZWI3ODQ2OTFjMiIsImMiOjEwfQ%3D%3D'
    })

@login_required
def powerbi_uad_view(request):
    return render(request, 'dashboards/powerbi_dashboard.html', {
        'title': 'Dashboard Unpad Dalam Angka',
        'embed_url': 'https://app.powerbi.com/view?r=eyJrIjoiNjA3NjQ1NjAtMTYwOC00Mzk2LThjZjgtOTQ5M2YyMWMzOWEwIiwidCI6ImVjOWFlNGY3LTI1MDQtNDYxYy1iMDZkLTE0ZWI3ODQ2OTFjMiIsImMiOjEwfQ%3D%3D'
    })

# Fungsi untuk menampilkan data
@login_required
def redash_data_view(request):
    # Redash API endpoint
    query_id = 145  # Ganti dengan Query ID Anda
    redash_base_url = 'https://dahan.unpad.ac.id/api/queries/'
    api_key = 'sCwfGxkHRLSXFkkZHRS14zituO345nXdQ72dlkId'  # Ganti dengan API Key Anda
    url = f'{redash_base_url}{query_id}/results.json?api_key={api_key}'

    try:
        # Ambil data dari Redash API
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Ekstrak kolom dan baris dari JSON
        columns = [col['name'] for col in data['query_result']['data']['columns']]
        rows = data['query_result']['data']['rows']

        # Kirimkan data ke template
        return render(request, 'dashboards/raw_data.html', {'columns': columns, 'rows': rows})

    except requests.exceptions.RequestException as e:
        # Jika terjadi error, kembalikan JSON error
        return JsonResponse({'error': str(e)}, status=500)


@login_required    
def redash_download_excel(request):
    # Redash API endpoint
    query_id = 145  # Ganti dengan Query ID Anda
    redash_base_url = 'https://dahan.unpad.ac.id/api/queries/'
    api_key = 'sCwfGxkHRLSXFkkZHRS14zituO345nXdQ72dlkId'  # Ganti dengan API Key Anda
    url = f'{redash_base_url}{query_id}/results.json?api_key={api_key}' 

    # Ambil data dari Redash
    try:
        response = requests.get(url)
        response.raise_for_status()  # Cek jika ada error pada permintaan
        data = response.json()

        # Ekstrak kolom dan baris dari Redash JSON
        columns = [col['name'] for col in data['query_result']['data']['columns']]
        rows = data['query_result']['data']['rows']

        # Konversi ke DataFrame
        df = pd.DataFrame(rows, columns=columns)

        # Simpan ke Excel
        output = BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')

        # Kembalikan file Excel sebagai response
        output.seek(0)
        response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="redash_data.xlsx"'
        return response

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)


@login_required
def redash_embed_view(request):
    embed_url = "https://dahan.unpad.ac.id/embed/query/145/visualization/189?api_key=qwJpKqtNh7f3NCEgykgE5T8YcDnNlSl968YTLuYU&"
    return render(request, 'dashboards/redash_embed.html', {
        'title': 'Raw Data View',
        'embed_url': embed_url
    })

