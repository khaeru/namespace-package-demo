Python namespace packages example
*********************************

To use::

    pip install repository_a
    pip install repository_b
    python demo.py

How it works:

The two directories ``repository_a`` and ``repository_b`` would live in separate Git/GitHub repositories.

- Each can be public or private, independently.
- At minimum, ``repository_a`` should be published on PyPI, so it can be installed by anyone.
- ``repository_b`` could be private.

When installed, Python overlays the contents of the two packages in a single directory tree::

    message_data_demo        # installed from repository_a
    ├── __init__.py          #                repository_a
    └── model                #                repository_a
        ├── __init__.py      #                repository_a
        └── transport        # installed from repository_b
            └── __init__.py  #                repository_b

``demo.py`` can thus import from both packages as if they were one, monolithic package. It outputs::

    message_data_demo imported from main package
    message_data_demo.model imported from main package
    message_data_demo.model.transport imported from namespace package

One can create a private package in a new repository, ``repository_c``, like so::

    message_data_demo         # no __init__.py at this level
    ├── model                 # no __init__.py at this level
    │   └── my_private_model
    │       └── __init__.py
    └── setup.py

…install using::

    pip install git+git://github.com/user/repo.git#egg=message_data_demo-my_private_model

…and then make use of both public and private pieces::

    # Items from the main package
    from message_data_demo.tools import foo, bar

    # Items from the private repo/package
    from message_data_demo.model import my_private_model
