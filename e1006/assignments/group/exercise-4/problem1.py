from collections import defaultdict


def count_ngrams(filename, n=2):
    """
    This function reads an input file and returns a dictionary of n-gram counts.
    filename is a string, n is an integer. The resulting dictionary maps n-grams
    to their frequency (i.e., the count of how often that n-gram appears). Each
    n-gram key is a tuple and the count is an int.
    """
    # The defaultdict class may be useful here. Check the python documentation
    # for more information:
    # https://docs.python.org/3/library/collections.html#collections.defaultdict

    pass # Replace this


def single_occurences(ngram_count_dict):
    """
    This functions takes a dictionary (in the format produces by count_ngrams)
    and returns a list of all ngrans with only 1 occurence. That is, this
    function should return a list of all n-grams with a count of 1.
    """
    return [] # Replace this


def most_frequent(ngram_count_dict, num=5):
    """
    This function takes in two parameters:
      - ngram_count_dict is a dictionary of ngram counts
      - num denotes the number of n-grams to return.
    This function returns a list of the num n-grams with the highest occurence
    in the file. For example if num=10, the method should return the 10 most
    frequent ngrams in a list.
    """

    # Hint: You may need to sort the information in the dict. Python does not
    # support sorting dicts directly. You will have to convert the dict into a
    # list of (frequency, n-gram) tuples, sort the list based on frequency, and
    # return a list of the num n-grams with the highest frequency. NOTE: you
    # should NOT return the frequencies, just a list of the n-grams

    return [] # Replace this


def main(filename, n, most_frequent_k):

    ngram_counts = count_ngrams(filename, n)

    print(f'{n}-grams that occur only once:')
    print(single_occurences(ngram_counts))

    print(f'{most_frequent_k} most frequent {n}-grams:')
    print(most_frequent(ngram_counts, most_frequent_k))


if __name__ == "__main__":
    main("", 2, 5)
