from django.shortcuts import render
from django.http import JsonResponse
import yt_dlp
import os


def home(request):
    return render(request, 'downloader/home.html')


def download_video(request):
    url = request.POST.get('url')

    # Use yt-dlp to download videos from various platforms
    try:
        ydl_opts = {
            'format': 'best',  # This can be adjusted based on user preference
            'outtmpl': './downloads/%(title)s.%(ext)s',  # Path where videos are saved
        }

        # Initialize yt-dlp and attempt to download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)

        # Return the download link
        download_link = f"/downloads/{os.path.basename(file_path)}"
        return JsonResponse({'download_link': download_link})

    except Exception as e:
        return JsonResponse({'error': 'Error downloading video: ' + str(e)})

