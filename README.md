# YouTube Downloader

A simple Python script that downloads a YouTube video as **MP4** (video) or **MP3** (audio only). You choose which one.

## Setup

1. Install [Python](https://www.python.org/downloads/) (3.9 or newer).
2. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. **For MP3 (and best-quality MP4)** you also need [ffmpeg](https://ffmpeg.org/download.html).
   On Windows the easiest way is:

   ```bash
   winget install ffmpeg
   ```

## Usage

```bash
python main.py
```

Then paste a YouTube link and pick:

- `1` for MP4 (video)
- `2` for MP3 (audio only)

Files are saved in the `downloads` folder.

## Built with

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)

## Note

Only download videos you have the right to download.
