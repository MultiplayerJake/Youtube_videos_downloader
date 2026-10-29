# YouTube Videos Downloader

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/backend-yt--dlp-red.svg)](https://github.com/yt-dlp/yt-dlp)

A simple, robust, and interactive Python utility for downloading videos from YouTube, Twitch, Instagram, and over 1,000 other supported platforms with zero configuration required for `ffmpeg`.

---

## ✨ Features

- **Universal Support**: Powered by `yt-dlp`, supporting YouTube videos/shorts/playlists, Twitch VODs and live streams, Instagram reels, and 1,000+ websites.
- **Zero-Hassle Ffmpeg**: Automatically detects and integrates `ffmpeg` via `imageio_ffmpeg`. No manual system PATH configuration or external binary downloads required!
- **Direct to Downloads**: Automatically saves your downloaded videos directly into your operating system's default `Downloads` folder.
- **High Quality `.mp4` Output**: Automatically merges and converts streams into high-quality `.mp4` format.
- **Interactive CLI**: Clean, simple interactive prompt—just paste your link and let the script handle the rest.

---

# Video showcase:


https://github.com/user-attachments/assets/a61799b0-a368-4ba7-aecb-69688fa5a058


## 📋 Prerequisites

- **Python 3.8 or higher** installed on your system.
- **pip** (Python package manager).

---

## 🚀 Installation

1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/MultiplayerJake/Youtube_videos_downloader.git
   cd Youtube_videos_downloader
   ```

2. **Install the required dependencies**:
   ```bash
   pip install yt-dlp imageio-ffmpeg
   ```

---

## 💻 Usage

1. Run the Python script from your terminal:
   ```bash
   python YoutubeDownload.py
   ```

2. When prompted by the interactive CLI, paste the URL of the video (YouTube, Twitch, Instagram, etc.) and press **Enter**.

3. The script will fetch video information, process the download using bundled `ffmpeg`, and save the `.mp4` file directly to your system `Downloads` folder.

---

## ⚙️ How It Works

- **`yt-dlp`**: Provides state-of-the-art downloading capabilities, robust extraction, and frequent updates against upstream site changes.
- **`imageio_ffmpeg`**: Programmatically provides a verified static build of `ffmpeg`, allowing the script to perform video merging and format conversion seamlessly across Windows, macOS, and Linux without requiring manual binary installation.

---

I have an executable file that you can use on any Windows computer. If you want it, contact me.
