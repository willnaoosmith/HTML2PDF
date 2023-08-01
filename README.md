# HTML2PDF

A script to convert an HTML file to PDF.
A4 size as default.

## Requirements
- Python 3.x
- selenium
- chromedriver

## How to
1. Make your HTML changes on the `index.html` and `style.css` files as you wish. Per default, is set-up so every div with the `page` class will be a new page (of course).
2. Change the inputFle variable inside the HTML2PDF.py file to the full path of your HTML file, or to an online website if you wish.
3. Run the script by executing `python HTML2PDF.py`
4. Your file will be called `generatedPDF.pdf`, or a name of your choice, by setting it up using the `output` argument on the `saveHtmlAsPDF` function.

## To do
1. Add option to use command line arguments when running HTML2PDF.py.