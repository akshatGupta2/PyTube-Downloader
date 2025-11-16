from pytubefix import YouTube
from pytubefix.cli import on_progress
from tqdm import tqdm

progress_bar = None
total_file_size = 0


def list_info(yt:YouTube, url:str, audio=False):
    ys=None
    if (not audio):
        ys=yt.streams.filter(adaptive=True, only_video=True)
    else:
        ys=yt.streams.filter(only_audio=True)
    
    for i in ys:
        print(i)


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
    pass


def complete():
    pass


if __name__=="__main__":
    main()