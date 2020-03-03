from DoujinshiDownloader import *
import os

def main():
    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)


    """id = 123946

    b = Book(id)
    dir = path + b.name
    if not os.path.exists(dir):
        os.makedirs(dir)
    b.SaveAllImages(dir)"""



    q = Search("females only", 1, True)
    path = "plot/"
    if not os.path.exists(path):
        os.makedirs(path)
    q.DownloadBooks(path)


if __name__ == "__main__":
    if True:
        main()
    else:
        import cProfile

        cProfile.run('main()')
