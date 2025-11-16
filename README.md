<!-- # Hello
## Introduction
This is a normal text. Hello everyone.
<!-- to start new para in markdown seperate two lines wit one extra line -->
This is to *tell* y**o**u ~~about~~ my experiene with typing<!--use two spaces to switch to new line without changing para-->  dsfsdfsdff -->
# Pytube Video Downloader

## Introduction
This project is a Python-based video downloader built using the `pytube-fix` library. It allows users to download video and audio streams from YouTube, merge them into a single file, and save the output locally. The project also uses `ffmpeg` for merging audio and video files.

---

## Features
- List available video and audio streams in a tabular format.
- Download video streams (WebM format).
- Download audio streams (MP4 or WebM format).
- Merge video and audio files using `ffmpeg`.
- Specify audio bitrate during merging.

---

## Requirements
- Python 3.7 or higher
- `pytube-fix` library
- `ffmpeg` installed and added to the system PATH
- Additional Python libraries:
  - `tqdm`
  - `tabulate`
  - `ffmpeg-python`

---

## Installation
1. Clone the repository:
   ```bash
   $ git clone https://github.com/your-username/pytube-downloader.git
   $ cd pytube-downloader
   ```
2. Create a venv environment and install the required Python libraries:
    ```bash
    $ python -m venv .venv
    $ pip install -r ./requirements.txt
    ```
3. Activate the venv using:
    ```bash 
    $ ./venv/Scripts/activate
4. Ensure `ffmpeg` is installed and added to your system PATH:
    [Download FFmpeg](https://ffmpeg.org/download.html)

---

## Usage
1. Run the script:
   ```bash
   $ python ytdownload.py
   url: 
   ```
2. Enter the YouTube video URL when propted.
3. Select the desired video by typing the `itag`.
4. Choose whether to merge the downloaded video and audio files.
5. The merged file will be saved in the `Output` directory.