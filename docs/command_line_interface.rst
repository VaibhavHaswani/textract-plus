.. _command-line-interface:

Command line interface
======================

textract-plus
--------------

.. argparse::
   :module: textractplus.cli
   :func: get_parser
   :prog: textractplus

.. note:: 

    To make the command line interface as usable as possible,
    autocompletion of available options with textractplus is enabled by
    @kislyuk's amazing `argcomplete
    <https://github.com/kislyuk/argcomplete>`_ package.  Follow
    instructions to `enable global autocomplete
    <https://github.com/kislyuk/argcomplete#activating-global-completion>`_
    and you should be all set. As an example, this is also configured
    in the `virtual machine provisioning for this project
    <https://github.com/VaibhavHaswani/textract-plus/blob/master/provision/development.sh#L17>`_.
