#  sphinxcontrib-pdfembed
This is the code for the sphinxcontrib.pdfembed extension, which embedds PDF files in the sphinx generated webpages.

## Installation

   ``pip install git+git://github.com/SuperKogito/sphinxcontrib-pdfembed``

## Configuration
Add ``'sphinxcontrib.pdfembed'`` to the ``extensions`` list in ``conf.py``:

    extensions = [ 'sphinxcontrib.pdfembed' ]


## Usage
To obfuscate an email address use something like:

    :pdfembed:`src:_static/path_to_pdf.pdf, height:1600, width:1300, align:middle`

* Please keep in mind that the pdf should be placed under _/static in order to be copied to the build folder to be seen by the HTML files.
## History
0.1: First public release.
