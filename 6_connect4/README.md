# Connect 4

You finish your awesome TicTacToe game and decide to show our friends.
Turns out half of them hate it because they like Connect 4 better.
*End of contrived example to warrant this assignment.*

Before moving on, familiarize yourself with
[Connect 4](https://en.wikipedia.org/wiki/Connect_Four) if you don't already
know.

So, you finished your code and some new requirements just came in. You don't
want to start from scratch to implement it. You also suspect that people will
want you to implement more games in the future.

This is pretty analogous to software product developement.

We have to modify our program to accomodate this, and make it
easier to implement future requests in our program. But firt,
let's talk about an important concept in software design.


# Levels of abstraction

The dictionary definition of abstraction is to deal with ideas rather than
specific details. In the context of software development, it means to represent
a higher level view of some operation and to avoid the details of that
operation's implementation. **This allows developers to simplify designs and
hide the detailed complexity from developers who should not be
concerned with those details.** The higher the level of abstraction, the
more generalized the idea is. That's still pretty vague for our use case, so
let's get into some examples.

The apps on your smart phone work at a high level of abstraction. As a user,
you simply install the app, and run it. You are not concerned about the
files on the operating system, or the installation process that extracts
and moves the files into the necessary locations. The code does all
that for you, at a lower level of abstraction.

Different programming languages operate at different levels of abstraction.
[Assembly language](https://en.wikipedia.org/wiki/Assembly_language) allows you
to program at a *lower* level of abstraction. You have control over specific
hardware registers and the ability to manipulate memory directly. Instead of
using conditionals, loops, functions, and classes, you use instructions
that map very close to [machine code](https://en.wikipedia.org/wiki/Machine_code)
for that specific CPU architecture. It is definitely harder for humans
to grok an assembly language program.

The other end of the spectrum has languages like Python. Python uses
conditionals, loops, functions and classes. You don't manipulate memory
directly. It operates at a *higher* level of abstraction. By using Python's
constructs, the details of the machine language are *hidden* from the
programmer. As a result, it is a lot easier for humans to read and understand
the programs. It also makes programming faster. Imagine trying to program
TicTacToe in assembly.

> The Python interpreter still transforms our human readable program into
> machine instructions before the program can execute. That's necessary because
> the CPU only understands machine instructions.

C and C++ are somewhere in between those two ends of the spectrum.

# Abstraction in the context of the TicTacToe program

In the previous assignment, you implemented TicTacToe. Your code may look
something like this pseudo code.

```
make a 3x3 game board

while true
    print the 3x3 board

    get player1 move: column and row
    make sure row and column are less than 3
    place player1 piece in cell specified by move
    check if there are 3 of the same markers in a line
    
    print the 3x3 board

    get player2 move: column and row
    make sure row and column are less than 3
    place player2 piece in cell specified by move
    check if there are 3 of the same markers in a line
```

The code above is operating a a certain level of abstraction. There's a lot of
concepts in there that are specific to TicTacToe. We make a 3x3 board
specifically for TicTacToe. We are checking the user input to make sure they
fit in the TicTacToe board. Our victory condition is specific to TicTacToe
as well. This code will not work for Connect 4.

We have a couple of options in implementing Connect 4 now. We could make
a similar loop to drive the new game. Every time somebody asks us to implement
a new game, we'd create a new loop to drive it. This doesn't scale well.

On the other hand, if we think about the game at a *higher* level of
abstraction, we quickly discover that TicTacToe and Connect 4 have a lot in
common. Let's go through the pseudo code again, at a higher level of
abstraction.

```
make a game board

while true
    print the board

    get player1 move
    make sure the move is valid
    place player1 piece
    check if a victory condition has been met
    
    print the board

    get player2 move
    make sure the move is valid
    place player2 piece
    check if a victory condition has been met
```

Notice that there is no more TicTacToe specific pseudo code! By thinking
about the games at a higher level of abstraction, we determined they both have
the following characteristics:

1. they have a game board
2. each player makes a move
3. we check whether it is valid
4. place the move on the board
5. check for a victory condition

That flow works for both of our games!

If we go back to the lower level of abstraction, the games are indeed different.
The boards are different sizes. In TicTacToe, the player must specify a column
and row to identify a cell. In Connect 4, the player only specifies a column.
(The piece "slides" down to the lowest available row.) The victory conditions
are different too. But, all these *implementation details* are *hidden* from
the main game loop code. This is what allows us to reuse this game loop for
many games!

# How do we change our code to a higher level of abstraction?
A concept in *Object Oriented Programming* (OOP) called *polymorphism* helps us do this.

## Polymorphism and inheritance
Polymorphism is the ability for the same symbol, or line of code, to behave
differently or represent multiple types. Again, a vague definition. So, on to
examples.

Consider the Python classes `Dog` and `Snake`. Each one might have some
basic attributes, and some functions to represent their behavior. For `Dog`,
we might have a `bark()` function, whereas `Snake` have `hiss()`. If we think
about these at a higher level of abstraction, the functions are simply
having the animals speak.

We can use Python class inheritance to represent this higher level of
abstraction. Inheritance allows us to specify a base class and a child
class. The child class *inherits* attributes and functions from the base
class. In this case, we can make an `Animal` class to be used as the base
class, and make `Dog` and `Snake` the child, or derived, classes.

OOP languages also allow us to *override* base class methods
when the derived class needs some specific behavior. Then, in the code,
the appropriate method will be automatically called based on the type
of object that's calling it.

Here's how we set that up:

```python
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def speak(self):
        print("Uh, generic animal noise?")

    def move(self):
        print("Uh, travel through spacetime?")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def speak(self):
        print("Woof")

    def move(self):
        print("Run")

class Snake(Animal):
    def __init__(self, name, color):
        super().__init__(name, color)

    def speak(self):
        print("Hisssss")

    def move(self):
        print("Slither")
```

Notice how `Dog` and `Snake` inherit `Animal`. Also notice that `Dog`
and `Snake` *both* have `speak()` and `move()` methods. They *override*
the behavior of those methods in `Animal` class.

Now that we've defined our classes, let's use them to see an example
of polymorphism.

Consider the following code:

```python

def make_animal(type):
    if type == 1:
        return Dog("Fido", "black")

    if type == 2:
        return Snake("Sally", "green")

my_animal = make_animal(1)
my_animal.speak()
my_animal.move()

my_animal = make_animal(2)
my_animal.speak()
my_animal.move()
```

If we run that, we will see the following output:

```
Woof
Run
Hisssss
Slither
```

Notice how two of the same calls to `my_aniimal.speak()` result in two different code
behaviors! This is polymorphism in action. Also notice how our code is calling `speak()`
and `move()`. It is operating at a higher level of abstraction. The implementation
details are handled by the derived classes.

For more information and examples of inheritance and polymorphism, take a look
at [this](https://overiq.com/python-101/inheritance-and-polymorphism-in-python/).


# How do we modify our TicTacToe program?

Think about how to apply this to our TicTacToe and Connect 4 games.

We can use inheritance and polymorphism to represent both of our games.
Every step in our *higher* abstraction pseudo code can be represented
with polymorphic code. As a result, once you set up the proper game,
the existing code will execute the appropriate game methods for you.

# What level of abstraction should I program at to begin with?

This is a hard question to answer. With this TicTacToe example, knowing that
your friends will request more games ahead of time would have allowed you
to plan the level of abstraction accordingly. This isn't always easy to do
in practice. Many times, the requirements change quickly and with short notice.

It's OK to change the level of abstraction organically, like we are doing with
this assignment. Going back to existing code and redesigning it to better
function with new requirements is called *code refactoring*. This is an important
part of keeping a clean, easy to use, and bug free code base.


# Assignment

## 1. Copy your TicTacToe assignment implementation into `./work` and rename it to `<your_name>_connect4.py`

## 1. Based on your TicTacToe code, determine the class inheritance structure
Hint: The implementation code you wrote for TicTacToe will have to be placed
in the *derived* classes associated with TicTacToe

## 4. Modify your `GameLoop` implementation to operate with polymorphic code

## 2. As the first step of the program, have the user specify which game they want to play

## 3. Create a new set of derived classes to implement Connect 4

## 4. After you finish your Connect 4 implementation, copy and answer the following questions in your Python implementation file:

If somebody later came to you and asked to implement the game of Checkers, what
general code changes would you require?

What derived classes would you need for the Checkers game?

How would the derived Checkers class implement the game board?

What would a player move look like? (ie. What does a player need to specify to consitute a move?)

How would you implement the victory condition check?

