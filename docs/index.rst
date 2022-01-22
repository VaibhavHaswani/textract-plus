
textract Plus
================================

As undesirable as it might be, more often than not there is extremely
useful information embedded in Word documents, PowerPoint
presentations, PDFs, etc---so-called "dark data"---that would be
valuable for further textual analysis and visualization. While
:ref:`several packages <supporting>` exist for extracting content from
each of these formats on their own, this package provides a single
interface for extracting content from any type of file, without any
irrelevant markup.

This package provides two primary facilities for doing this, the
:ref:`command line interface <command-line-interface>`

.. code-block:: bash

    textractplus path/to/file.extension

or the :ref:`python package <python-package>`

.. code-block:: python

    # some python file
    import textractplus as tp
    text = tp.process("path/to/file.extension")

.. _supporting:

Currently supporting
--------------------

textract-plus supports a growing list of file types for text extraction. If
you don't see your favorite file type here, Please recommend other
file types by either mentioning them on the `issue tracker
<https://github.com/VaibhavHaswani/textract-plus/issues>`_ or by
:ref:`contributing a pull request <contributing>`.


* ``.csv`` via python builtins

* ``.tsv`` and ``.tab`` via python builtins

* ``.doc`` via `antiword`_

* ``.docx`` via `python-docx2txt`_

* ``.eml`` via python builtins

* ``.epub`` via `ebooklib`_

* ``.gif`` via `tesseract-ocr`_

* ``.jpg`` and ``.jpeg`` via `tesseract-ocr`_

* ``.json`` via python builtins

* ``.html`` and ``.htm`` via `beautifulsoup4`_

* ``.mp3`` via `sox`_, `SpeechRecognition`_, and `pocketsphinx`_

* ``.msg`` via `msg-extractor`_

* ``.odt`` via python builtins

* ``.ogg`` via `sox`_, `SpeechRecognition`_, and `pocketsphinx`_

* ``.pdf`` via `pdftotext`_ (default) or `pdfminer.six`_

* ``.png`` via `tesseract-ocr`_

* ``.pptx`` via `python-pptx`_

* ``.ps`` via `ps2ascii`_

* ``.rtf`` via `unrtf`_

* ``.tiff`` and ``.tif`` via `tesseract-ocr`_

* ``.txt`` via python builtins

* ``.wav`` via `SpeechRecognition`_ and `pocketsphinx`_

* ``.xlsx`` via `xlrd <https://pypi.python.org/pypi/xlrd>`_

* ``.xls`` via `xlrd <https://pypi.python.org/pypi/xlrd>`_


.. this is a list of all the packages that textract uses for extraction
.. _antiword: http://www.winfield.demon.nl/
.. _beautifulsoup4: http://beautiful-soup-4.readthedocs.org/en/latest/
.. _ebooklib: https://github.com/aerkalov/ebooklib
.. _msg-extractor: https://github.com/mattgwwalker/msg-extractor
.. _pdfminer.six: https://github.com/goulu/pdfminer
.. _pdftotext: http://poppler.freedesktop.org/
.. _pocketsphinx: https://github.com/cmusphinx/pocketsphinx/
.. _ps2ascii: https://www.ghostscript.com/doc/current/Use.htm
.. _python-docx2txt: https://github.com/ankushshah89/python-docx2txt
.. _python-pptx: https://python-pptx.readthedocs.org/en/latest/
.. _SpeechRecognition: https://pypi.python.org/pypi/SpeechRecognition/
.. _sox: http://sox.sourceforge.net/
.. _tesseract-ocr: https://code.google.com/p/tesseract-ocr/
.. _unrtf: http://www.gnu.org/software/unrtf/


Extended with Textract Plus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* ``.dotx`` via `docx2python`_

* ``.docm`` via `docx2python`_

* ``.pptm`` via `python-pptx`_

.. this is a list of extended packages by textract plus
.. _docx2python: https://github.com/ShayHill/docx2python



.. _related-projects:

Related projects
----------------

Of course, textract-plus isn't the first project with the aim to provide a
simple interface for extracting text from any document. But this is,
to the best of my knowledge, the only project that is written in
python (a language commonly chosen by the natural language processing
community) and is :ref:`method agnostic about how content is extracted
<contributing>`. I'm sure that there are other similar projects out
there, but here is a small sample of similar projects:

* `Apache Tika <http://tika.apache.org/>`_ has `very similar, if not
  identical, aims as textract-plus
  <https://github.com/VaibhavHaswani/textract-plus/issues/12>`_ and has
  impressive coverage of a wide range of file formats. It is written
  in java.

* `textract (node.js) <https://github.com/dbashford/textract>`_ has
  similar aims as this textract-plus package (including an identical name!
  great minds...). It is written in node.js.

* `pandoc <http://johnmacfarlane.net/pandoc/>`_ is intended to be a
  document conversion tool (a much more difficult task!), but it does have
  `the ability to convert to plain text
  <http://johnmacfarlane.net/pandoc/demos.html>`_. It is written in
  Haskell.


Contents:

.. toctree::
   :maxdepth: 2

   command_line_interface
   python_package
   installation
   contributing
   changelog


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
