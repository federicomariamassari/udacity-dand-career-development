### Question 2
_You are given a **ten-piece** box of chocolate truffles. You know based on the label that six of the pieces have an orange cream filling and four of the pieces have a coconut filling. If you were to eat four pieces in a row, what is the probability that the **first two** pieces you eat have an orange cream filling and the **last two** have a coconut filling?_

### Answer
The probability to select truffles in the given order and without replacement is:
```
pr(X = {orange_cream, orange_cream, coconut, coconut}) = 6/10 * 5/9 * 4/8 * 3/7 ≈ 0.07142857
```
Using combinations, the number of ways of choosing two orange cream filling truffles out of six available, and two coconut filling truffles out of four available are, respectively, <sub>6</sub>C<sub>2</sub> = 15 and <sub>4</sub>C<sub>2</sub> = 6. So, the number of ways of choosing two orange cream filling and two coconut filling is the product of the above, 15 * 6 = 90. The number of ways of picking four truffles out of ten available is <sub>10</sub>C<sub>4</sub> = 210. The probability is defined as the ratio of desired over total possible outcomes, in this case 90 / 210 ≈ 0.428571. However, of the six combinations _X_ = {OOCC, OCOC, OCCO, COOC, COCO, CCOO} only the first one is admissible. Therefore, one must divide the result by <sub>4</sub>C<sub>2</sub> = 6, to obtain _p_(_X_ = OOCC) ≈ 0.07142857.


```python
class Truffle:
    def __init__(self, N, k):
        self.N = N
        self.k = k
```

```python
def pick_sequence(*args, ordered=False):
    """Compute probability of picking a sequence of truffles from a box

    Compute the probability of choosing a desired sequence from a box of
    assorted truffles, without replacement and, if applicable, specifying
    whether order matters.

    Arguments:
        *args -- class. A kind of truffle. Instance with attributes:
            - N: int. The total number available in the box
            - k: int. The desired number to pick

    Keyword arguments:
        ordered -- bool. If True, sequence order matters (default False)
    """
    from scipy import special

    box, picked, desired, total = 0, 0, 1, 1

    for e in args:
        box += e.N
        picked += e.k
        desired *= special.comb(e.N, e.k)

    total = special.comb(box, picked)

    if ordered:
        total *= special.comb(picked, args[0].k)

    return desired / total
```

```python
orange_cream = Truffle(6, 2)
coconut = Truffle(4, 2)
```

```python
pick_sequence(orange_cream, coconut, ordered=True)
```

```
0.071428571428571425
```

#### Follow-up
_If you were given an identical box of chocolates and again eat four pieces in a row, what is the probability that exactly **two** contain coconut filling?_

#### Answer
In this case order does not matter, so there are six possible sequences:

```python
pick_sequence(orange_cream, coconut)
```

```
0.42857142857142855
```
