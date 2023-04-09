from pytube import YouTube
from tqdm import tqdm

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress_bar.update(bytes_downloaded)

url = "https://www.youtube.com/watch?v=AqyWfisjCFQ"

# Create the YouTube object first
yt = YouTube(url)

# get the highest resolution video stream
stream = yt.streams.get_highest_resolution()

# get the total file size in bytes
file_size = stream.filesize

# create a progress bar object
progress_bar = tqdm(total=file_size, unit="iB", unit_scale=True)

# Then register the callback
yt.register_on_progress_callback(on_progress)

# Download the video, getting back the file path the video was downloaded to
file_path = yt.streams.filter(progressive=True).get_highest_resolution().download()
print(f"file_path is {file_path}")