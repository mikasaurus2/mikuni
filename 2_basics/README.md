# Programming Basics
All programs are composed from basic building blocks. Some programs do get
quite complex, but they are simply using more building blocks to layer
complexity on previous building blocks.

All programs boil down to basic constructs like variables, loops, functions,
and classes, regardless of the programming language.

As you go through this exercise, try to understand how these are
used, as opposed to just learning the syntax. This promotes thinking
about code conceptually, and allows you to transfer your coding skills
to any language you choose to learn.

Different languages have different syntax rules and learning the syntax is
just a matter of brain muscle memory.

## Variables
These simply store data. They can be different types, like integers (numbers)
or strings. Some languages require that you specify the type (like C++). Other
languages deduce the type for you (like Python).

## Loops
Loops are used to repeat a block of code. Conceptually speaking, you want
to repeat a set of commands until a certain condition is met.

Say you have some code that checks if a file is present, and gives you
a yes or no answer. If you want to make sure the file is there before
proceeding, you can use a loop to execute your file checking code
until it tells you the file is there.

In other cases, you may have a list of variables. To go through that list and
view all of them, you need a loop. Looping over a list until you hit the end
like this is also called *iterating*.

## Functions
Functions are intended to execute a specific task or a related group of actions.
After they are defined, they can be called, or invoked, from other parts
of your program. Functions can take parameters, or arguments, to be used
when they execute their code. They can also return variables or values.

As an example, consider a function that converts from celsius to fahrenheit.
It might be called something like `CelsiusToFahrenheit`. It takes an integer 
as a parameter (the fahrenheit) and spits out another integer (the celsius).

The benefit here is that you only have to write the conversion code once.
Then, any time you need to convert from celsius to fahrenheit, you simply
invoke the function.

This promotes code reusability, clarity, and maintainability. Imagine if,
instead of using that function, you copied the conversion code to every
location that it was needed. If you later discovered a bug in your calculation,
you'd have to change it in every location you have a copy of the calculation
code. If you used a function, on the other hand, you'd only have to change it
inside the function. All the code that invokes the function would benefit from
that bug fix.

## Classes
Classes are an important part of Object Oriented Programming. The class
encapsulates some entity or behavior. Classes contain variables
and methods, which are simply class specific functions. These variables
and methods form the attributes and actions of the thing the
class is representing.

Classes themselves are only blueprints though. In order to actually
have the thing the class represents, you must create an Object.
Objects are instances of a class. A class is a template for creating
objects.

Those definitions are pretty vague, so here are some concrete examples.

Let's say you're programming some video game where a user interacts with
a pet dog. You'll have to program that dog with all the dog-like
behavior it'll need. In that case, you'd create a Dog class.

This serves a couple of purposes. One of which is code organization.
All the dog behavior code will live in the Dog class. If other
programmers need to modify the dog's behavior, they know to look
for and to modify the Dog class.

Let's say you also want the player to have multiple dogs. Having
a Dog class makes this easy because you can simply create multiple
dog objects! Their properties would all be the same, but the values
of those properties could be different. In other words, each dog
has a `name`, but their names are different.

Another benefit is the encapsulation itself. Encapsulation means
that the code implementing the Dog class is "hidden" from other,
non-related code. Let's say the player presses some button that
makes a dog bark. You, as the programmer, would bind that
button press to invoke the Dog member function `Bark()`. You also
have to implement that `Bark()` member function by writing code
to interact with whatever sound system the game is using. In this
case, the button pressing code only invokes `Bark()` and is unaware
of any nuances or complexities of the sound system. In the future,
if there's some update to the sound system code, you'd only have
to change that inside the `Bark()` implementation. Everything that
calls `Bark()` would *not* have to be changed.

In this way, encapsulation provides an *interface* to the object
for other pieces of code to use. By doing that, the implementation
can change without breaking those other pieces of code, as long as
the interface is respected. This is extremely important in large
scale software projects.

# Program style and conventions

Large code bases follow style and naming convention rules. The
"correct" style is decided by the organization or coding community
based on their consensus.

The main benefit of maintaining consistent style is code readability
and implementation consistency.

It helps people understand code more easily. If a bug fix or feature requires you to
dive into someone else's code, you'll have an easier time groking it if the
code is readable and the syntax is familiar.

The style guidelines can specify which library or module to use when there are
multiple options. This ensures consistent code behavior and prevents bugs from
popping up in seemingly identical code that just so happens to use a different
underlying module.

For these assignments, let's just follow the basic Python naming convention
guide below. Having a consistent variable, function, and class naming style
will make it easier to read and do code reviews.

[naming conventions](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)

There are more comprehensive style guidelines for Python, but I don't think
it's worth following those at this point. After all, these are small, non
production code assignments. It's not worth slowing down the pace to nitpick on
style conventions. Use your best judgement in making your code clean, and we'll
update this later if we need to.


# Assignment
The goal here is to get familiar with Python's basic constructs.

## 1. copy the basics.py template file into `./work` and rename it to `<your_name>_basics.py`
## 2. ensure you have the python3 interpreter
Run `python3 <your_name>_basics.py`

[Why we use Python 3](http://www.youtube.com/watch?v=xOrgLj9lOwk&t=82)

## 3. go through the python file and fill in the coding exercises
Use any online resources as necessary.

Here are some resources. You don't have to read these all before you start. Use
them as a reference if you don't understand a specific concept.

1. [overiq python tutorial](https://overiq.com/python-101/)
2. [learnpython.org](https://www.learnpython.org/)
3. [pythonbasics.org](https://pythonbasics.org/)
4. [w3schools Python reference](https://www.w3schools.com/Python/python_intro.asp)
5. [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

