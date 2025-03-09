from pytubefix import YouTube
from pytubefix.cli import on_progress


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
    yt=YouTube(url)
    
    list_info(yt, url)
    download(yt)
    print("\n")
    list_info(yt, url, True)
    download(yt, True)
    
    

def prog():
    pass


if __name__=="__main__":
    main()