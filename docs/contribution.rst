How to contribute
=================

Eliza is currently in active development and welcomes code improvements and bug fixes.
For those of your interested, providing documentation to the lesser know parts would be equally awesome!

Pull down the source::

    $ git clone git@github.com:redvox/Eliza.git

.. note::

    All code contributions should have adequate tests. If you add something, please add a test to our test-suite.

    To run the tests simply run the following command from the root directory::

    $ ./run-tests.sh

Style
^^^^^

If you decide to contribute code please follow naming conventions and style guides the code currently complies too.

When in doubt, be safe, follow `PEP-8. <http://www.python.org/dev/peps/pep-0008/>`_

Documentation
^^^^^^^^^^^^^

Contributing to documentation is as simple as editing the specified file in the *docs* directory of the source. We welcome all code improvements.


We use Sphinx for building our documentation. That can be obtained `here <http://sphinx-doc.org/>`_.

.. note::

    To view the docs as html, use the Makefile includes in the /docs directory. Simply run the following command::

    $ ./docs/build.sh


Reporting Issues
^^^^^^^^^^^^^^^^
This is most important of all, if there are issues please let us know. So we can improve Eliza.
If you don't report it, we probably won't fix it.
