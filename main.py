import sys
from qr import generate_qr
from firebase import upload_and_return_url

def get_timestamp_filename():
    import time
    return time.strftime("%Y%m%d-%H%M%S")

def upload_and_download_qr(argv):
    filename = argv[0]
    url = upload_and_return_url(filename)
    generate_qr(url, get_timestamp_filename())    
    

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: main.py [FILENAME}")
        exit(1)
    upload_and_download_qr(sys.argv[1:])
