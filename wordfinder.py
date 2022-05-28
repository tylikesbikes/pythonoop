"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """
    picks random words from a file that contains one word on each line

    >>> wf = WordFinder('testwords.txt')
    5 words read

    >>> wf.random() in ['bike','bicycle','bicicleta','velo','velocipede']
    True

    """
    def __init__(self, path):
        self.file_path = path
        self.word_list = self.get_words()
        self.num_words = self.print_word_count()

    def get_words(self):
        """creates a list of words in the file at location 'path'"""
        f = open(self.file_path,'r')
        l = []
        for line in f:
            l.append(line.strip())

        f.close()
        
        return l

    def print_word_count(self):
        print (f"{len(self.word_list)} words read")

    def random(self):
        return self.word_list[randint(0,len(self.word_list)-1)]

class SpecialWordFinder(WordFinder):

    def get_words(self):
        f = open(self.file_path,'r')
        l=[]
        for line in f:
            if line[0] not in ["#","\n"]:
                l.append(line.strip())

        f.close()

        return l