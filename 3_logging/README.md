# Don't reinvent the wheel
Using basic building blocks, you can build up your program with more building
blocks to do more and more complex things. In many cases, you implement these
building blocks yourself.

However, there are some things that almost every program needs.

For example, every program benefits from a good logging mechanism.
Logging is important to show internal program state and decisions,
which in turn allows programmers to track program behavior and bugs.

Communication over a network is also useful for client and server
programs. You can have different APIs between programs that you
*would* have to implement. But interacting with the kernel to send
network traffic is the same everywhere.

It would suck to constantly rewrite that same logging or network mechanism
every time you made a new program. So, people created ways of reusing big
chunks of code.


# Modules and libraries
To that end, people create modules or libraries to allow programs to easily
import a bunch of useful code.

> C++ uses libraries and linking. Python uses modules. Python's
> module's are much easier to install and import. C++ is also getting
> it's own modules with C++20.

So, if you're making a program and you want to have a good logging
mechanism, you simply import the `logging` module and begin using
it in the code.

Modules and libraries allow you to focus on the interesting part
of the program. There are a lot of very useful modules. If you find one
that meets the requirements for what you're trying to do, it makes
sense to use it to make your life easier.


# Logging
I can just use `print()` to see what's happening, right?

![No](https://media.giphy.com/media/12XMGIWtrHBl5e/giphy.gif)

`print()`s work OK for small test programs. They are easy to use and you can
quickly sprinkle them everywhere to see what your program is doing. In large
scale production code though, they aren't viable. Here's why.

Log messages need to show the date and time they were logged. Your program may
be running for a long time. If a customer calls with an issue, you will need to
view the logs at some specific time to determine what went wrong.

Log messages need to print the file and line number they were invoked from.
This is required to track down the exact piece of code that logged the
message. Then, you can view the code around it to determine the conditions
that triggered the logging.

Log messages need to have different levels of log severity. The standard levels
are `DEBUG` (sometimes multiple levels), `INFO`, `WARNING`, and `ERROR`.
These severity levels make it easier to determine if and when an error occurred.

Programmers also need to be able to set the level of logging they want. Normally,
you only want to log `INFO`, `WARNING`, and `ERROR`. These messages will help
you determine important events and errors that the program encounters. `DEBUG`
logging shows verbose and detailed internal program state. By default, you don't
log at that level, because you don't want to spam the log file when there's
nothing wrong. There's also a performance penalty for logging more things to a
file, because IO is generally slow.

However, if a customer experiences an issue, you'll want to enable `DEBUG` logging.
This can show you detailed internal program state, which might make it easier
to determine the customer's issue or if there's a bug in the code.

You can hack all this information manually into your `print()` function
call, but you'd be reinventing the wheel. The Python logging module does all of
this for us. Yay!

In closing, use `print()` only for output you want the user to see.


# The Python logging module

This [tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial) covers
it pretty well.

A quick read of the sections before the Advanced Logging Tutorial section will
suffice for this assignment.


# Assignment
The file for this assignment has some buggy Python code. Use debug logging
to log the program state at various points in the code to determine what
the bugs are.

## 1. copy the logging_bugs.py template file into `./work` and rename it to `<your_name>_logging_bugs.py`

## 2. Set up logging to print the date, the time, the filename, and the log level

And then your actual log message after that.

## 3. Add logging to the program to demonstrate the bugs

If you find some bugs just by looking at the code, that's great! Put in a
log line that would be helpful for debugging anyways.

Explain the bug with in code comments, or as comments in your pull request.

## 4. Once you get the program to succeed, turn off `DEBUG` logging to avoid cluttering the program's output

Turning on and off extra logging is really easy with log levels. Imagine having
to go back and delete all the `print()` function calls you sprinkled everywhere
when you're done debugging. Or, adding everything back in if a new bug arises.


