from pytubefix import YouTube
from pytubefix.cli import on_progress
from tqdm import tqdm
from tabulate import tabulate

progress_bar = None
total_file_size = 0


def list_info(yt:YouTube, url:str, audio=False):
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
    if (not audio):
        yt.streams.get_by_itag(itag).download("./Videos")
    else:
        yt.streams.get_by_itag(itag).download("./Audio")
    
    
def main():
    url=input("url: ")
    yt=YouTube(url, on_progress_callback=prog)
    
    list_info(yt, url)
    tqdm(download(yt))
    print("\n")
    list_info(yt, url, True)
    tqdm(download(yt, True))
    
    
def prog(stream, chunk, bytes_remaining):
    global progress_bar, total_file_size
    
    if progress_bar is None:
        total_file_size = stream.filesize
        progress_bar = tqdm(total=total_file_size, unit="A", unit_scale=True, desc="Progres")
    
    progress_bar.update(len(chunk))
    
    if bytes_remaining == 0:
        progress_bar.close()
        progress_bar = None


if __name__=="__main__":
    main()