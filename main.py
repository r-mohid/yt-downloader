"""
YouTube Downloader
Download a YouTube video as MP4 (video) or MP3 (audio only).
"""

import os
import shutil

from yt_dlp import YoutubeDL

DOWNLOAD_FOLDER = "downloads"


def download_mp4(url):
    options = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])


def download_mp3(url):
    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with YoutubeDL(options) as ydl:
        ydl.download([url])


def main():
    print("=== YouTube Downloader ===\n")

    url = input("Paste a YouTube link: ").strip()
    if not url:
        print("No link entered. Bye!")
        return

    print("\nWhat do you want?")
    print("  1) MP4 (video)")
    print("  2) MP3 (audio only)")
    choice = input("Enter 1 or 2: ").strip()

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    try:
        if choice == "1":
            download_mp4(url)
        elif choice == "2":
            if shutil.which("ffmpeg") is None:
                print("\nMP3 needs ffmpeg installed. See the README for how to install it.")
                return
            download_mp3(url)
        else:
            print("Please pick 1 or 2.")
            return
    except Exception as error:
        print(f"\nSomething went wrong: {error}")
        return

    print(f"\nDone! Check the '{DOWNLOAD_FOLDER}' folder.")


if __name__ == "__main__":
    main()
