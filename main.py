import sys
sys.path.insert(0,"Dependencies/Nhentai-api")
from Nhentai_api import *
import os

def main():
    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)

    test_case = 2
    if test_case == 0:
        id = 123946

        b = Book(id)
        dir = path + b.name
        if not os.path.exists(dir):
            os.makedirs(dir)
        b.save_all_images(dir)


    elif test_case == 1:
        q = Search("females only", 1, True)
        q.download_books(path)

    elif test_case == 2:
        id = 123946

        b = Book(id)
        print(b.get_tags())

    else:
        print("Invalid test case")


if __name__ == "__main__":
    if True:
        import time

        start_time = time.time()
        main()
        print("Program execution finished in --- %s seconds ---" % (time.time() - start_time))
    else:
        import cProfile

        cProfile.run('main()')
