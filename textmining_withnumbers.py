# This code creates a term-document matrix
# A term-document matrix shows how often each word appears in each document

import re, csv, os

# This function splits a document (string) into words (tokens)
def simple_tokenize(document):
    """
    Turn a document into a list of words.

    - Change everything to lowercase.
    - Replace anything that is not a letter or number with a space.
    - Split the text into words and return.
    """
    document = document.lower()
    document = re.sub('[^a-z0-9]', ' ', document)
    return document.strip().split()


# This class makes a term-document matrix
class TermDocumentMatrix(object):

    def __init__(self, tokenizer=simple_tokenize):
        """
        Start with an empty matrix.

        - You can give your own tokenizer function.
        - If you don’t give one, it uses simple_tokenize.
        """
        self.tokenize = tokenizer
        self.sparse = []         # List of dictionaries, one per document
        self.doc_count = {}      # Count how many documents have each word

    def add_doc(self, document):
        """
        Add a new document to the matrix.

        - Split it into words.
        - Count how often each word appears in this document.
        - Save the word counts.
        - Update how many documents contain each word.
        """
        words = self.tokenize(document)
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        self.sparse.append(word_counts)
        for word in word_counts:
            self.doc_count[word] = self.doc_count.get(word, 0) + 1

    def rows(self, cutoff=2):
        """
        Get rows for the term-document matrix.

        - Only keep words that appear in at least 'cutoff' documents.
        - First row: list of words (header).
        - Next rows: how many times each word appears in each document.
        """
        words = [word for word in self.doc_count if self.doc_count[word] >= cutoff]
        yield words  # Header row with words
        for row in self.sparse:
            data = [row.get(word, 0) for word in words]
            yield data  # Word counts for each document

    def write_csv(self, filename, cutoff=2):
        """
        Save the matrix to a CSV file.

        - 'filename' is the name of the file to save.
        - Only include words that appear in at least 'cutoff' documents.
        """
        f = csv.writer(open(filename, 'wb'))  # 'wb' is for binary write mode (Python 2)
        for row in self.rows(cutoff=cutoff):
            f.writerow(row)

