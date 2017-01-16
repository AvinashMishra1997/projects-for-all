import random
import urllib

x=raw_input('Enter url here:')
def download_url_lib(url):
    name= random.randrange(1,1000)
    full_name= str(name) + '.jpg'
    urllib.urlretrieve(url , full_name)

download_url_lib(x)
