def read_market_data(filename):
    """
    Read in the farmers market data from the given filename and return
    a tuple of two objects:
    1) A dictionary mapping zip codes to lists of farmers market tuples.
    2) A dictionary mapping towns to sets of zip codes.
    """
    return {}, {} # replace this line


def format_market_data(market):
    """
    Return a human-readable string representing the farmers market tuple
    passed to the function in the market parameter.
    """
    return "" # replace this line


if __name__ == "__main__":

    # This main program reads in the file markets.txt once and then asks
    # the user repeatedly to enter a zip code or a town name (in a while
    # loop until the user types "quit").

    FILENAME = "markets.txt"

    try:
        zip_to_market, town_to_zips = read_market_data(FILENAME)

        # your main loop goes here 

    except (FileNotFoundError, IOError):
        print("Error reading {}".format(FILENAME))
