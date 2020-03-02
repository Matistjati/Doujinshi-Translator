from DoujinshiDownloader import *
import os

if __name__ == "__main__":

    #id = 123946

    #b = Book(id)
    #b.SaveAllImages('C:/Users/joshua.jeffmarander/desktop/plot')
    import time

    start_time = time.time()
    q = Search("females only", 1, True)
    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)
    q.DownloadBooks(path)

    print("--- %s seconds ---" % (time.time() - start_time))
