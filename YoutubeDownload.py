import imageio_ffmpeg
import yt_dlp
import os

def get_ffmpeg_path():
    return imageio_ffmpeg.get_ffmpeg_exe()

url = input("Youtube URL> ")
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

ydl_opts = {
    "format": "bestvideo[vcodec^=avc1]+bestaudio[ext=m4a]/best[vcodec^=avc1]/best",
    "merge_output_format": "mp4",
    "outtmpl": os.path.join(downloads_folder, "%(title)s.%(ext)s"),
    "ffmpeg_location": get_ffmpeg_path(),
}

yt_dlp.YoutubeDL(ydl_opts).download([url])