moos
====

Mississippi OpenElections OCR Scanner

An adaptation of [craiget](https://github.com/craiget)'s python script
to automate scanning a table with tesseract available
[on his blog](http://craiget.com/extracting-table-data-from-pdfs-with-ocr/).
I am in the process of changing it to work with Wand instead of PIL,
and call tesseract directly, in order to suit my own needs of speeding up
data entry at the [openelections-data-ms project](https://github.com/openelections/openelections-data-ms).

With the `package` branch, I am making the original script into something
that isn't as fussy as the original script, which requires being run in
the same directory as the file, and requires a "working" directory there
as well.
