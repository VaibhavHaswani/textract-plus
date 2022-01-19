.. NOTES FOR CREATING A RELEASE:
..
..   * bumpversion {major|minor|patch}
..   * git push && git push --tags
..   * twine upload -r textract dist/*
..   * convert into release https://github.com/deanmalmgren/textract/releases

textract-plus
=============

Extract text from any document with more power and a more wide extension scope. No more muss. No more fuss.

`Full documentation <http://textract.readthedocs.org>`__.

|Build Status| |Version| |Downloads| |Test Coverage| |Documentation Status|
|Updates| |Stars| |Forks|

.. |Build Status| image:: https://travis-ci.org/deanmalmgren/textract.svg?branch=master
   :target: https://travis-ci.org/deanmalmgren/textract

.. |Version| image:: https://img.shields.io/pypi/v/textract.svg
   :target: https://warehouse.python.org/project/textract/

.. |Downloads| image:: https://img.shields.io/pypi/dm/textract.svg
   :target: https://warehouse.python.org/project/textract/

.. |Test Coverage| image:: https://coveralls.io/repos/github/deanmalmgren/textract/badge.svg?branch=master
    :target: https://coveralls.io/github/deanmalmgren/textract?branch=master

.. |Documentation Status| image:: https://readthedocs.org/projects/textract/badge/?version=latest
   :target: https://readthedocs.org/projects/textract/?badge=latest

.. |Updates| image:: https://pyup.io/repos/github/deanmalmgren/textract/shield.svg
    :target: https://pyup.io/repos/github/deanmalmgren/textract/

.. |Stars| image:: https://img.shields.io/github/stars/deanmalmgren/textract.svg
    :target: https://github.com/deanmalmgren/textract/stargazers

.. |Forks| image:: https://img.shields.io/github/forks/deanmalmgren/textract.svg
    :target: https://github.com/deanmalmgren/textract/network

Currently supporting extensions
--------------------------------

Textract Plus supports a growing and extended list of file types for text extraction than textract. If
you don't see your favorite file type here, Please recommend other
file types by either mentioning them on the `issue tracker
<https://github.com/VaibhavHaswani/textract-plus>`_ or by
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


* Extended support *

* ``.dotx`` via `docx2python`_

* ``.docm`` via `docx2python`_

* ``.pptm`` via `python-pptx`_

.. this is a list of extended packages by textract plus
.. _docx2python: https://github.com/ShayHill/docx2python
