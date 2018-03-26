# Data Analyst Nanodegree: C1 Interview Practice
__Federico Maria Massari / federico.massari@bocconialumni.it__

## Question 2
_You are given a **ten-piece** box of chocolate truffles. You know based on the label that six of the pieces have an orange cream filling and four of the pieces have a coconut filling. If you were to eat four pieces in a row, what is the probability that the **first two** pieces you eat have an orange cream filling and the **last two** have a coconut filling?_

### Answer
Out of ten truffles in the box, the probability of picking one with orange cream filling is 6/10. If the truffle is not replaced, the probability of choosing a second one of the same kind is 5/9. Then, out of eight remaining chocolates, the chance of taking one with coconut filling is 4/8, and that of picking another one with the same filling is 3/7. Hence, the probability of selecting the truffles in the given order and without replacement is:
```
pr(X = {orange_cream, orange_cream, coconut, coconut}) = 6/10 * 5/9 * 4/8 * 3/7 ≈ 0.07142857
```
### Alternative solution
Using permutations, the number of ways of choosing two orange cream filling truffles out of six available, and two coconut filling truffles out of four available are, respectively, <sub>6</sub>P<sub>2</sub> = 30 and <sub>4</sub>P<sub>2</sub> = 12. So, the number of ways of choosing two orange cream filling and two coconut filling is the product of the above, 30 * 12 = 360. The number of ways of picking four truffles out of ten available is <sub>10</sub>P<sub>4</sub> = 5040. The probability is defined as the ratio of desired over total possible outcomes, in this case 360 / 5040 ≈ 0.07142857.

The solution is easy to implement in Python. Define class object `Truffle` to characterise truffles with different fillings:

```python
class Truffle:
    """Create an instance for a truffle with a particular filling.

    Attributes:
        N -- int. The number of same-flavoured truffles in the box.
        k -- int. The desired number of same-flavoured truffles to pick.
    """

    def __init__(self, N, k):
        self.N = N
        self.k = k
```
Then, create an instance for each available kind of truffle:
```python
orange_cream = Truffle(6, 2)
coconut = Truffle(4, 2)
```
Specify the selection algorithm as follows (`*args` allows to input a variable number of Truffle instances):
```python
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
```
The desired probability is:
```python
pick_sequence(orange_cream, coconut, permutation=True)
```
```
0.071428571428571425
```

### Follow-up
_If you were given an identical box of chocolates and again eat four pieces in a row, what is the probability that exactly **two** contain coconut filling?_

### Answer
Since order does not matter anymore, we use combinations:

```python
pick_sequence(orange_cream, coconut)
```
```
0.42857142857142855
```

## Question 3
_Given the table `users`:_

```
Table "users"
+-------------+-----------+
| Column      | Type      |
+-------------+-----------+
| id          | integer   |
| username    | character |
| email       | character |
| city        | character |
| state       | character |
| zip         | integer   |
| active      | boolean   |
+-------------+-----------+
```
_construct a query to find the **top five states** with the **highest number of active users**. Include the number for each state in the query result. Example result:_
```
+------------+------------------+
| state      | num_active_users |
+------------+------------------+
| New Mexico | 502              |
| Alabama    | 495              |
| California | 300              |
| Maine      | 201              |
| Texas      | 189              |
+------------+------------------+
```

### Answer
A possible solution to the problem could be this:
```sql
SELECT state, sum(active) AS num_active_users
    FROM users
    GROUP BY state
    ORDER BY num_active_users DESC
        LIMIT 5;
```

### Explanation
First, the query takes table `users` and groups its entries by variable `state`. Then, it sums the corresponding values in column `active` (using an alias) to obtain the number of active users for each state. A simple sum is enough, in this case, because the variable is Boolean (0: non-active user; 1: active user). Finally, the output is sorted in descending order, and only the top five values, together with the state they relate to, are displayed.

## Question 4
_Define a function `first_unique` that takes a string as input and returns the first non-repeated (unique) character in the input string. If there are no unique characters return `None`._

### Answer
```python
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
```

### Explanation
To minimise execution time, the function preliminary checks whether the string is fully numeric, and if not, whether it has length one. In the first case, the function returns None; in the second, the string itself. Length is tested second, to avoid one-digit strings (e.g., '1') as output.

The bulk of the code is run if these conditions do not apply. First, the function generates the set of characters in the string, including numbers (which are filtered out in the next step). Then, using dictionary comprehension, it maps each character to the position it is first found inside the string, but only if the character is unique (i.e., count equal to 1) and not a digit. Strings with no unique characters (e.g., 'aa') would break the algorithm at this point, hence the code is placed inside a _try-except_ block. Finally, the function transverses the dictionary, and returns the unique character whose position index is the smallest. If an exception is raised (i.e., no unique character in the string), the function returns None.

__Time complexity.__ The algorithm should take, on average, _linear time_ O(n). The best case would be _constant time_ O(1), if the input string (either numeric or character) has length 1. The worst case would be _linear time_ O(3n), if the input string is a sequence of unique characters: in this situation, `set` would not decrease its length, and both dictionary comprehension and the minimum operator would have to cross the original string in its entirety.

__Space complexity.__ Apart from the best case scenario, in which either None or the input string are returned, the algorithm creates two intermediate variables, `uniques` and `mapping`. At worst, these have, respectively, the same and twice (the dictionary also stores the position index) the length of the original string. While maximum space complexity can be O(4n), on average it should be O(2n), if input is included in the computation. Approximate space complexity is O(n).
