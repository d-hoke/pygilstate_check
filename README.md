pygilstate_check
================

C-api to check whether the current thread has acquired the GIL or not (PyGILState_Check) for python 2

This project simply adds a way to determine whether the GIL is being
held by a thread in a convenient way. It is mostly a backport of
Python 3.4's c-api function `PyGILState_Check`
https://docs.python.org/3/c-api/init.html?highlight=pygilstate_check#c.PyGILState_Check
It can be useful in debugging deadlocks/crashes in python-c api usage
by checking whether the GIL is acquired or not where expected.


Code Example
============

For example in calling c code

```
if (PyGILState_Check2()) {
   /* I have the GIL */
} else {
  /* I do not have the GIL */
}
```


Motivation
==========

The motivation for this was debuggung PySide deadlocks and segfaults.
PySide nwould sometimes not release the GIL at C++ boundary where it
should (i.e. C++ code would be dealing with locks and out-of-order
acquisition of GIL and C++ QMutex would cause deadlocks)

With this project, you can simply load the dynamic library in gdb and
add a conditional breakpoint and ascertain which part of code is not
correctly release/acquiring the GIL.


Installation
============

Clone the repository and then do the usual python install process:

```
python setup.py install
```

You need to have a working compiler setup to be able to install it.

## API Reference

```
/* Return 1 if the current thread is holding the GIL and 0 otherwise */
int PyGILState_Check2(void);
```

Using the python module from python is pointless because you already
know that you have the GIL.


Tests
=====

The following python commands will execute a simple test checking
whether the correct result is returned.

```
import pygilstate_check
pygilstate_check.test()
```


Contributors
============

Pankaj Pandey.
Contribute somthing to see your name here :)


License
=======

The code and other files are licensed under the MIT license
which can be seen in the LICENSE.txt file or from the url:
http://opensource.org/licenses/MIT
