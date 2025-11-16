from pytubefix import YouTube
from pytubefix.cli import on_progress
from tqdm import tqdm
from tabulate import tabulate
import ffmpeg
import os

progress_bar = None
total_file_size = 0


def list_info(yt:YouTube, url:str, audio: bool=False):
    ys=None
    if (not audio):
        ys=yt.streams.filter(adaptive=True, only_video=True, file_extension="webm")
    else:
        ys=yt.streams.filter(only_audio=True, file_extension="webm")
    
    # for i in ys:
    #     print(i)
    table_data = []
    for stream in ys:
        table_data.append([stream.itag, stream.mime_type,  getattr(stream, "resolution", "N/A"), stream.resolution or "N/A", stream.filesize_approx])
    headers = ["itag", "Type", "Resolution", "FPS", "Approx. Filesize"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    

def download(yt:YouTube, audio=False):
    print("\n")
    itag=input('Enter itag: ')
    try:
        if (not audio):
            file_path=yt.streams.get_by_itag(itag).download("./Videos")
        else:
            file_path=yt.streams.get_by_itag(itag).download("./Audio")
        print(f'Downloaded: {file_path}')
        return file_path, getattr(yt.streams.get_by_itag(itag), "abr", None)
    except Exception as e:
        print(e)
        

def merge_audio_vid(vid_path: str, audio_path: str, output_path: str, audio_bitrt: str):
    if audio_bitrt:
            audio_bitrt = audio_bitrt.replace("kbps", "k")
    try:
        vid_path=ffmpeg.input(vid_path)
        audio_path=ffmpeg.input(audio_path)
        ffmpeg.concat(vid_path, audio_path, v=1, a=1).output(output_path).run()
        print(f"Merged file saved to: {output_path}")
    except ffmpeg.Error as e:
        print(f"Error during the merging process: {e}")
    
       
def prog(stream, chunk, bytes_remaining):
    global progress_bar, total_file_size
    
    if progress_bar is None:
        total_file_size = stream.filesize
        progress_bar = tqdm(total=total_file_size, unit="A", unit_scale=True, desc="Progres")
    
    progress_bar.update(len(chunk))
    
    if bytes_remaining == 0:
        progress_bar.close()
        progress_bar = None


def main():
    url = input("url: ")
    yt = YouTube(url, on_progress_callback=prog)

    # List video streams
    print("Video Streams:")
    list_info(yt, url)
    video_path, vid_brt = download(yt)  # Capture the video file path
    print("\n")

    # List audio streams
    print("Audio Streams:")
    list_info(yt, url, True)
    audio_path, aud_brt = download(yt, True)  # Capture the audio file path
    print("\n")

    # Ask user if they want to merge the files
    merge = input("Do you want to merge the files (Y/N): ").strip().lower() == "y"
    if merge:
        if video_path and audio_path:
            output_path = "./Output/merged_video.webm"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            merge_audio_vid(video_path, audio_path, output_path, audio_bitrt=aud_brt)

        else:
            print("Error: Missing video or audio file for merging.")


if __name__=="__main__":
    main()