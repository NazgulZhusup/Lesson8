# class Book():
#     def read(self):
#         print("Reading")
#
# class StoryReader():
#     def __init__(self):
#         self.books = Book()
#
#     def tell_story(self):
#         self.books.read()




from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySource):
    def get_story(self):
        print("Reading story")


class AudioBook(StorySource):
    def get_story(self):
        print("Listening story")


class StoryReader():
    def __init__(self, story_source: StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()


book = Book()
audiobook = AudioBook()

readerBook = StoryReader(book)
readerAudioBook = StoryReader(audiobook)

readerBook.tell_story()
readerAudioBook.tell_story()






