# HTML2PDF

A script to convert an HTML file to PDF.
A4 size as default.

## Requirements
- Python 3.x.
- selenium.
- chromedriver.

## How to
First of all, you have the options to:
- Create a PDF from a static HTML or webpage of your choice. IF so, use the files ending with `WithoutParameters`.
- Create a PDF from a HTML programmatically, using  parameters of your choice. If so, use the files ending with `WithParameters`.

1. Make your HTML changes on the `index.html` and `style.css` files of your choice. Per default, is set-up so every div with the `page` class will be a new page (of course).
2. Change the inputFle variable inside the HTML2PDF.py file of your choice to the full path of your HTML file, or to an online website if you wish.
3. Run the script by executing `python HTML2PDF.py` of your choice.
4. Your file will be called something like `generatedPDF-Parameters.pdf` (Depeding if you chose with or without parameters), or a name of your choice, by setting it up using the `output` argument on the `saveHtmlAsPDF` function.

## To do
1. Add option to use command line arguments when running HTML2PDF.py.