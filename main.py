import sys
sys.path.insert(0,"Dependencies/Nhentai-api")
from Nhentai_api import *
import os

def main():
    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)

    if False:
        id = 123946

        b = Book(id)
        dir = path + b.name
        if not os.path.exists(dir):
            os.makedirs(dir)
        b.save_all_images(dir)


    else:
        q = Search("females only", 1, True)
        q.download_books(path)


if __name__ == "__main__":
    if True:
        import time

        start_time = time.time()
        main()
        print("Program execution finished in --- %s seconds ---" % (time.time() - start_time))
    else:
        import cProfile

        cProfile.run('main()')
