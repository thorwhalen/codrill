
# codrill
Extract code exercises from code itself

To install:	```pip install codrill```

There's so many extremely useful gems in builtins (there's also a lot of useless noise).
Personally, I use `collections`, `itertools` and `functools` as well as `map` and `zip` constantly.
Also recently, `contextlib`.

Sometimes, you can avoid a many line function simply by putting a few right builtin elements together.

Knowing what's out there is a first step.

But it's not enough. You got to think of these components when a problem arises.
So you need actual practice.

For example, what would the one liner be to implement this function:

```python
def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return ...  # fill in the blanks
```

See the answer in [itertools recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes).
The latter contains many more opportunities for such exercises.

But it would be nice to be able to extract these automatically from code. So here's my little version of that.

# Examples:

## `more_itertools`

To get random exercises for the `more_itertools` module
(need to pip install it if you don't have it).

```python
from codrill import Exercises
import more_itertools.more as m
e = Exercises(m)
# and then repeatedly ask for random exercises.
e.print_random_exercise()
```

This `Exercises` class is meant to be subclassed to include tracking of exercises presented,
and possibly performance metrics (explicitly self-declared or inferred from a response).
These statistics can then be used to chose the exercises not randomly, but so as to
optimize learning.


## itertools recipes

I don't know of a pip installable package for the
 [itertools recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes)
so I copied that code and put in a local file under `.../ut/util/uiter.py`.

Using that setup, in the following I'll print out all the exercises that
have no more than 30 lines of docs and 4 lines of code.
This filtering helps to not get exercises that are too large in their
description (the docs) or their solution (the code).

```python
from codrill import snippets_of_funcs
import ut.util.uiter as m
# find the file for uiter here:
#   https://github.com/thorwhalen/ut/blob/master/util/uiter.py

for snippet in snippets_of_funcs(m, max_code_lines=4, max_doc_lines=30):
    if not snippet.startswith('_'):
        print(snippet)
        print()
```
