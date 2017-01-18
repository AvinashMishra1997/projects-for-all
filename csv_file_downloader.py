import urllib

x=raw_input('Enter url of file u want to download here:')

def csv_file_downloader(csv_url):
    open_url = urllib.urlopen('csv_url')
    read_file = open_url.read()
    str_file = str(read_file)
    lines = str_file.split('\\n')
    save_file = r'csv_file_downloader.csv'
    file_open = open('save_file' , 'w')
    for line in lines:
        file_open.write(line + '\n')
    file_open.close()


csv_file_downloader(x)
