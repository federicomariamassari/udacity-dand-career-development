"""Udacity Data Analyst Nanodegree: C1 Data Analyst Interview Practice

(2018) Federico Maria Massari / federico.massari@bocconialumni.it

This module contains all the code for Udacity Career Development Project C1.
Requires Python 3.
"""

"""ANSWER TO QUESTION 2
"""
class Truffle:
    """Create an instance for a truffle with a particular filling.

    Attributes:
        N -- int. The number of same-flavoured truffles in the box.
        k -- int. The desired number of same-flavoured truffles to pick.
    """

    def __init__(self, N, k):
        self.N = N
        self.k = k

def pick_sequence(*args, permutation=False):
    """Compute the probability of a sequence of truffles without replacement.

    Arguments:
        *args -- class. A variable number of Truffle instances.

    Keyword arguments:
        permutation -- bool. If True (i.e., order matters) use permutations
            to calculate probability. Else, use combinations (default False).

    Returns:
        float. Probability, as the ratio of desired over total outcomes.
    """
    from scipy import special

    # Initialise variables to sum (0) and multiply (1)
    box = pick = 0
    desired = total = 1

    for e in args:
        box += e.N    # Total truffles in the box
        pick += e.k   # Total truffles to pick

        if permutation:
            desired *= special.perm(e.N, e.k)
        else:
            desired *= special.comb(e.N, e.k)

    if permutation:
        total = special.perm(box, pick)
    else:
        total = special.comb(box, pick)

    return desired / total

"""ANSWER TO QUESTION 4
"""
def first_unique(string):
    """Return the first unique character of a non-fully-numeric string.

    Arguments:
        string -- str. The input string.

    Returns:
        str. The first non-repeated character of a string, unless the latter
        is fully numeric or has no uniques. In those cases, return None.
    """
    if string.isdigit():
        return None

    # Simply return the non-digit string of length one
    elif len(string) == 1:
        return string

    else:
        # Find the set of all characters in the string
        uniques = set(string)

        try:
            # Map unique, non-digit characters to their position inside the
            # string using dictionary comprehension
            mapping = {e: string.find(e) for e in uniques
                       if string.count(e) == 1 and not e.isdigit()}

            # Return unique character with smallest position index
            return string[min([mapping[i] for i in mapping])]

        except ValueError:
            # Rule out strings with non-unique characters
            return None
