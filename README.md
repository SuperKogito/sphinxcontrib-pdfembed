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





### Advanced parameters for embedding PDF files

You can embed a PDF document using the  ```:pdfembed:``` command and passing the following arguments: `src`, `height`, `width`, `align`

**Example:** ```    :pdfembed:`src:_static/path_to_pdf.pdf, height:1600, width:1300, align:middle` ```

The `src` argument can be extended to exactly specify what to display (a named destination or specific page), and how to display it (using such characteristics as a specific view, scroll-bars, bookmarks, annotations, or highlighting). These parameters for `src` are supported by most browsers, and can be used when opening PDF documents.

#### Parameters

| Syntax                                                                                                                                                                                                          |      Description                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ```page=pagenum```                                                                                                                                                                                              | Specifies a numbered page in the document, using an integer value. The document’s first page has a `pagenum` value of 1.                                              |
| ```comment=commentID```                                                                                                                                                                                         | Specifies a comment on a given `page` in the PDF document. Use the page command before this command. For example:<br> `#page=1&comment=452fde0e-fd22-457c-84aa-2cf5bed5a349` |
| ```zoom=scale```<br>```zoom=scale,left,top```                                                                                                                                                                   | Sets the zoom and scroll factors, using float or integer values. For example, a scale value of 100 indicates a zoom value of 100%. <br> Scroll values left and top are in a coordinate system where 0,0 represents the top left corner of the visible page, regardless of document rotation.|
| ```view=Fit```<br>```view=FitH```<br>```view=FitH,top```<br>```view=FitV```<br>```view=FitV,left```<br>```view=FitB```<br>```view=FitBH```<br>```view=FitBH,top```<br>```view=FitBV```<br>```view=FitBV,left``` | Set the view of the displayed page, using the keyword values defined in the PDF language specification. For more information, see the PDF Reference.Scroll values left and top are floats or integers in a coordinate system where 0,0 represents the top left corner of the visible page, regardless of document rotation. <br>*-Use the page command before this command.* <br><br>**Note:** This parameter is not supported on the command line |
| ```viewrect=left,top,wd,ht```                                                                                                                                                                                   | Sets the view rectangle using float or integer values in a coordinate system where 0,0 represents the top left corner of the visible page, regardless of document rotation.<br> *- Use the page command before this command* <br><br> **Note:** This parameter is not supported on the command line. |
| ```pagemode=bookmarks```<br>```pagemode=thumbs```<br>```pagemode=none (default)```                                                                                                                              | Displays bookmarks or thumbnails.                      |
| ```scrollbar=1|0```                                                                                                                                                                                             | Turns scrollbars on or off.                            |
| ```search=wordList```                                                                                                                                                                                           | Opens the Search panel and performs a search for any of the words in the specified word list. The first matching word is highlighted in the document.<br><br> The words must be enclosed in quotation marks and separated by spaces. For example: `#search="word1 word2"` <br><br>You can search only for single words. You cannot search for a string of words.   |
| ```toolbar=1|0```                                                                                                                                                                                               | Turns the toolbar on or off.                           |
| ```statusbar=1|0```                                                                                                                                                                                             | Turns the status bar on or off.                        |
| ```messages=1|0```                                                                                                                                                                                              | Turns the document message bar on or off.              |
| ```navpanes=1|0```                                                                                                                                                                                              | Turns the navigation panes and tabs on or off.         |
| ```highlight=lt,rt,top,btm```                                                                                                                                                                                   | Highlights a specified rectangle on the displayed page. Use the `page` command before this command.<br><br>The rectangle values are integers in a coordinate system where 0,0 represents the top left corner of the visible page, regardless of document rotation.|


#### Specifying parameters in a `src` argument

- You can specify multiple parameters in a single `src`. Separate each parameter with either an ampersand (&) or a pound (#) character. Actions are processed and executed from left to right as they appear in the `src`.
- Because all specified actions are executed, it is possible that later actions will override the effects of previous actions, so it is important to use the correct order. For example, page actions should appear before zoom actions.
- Commands are not case sensitive except for the value of a named destination. There can be no spaces in the `src`.

#### `src` examples
  ```
  _static/pdf_file.pdf#Chapter6
  _static/pdf_file.pdf#page=3
  _static/pdf_file.pdf#page=3&zoom=200,250,100
  _static/pdf_file.pdf#zoom=50
  _static/pdf_file.pdf#page=72&view=fitH,100
  _static/pdf_file.pdf#pagemode=none
  _static/pdf_file.pdf#pagemode=bookmarks&page=2
  _static/pdf_file.pdf#page=3&pagemode=thumbs
  _static/pdf_file.pdf#page=1&comment=452fde0e-fd22-457c-84aa-2cf5bed5a349
  ```

#### `src` limitations

-  Only one digit following a decimal point is retained for float values.
-  Individual parameters, together with their values (separated by & or #), can be no greater then 32 characters in length.
-  You cannot use the reserved characters =, #, and &. There is no way to escape these special characters.
-  If you turn bookmarks off using a URL parameter when a document had previously been saved with bookmarks on, the bookmark scrollbars are displayed at first, and only disappear once Acrobat obtains enough streamed information to render the full page.

## Remarks
- More parameters can be found under [Parameters for Opening PDF Files](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/pdf_open_parameters.pdf).
* Please keep in mind that the pdf should be placed under `_/static` in order to be copied to the build folder to be seen by the HTML files.


## credits & sources
- [Parameters for Opening PDF Files by Adobe](https://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/pdf_open_parameters.pdf)
- [Sphinx-docs](http://www.sphinx-doc.org/en/master/)

## History
`0.1`: First public release.
