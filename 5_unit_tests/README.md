# Unit Tests

Testing is obviously an important part of software development, unless
you develop for AAA game studios. Then you could get away with stuff like this:

![skyrim horse](https://media.giphy.com/media/upBMycPndsCvm/giphy.gif)

There are different types of tests used throughout the software lifecycle,
but we'll focus on unit tests for now. Unit tests are intended to test a
specific piece of code, and only that piece. They focus on a specific
class or component in the code, and ensure that it works properly. They
also run very quickly, allowing you to run hundreds of tests on the
order of seconds.

It's definitely worth it to establish good unit tests as you write code. The
initial investment into writing the test will pay off. If you have a lot of
unit tests to verify your code is working, you can make changes to designs
or implementation, and be confident your changes didn't break the code!

Or, some unit tests will fail, and you'll know quickly that you broke some
specific functionality. This saves you a lot of time by shortening your
development loop. The other option is to discover your bugs through integration
testing, which can take hours to run. Or, even worse, having a customer
discover them. By that point, you'll probably be working on something
different, which makes switching back to bug fixing more difficult.

Remember how we broke down TicTacToe into different components?
Each component should be unit tested. Generally, unit tests
focus on just one specific component. If your class has a connection
to a MySQL database, unit tests want to isolate your specific component,
and ignore the MySQL interaction.

## Mock objects
Mock objects help unit tests interact with complex dependencies.
In the previous MySQL example, there would be an object that
handles the MySQL interaction. Instead of using that object,
and all the complex initialization that comes with it, you can
use a mock object.

A mock object doesn't need to have a real connection to a database.
Instead, you can specify the behavior for the mock object so
it acts *as if* it was connected to a database. This gives you
an easy way to reproduce database behavior in your code, without
actually needing a database.

Mocking objects is not necessary for this assignment, so we'll leave
it at that for now.

If you want to learn more, [here's](https://realpython.com/python-mock-library/)
a good resource.

## When should I write my unit tests?
There's no one answer here. There are a number of methodologies.

Test driven development has people write the unit test first, before
actually implementing the thing you're trying to do. This helps specify
the intended behavior, and you'll know your stuff works when you pass
all the tests.

I prefer to do quick iterations of coding implementation and unit tests. This
allows you to focus on making a good and easy to understand design, and testing
it when it solidifies.

So, code a little bit, solidify the design, come to a stopping point, and
write some unit tests. Find the right balance for you.

## Python's unittest module
Luckily, again, Python has a built in module for unit testing!

# Let's do some testin'
First, **copy** your TicTacToe implementation file into `./work`.
It'll be interesting to compare your unit tested implementation against
your initial one.

Implement your unit tests in a file called `<your_name>_tictactoe_ut.py`.

## 1. Write a basic unit test

We can start simply by making a unit test that doesn't require
any other file. We import the `unittest` module and create
a basic test case.

Test cases are a collection of individual unit tests. For now,
we can make one test case per component. Test cases are
classes themselves, and must inherit the `TestCase` class
in the `unittest` module.

Each test in the test case does some operations and asserts
some condition or state. The test functions have to start
with `test` so that the test runner code knows to execute them.

If we want to do a simple check to see if two numbers are
equal, it will look like this:

```Python
import unittest

class TestBasic(unittest.TestCase):

    def test(self):
        num_1 = 2 + 2
        num_2 = 4
        self.assertEqual(num_1, num_2)

if __name__ == '__main__':
    unittest.main()
```

Run this test with the following command:

`python3 <your_unit_test_file.py> -v`

See what happens if you change `num_2` to a value other than 4.

Here's another [tutorial](https://cgoldberg.github.io/python-unittest-tutorial/)
on Python unit testing. It also contains a list of common assertion
methods.


## 2. Modify your TicTacToe program

All our code is in one specific implementation file. To get access to that code
from our unit test program, we'll want to import it as a module *into* our test
program. When we do this, Python will run the code in the module you are
importing. Because we initialize the game and invoke `play()` in the original
implementation, the game will run when we run our unit tests. That's not what
we want.

We want two behaviors. When we run it as a standalone program, we want the game
to run normally. When we unit test it, we don't want the game to run. We only
want to use the components.

To work around this, we need to modify our TicTacToe implementation.
First, move the main execution code into a function called `main()`.
Then, add a conditional to *only* invoke `main()` if we run the
Python file directly.

It should look something like this:

```Python
def main():
    game = GameLoop()
    game.play()

if __name__ == "__main__":
    main()
```

That conditional will prevent the game execution when the file is
being imported. This works because `__name__` is a special variable. If
the file is being executed directly, `__name__` will be `__main__`.
If the file is being imported, `__name__` will be the module name.
(ie. the Python filename without the `.py` extension)


## 3. Import your TicTacToe into your unit test file

Any Python file can be used as a module. A file `test_prog.py` has the module
name `test_prog`. You can import it with a simple `import` statement. If you do
this though, your classes will have to be prefixed with the module name
every time you use them. This is because they are in a different namespace
than your unit test code.

Another option is to import them with `from ... import ...` style. So, if you
do something like this:

`from <your_tictactoe_file_without_the_py_suffix> import GameBoard`

This will allow you to use `GameBoard` without prefixes, in your unit
test file.


## 4. Write your test cases and tests

Make a test case for each component (class) in your TicTacToe file. Each test
case can have a `setUp()` method. This method runs before every specific test
and sets up any objects you may need. You can use that method to set up a
`GameBoard` object, instead of setting it up inside every `test` function.

Think of the tests each class should have, and try them out!


# Some more resources
[Here's](https://realpython.com/python-testing/) a good article
if you're looking for more info.
