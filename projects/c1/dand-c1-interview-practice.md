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
The query groups entries by variable `state` and sums the corresponding values in column `active` to obtain the number of active users for each state. A simple sum is enough because the variable is Boolean (0: non-active user; 1: active user). The output is sorted in descending order, and only the top five values are displayed.

## Question 4
_Define a function `first_unique` that takes a string as input and returns the first non-repeated (unique) character in the input string. If there are no unique characters return `None`._

### Answer
```python
def first_unique(string):

    return unique_char
```
