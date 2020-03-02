from DoujinshiDownloader import *
import os

if __name__ == "__main__":

    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)


    """id = 123946

    b = Book(id)
    dir = path + b.name
    if not os.path.exists(dir):
        os.makedirs(dir)
    b.SaveAllImages(dir)"""


    import time

    start_time = time.time()
    q = Search("females only", 1, True)
    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)
    q.DownloadBooks(path)

    print("--- %s seconds ---" % (time.time() - start_time))
