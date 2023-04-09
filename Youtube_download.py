import pytube

# set the download location
download_loc = r'C:\Users\suraj\Downloads'
#get the url
video_url = input('Enter the url: ')

#Create an instance of Youtube video
video_inst = pytube.YouTube(video_url)

stream = video_inst.streams.get_highest_resolution()

#download
stream.download()
print("File Succesfully downloaded")