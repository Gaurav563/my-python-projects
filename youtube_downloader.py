# from pytube import YouTube

# link = "https://www.youtube.com/watch?v=rgfiZB5EudA"
# youtube_1= YouTube(link)
# #------------------- PRINTING TITLE ------------------------
# # print(youtube_1.title)
# #------------------- PRINTING THUMBNAIL URL ---------------
# # print(youtube_1.thumbnail_url)


# # for all

# videos= youtube_1.streams.all()
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)

# stream = int(input( " enter :"))
# videos[stream].download()
# print("succesfully")
# #=========================================

# # =========== Audio only with filter============
# videos= youtube_1.streams.filter(only_audio=True)
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)

# stream = int(input( " enter :"))
# videos[stream].download()
# print("succesfully")

# # ***** playlist ****
from pytube import Playlist
py = Playlist("Paste the playlist url")
print(f'downloading :{py.title}')
for video in py:
    video.streams.first().download()
    