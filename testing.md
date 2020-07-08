This document explains how the project was tested. Please see full [README.md file](        LINK!!!!!!!!!!!!!    ).

# Automated testing

## Validators

* [W3 HTML validator](https://validator.w3.org/) was used on all the html files. Since the templating language was used in the html files, and the W3 HTML validators does not recognise them, I used page source code instead. I made sure to get the source code in all the possible states of the webpage (e.g product with coulours vs without colours, message displayed, product on homepage marked to be on wishlist etc.). A few errors were caught this way: nested a tags, unclosed p elements and repeated id's. These mistakes were corrected and now the HTML code validates without errors. 

* [W3 CSS validator](https://jigsaw.w3.org/css-validator/) was used to check all the CSS files. No errors were found. 