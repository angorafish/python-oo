import random
class WordFinder:
    """
    Word Finder: finds random words from a dictionary.
    >>> wf = WordFinder('test_words.txt') # 'test_words.txt' has 3 words: ["apple", "banana", "orange"]
   3 words read

   >>> wf.random() in ['apple', 'banana', 'orange']
   True

   >>> len(wf.words)
   3
    """

    def __init__(self, path):
        """Reads dictionary and reports number of words read."""
        self.words = self.read_words(path)
        print (f"{len(self.words)} words read")

    def read_words(self, path):
        """Reads the words from a file and returns a list of words."""
        with open(path) as file:
            return [line.strip() for line in file]
        
    def random(self):
        """Return a random word from word list."""
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """
    Special Word Finder: Retrieves random word from a dictionary, 
    ignores comments and blank lines.

    >>> swf = SpecialWordFinder('special_test_words.txt') # 'special_test_words.txt has 4 valid lines.
    4 words read

    >>> swf.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    >>>len(swf.words)
    4
    """
    def read_words(self, path):
        """Reads words from a file, filters out comments and blank lines,
        then returns a list of valid words."""
        with open(path) as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]
        