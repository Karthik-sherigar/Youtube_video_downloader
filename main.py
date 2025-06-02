import yt_dlp
link = input("Paste/Enter the video link below : ")
yt_dlp.YoutubeDL({'format':'best','outtmpl':'%(title)s.%(ext)s'}).download([link])