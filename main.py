import sys
from Dependencies.Nhentai_api.Nhentai_api import *
import os

def main():
    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)

    if True:
        id = 123946

        b = Book(id)
        dir = path + b.name
        if not os.path.exists(dir):
            os.makedirs(dir)
        b.SaveAllImages(dir)


    else:
        q = Search("females only", 1, True)
        q.DownloadBooks(path)


if __name__ == "__main__":
    if True:
        import time

        start_time = time.time()
        main()
        print("Program execution finisged in --- %s seconds ---" % (time.time() - start_time))
    else:
        import cProfile

        cProfile.run('main()')
