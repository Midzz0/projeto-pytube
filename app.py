from pytube import YouTube
from pytube import Playlist
import os

print("====================")
print("Download de Videos")
print("====================")

def menu():
    print("Pytube Downloader")
    print("1 - Download de videos")
    print("2 - Download de audios")
    print("3 - Download de playlist")
    print("0 - Sair")

def download_video():
    pass
    a = input("Coloque o link do video que deseja baixar: ")
    yt = YouTube (a)
    video = yt.streams.get_highest_resolution()
    video.download('./videos')
    print("Video baixado com sucesso")

def download_audio():
    pass
    b = input("Coloque o link do video que deseja baixar o áudio: ")
    yt = YouTube (b)
    audio = yt.streams.filter(only_audio=True).all()
    audio[0].download('./audios')
    print("Audio baixado com sucesso")

def download_playlist():
    pass
    p = input("Coloque o link da playlist que deseja baixar: ")
    playlist = Playlist(p)
    for url in playlist:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path='playlist')
    print("Playlist baixado com sucesso")
    
def main():
    menu()
    while True:
         opc = input("Insira uma opção: ")
         match opc:
              case '1':
                download_video()
                break
              case '2':
                 download_audio()
                 break
              case '3':
                 download_playlist()
                 break
              case '0':
                 print("Saindo...")
                 break
              case _:
                print("Opção inválida")
                continue

if __name__ == '__main__':
   main()          

#oiiii
