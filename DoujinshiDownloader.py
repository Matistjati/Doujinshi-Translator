import requests
import urllib
import os
from concurrent.futures import ThreadPoolExecutor


class Book:
    def GetBookInfo(self):
        while True:
            url = "https://nhentai.net/api/gallery/" + str(self.book_id)
            resp = requests.get(url=url)
            if resp.status_code == 200:
                data = resp.json()
                return data
            elif resp.status_code == 503:
                continue
            else:
                print("a man has fallen into the lego river")
                return ""

    def __init__(self, bookId):
        self.book_id = bookId
        self.book_info = self.GetBookInfo()
        self.bad = False

        if self.book_info == "":
            self.bad = True
            return

        self.media_id = self.book_info["media_id"]
        self.page_count = self.book_info["num_pages"]
        self.name = self.book_info["title"]["english"]

    def SaveImage(self, path, page, imageType):
        if os.path.isfile(path):
            return

        url = "https://i.nhentai.net/galleries/" + str(self.media_id) + "/" + str(page) + imageType
        with open(path, 'wb') as file:
            file.write(requests.get(url).content)



    def SaveAllImages(self, path):

        if self.bad:
            return

        for page in range(self.page_count):
            self.SaveImage(path + "/" + str(page + 1) + ".jpg", page + 1, ".jpg")

    def __call__(self, dir, page):
        type = self.book_info["images"]["pages"][page]["t"]
        type = ".jpg" if type == "j" else ".png"

        self.SaveImage(dir + type, page, type)

def CreateBook(id, bookList, i):
    bookList[i] = Book(id)

class Search:
    def GetSearchInfo(self):
        sort = "popular" if self.popular else ""
        url = "http://nhentai.net/api/galleries/search?query=" + self.query + "&page=" + str(self.page) + "&sort=" + sort
        print(url)
        resp = requests.get(url=url)
        data = resp.json()
        return data

    def __init__(self, query, page, popular=False):
        self.query = query
        self.popular = popular
        self.page = page
        self.searchInfo = self.GetSearchInfo()
        self.result = self.searchInfo["result"]
        self.books = []

        executor = ThreadPoolExecutor(len(self.result))
        for i in range(len(self.result)):
            self.books.append({})

        for i, book in enumerate(self.result):
            executor.submit(CreateBook, book["id"], self.books, i)

        executor.shutdown()



    def SaveBook(self, book, dir):
        imageDownloader = ThreadPoolExecutor(len(self.books))

        for page in range(book.page_count):
            imageDownloader.submit(book, dir + "/" + str(page + 1), page + 1)

        imageDownloader.shutdown()

    def __call__(self, book, dir):
        self.SaveBook(book, dir)

    def DownloadBooks(self, directory):
        executor = ThreadPoolExecutor(len(self.books))

        for i, book in enumerate(self.books):
            if book.bad:
                continue

            name = book.name
            blackList = ["/","\\",":","*","?","\"","<",">","|"]
            for i in blackList:
                name = name.replace(i, "")
            dir = directory + name

            if not os.path.exists(dir):
                os.makedirs(dir)

            executor.submit(self, book, dir)

        executor.shutdown()