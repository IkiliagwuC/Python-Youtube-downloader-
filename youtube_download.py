from sys import argv

script, video_url = argv

from pytube import YouTube

download_folder = r"C:\Users\USER\Downloads"

#remove hardcoding of the video url
# video_url = "https://www.youtube.com/watch?v=5-IN"

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()

stream.download(download_folder)

print("download successful, check download folder for file")
