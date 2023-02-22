import requests
from multiprocessing.pool import ThreadPool
 
def download_url(url):
  print("downloading: ",url)
  # assumes that the last segment after the / represents the file name
  # if url is abc/xyz/file.txt, the file name will be file.txt
  file_name_start_pos = url.rfind("/") + 1   # rfind finds the last occurence of the /
  file_name = url[file_name_start_pos:]      # slicing of a string for file name
 
  r = requests.get(url, stream=True)        
  if r.status_code == requests.codes.ok:
    with open(file_name, 'wb') as f:
      for data in r:
        f.write(data)
  return url

urls = ["url here"]
# Run 5 multiple threads. Each call will take the next element in urls list
results = ThreadPool(5).imap_unordered(download_url, urls)
for r in results:
    print(r)