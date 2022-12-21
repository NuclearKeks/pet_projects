from pytube import YouTube, Playlist
from os import system


def show_res_list(video):
    res_list = [stream.resolution for stream in video.streams.filter(progressive=True, file_extension='mp4')]
    print("----\nChoose the resolution from list:")
    for res in res_list:
        print(res)
    d_res = input('----\n')
    if d_res.find('p') == -1:
        d_res += 'p'
    return d_res


def download_moment(video, res):
    print(f'Downloading {video.title}')
    v = video.streams.get_by_resolution(res)
    try:
        v.download(output_path=directory)
    except:
        print(f"DownloadError {v.title}")

def download():
    system('cls')
    link = input("Enter a video/playlist link:\n")
    if link.find('/playlist?') !=-1:
        yt = Playlist(link)
        res = show_res_list(yt.videos[0])
        for video in yt.videos:
            download_moment(video, res)
    else:
        yt = YouTube(link)
        res = show_res_list(yt)
        download_moment(video, res)

    another = input("Download another video?(Y/N): ")
    if another.lower() == 'y':
        download()
    else:
        print("Download complete")

if __name__ == "__main__":
    system('cls')
    print('Choose directory for download:')
    directory = input(r'')
    download()