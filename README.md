[ColourPerfect](https://colourperfect.herokuapp.com/)


ColourPerfect is a unique online make-up shop that offers products that are just perfect for your beauty type! Take our test to find out which beauty type you are - spring, summer, autumn or maybe winter? Search for make-up product and we will tell you which shades are perfect match for you and make you look just fabulous! Then just pop them in your shopping cart and voila, you have your perfect makeup delivered to you in no time!

#### External user’s goal:

The external user's goal is to find out which shades of makeup fit the best and be able to easily purchase them. 

#### Site owner's goal:

The site owner's goal is to sell make-up products. 

 
## UX

The majority of users are expected to be women who want to find and purchase make-up products that will look best on them.   

### User stories

* As a user I want to know what the website offers as soon as I get there so I don't have to waste time if I am not interested in it
* As a user I want to quickly find out what the beauty types are so that I can decide if this something I am interested in
* As a user I want to quickly find out my beauty type so that I can see what shades are good for me
* As a user I want to have a search bar so that I can search for products I am interested in
* As a user I want to have a possbility to see products categories and filter by them, so that I can browse sections I am interested in
* As a user I want to have a possbility to see products brands and filter by them, so that I can browse products I am interested in
* As a user I want to be able to add items to my cart so I can purchase them
* As a user I want to be able to register and log in so that my shipping details are saved and I do not need to enter them every time I want to make a purchase
* As a user I want to be able to pay for my order using credit card
* As a user I want to receive a confirmation email when I checkout
* As a user I want to be able to view my order history
* As a user I want to be able to checkout without having an account 
* As a user I want to have a wishlist so that I can save products I do not want to buy right now but might in the future
* As a user I want to be able to quickly find contact details so that I can get in touch with customer service


The page navigation is designed to be intuitive and enable a user to perform required actions quickly and easily. The website offers many ways to view offered products, so that it is easy for user to find what they look for. There are also many suggestions, if the user does not exactly know what they look for. 

The main focus and a quality that distinguishes ColourPerfect from other e-commerce make-up websites, are colours. Therefore logo was designed to be colourful and [Magonia Grove Color Palette](https://www.color-hex.com/color-palette/91838) was used. Also, the first colour from this palette (#fc4f6f) became a theme colour (buttons, footer, links etc are in this colour). The background colour is white so that all the colours are well presented and the main focus is on them. 

### Colour matching

The idea of colour matching to different beauty types comes from the four seasons analysis. According to this theory there are 4 main types of beauty: spring, summer, autumn and winter. Different colours match better with those beauty types. Generally more vivid, and light colours (juicy, fruity colours) are better for the spring type, vivid but dark colours are recommened for autumn types, calmer and dark colours are suggested for winter types, and finally - calmer and light colours (pastels) are good match for the summer type. This is of course very generalised. 

Having this knowledge, I looked into different colour representations (e.g hex, rgb, hsl) to see which would be the best to use in an algorithm that can determine which beauty type is a match for given colour. In a simplified version warm colours are for warm types (spring and autumn) and blue colours are for cold types (winter and summer). However, this is a big simplification, since, for example, blue is considered a cold colour, however some shades can have warmer undertones and look much better on warm beauty types (e.g. marine blue is recommended for the autumn types). For this reason, dividing colours in a simple way, such that those that have bigger red value are warm and those with bigger blue value are cold, would not be sufficient and would return incorrect results, even additionally differentiate lighter colours from darker shades. Therefore, I looked into hsl values and how the colours change when one of the three values is changed. I used [the w3schools hsl page](https://www.w3schools.com/html/html_colors_hsl.asp#:~:text=HSL%20Color%20Values&text=Hue%20is%20a%20degree%20on,100%25%20is%20the%20full%20color.) for that. I noticed that hue value is not a criterion, for the similar reasons why division to cold and warm colours was not sufficient. However, saturation and lightness seemed to be the key values that could be used to determine which of the four categories a colour belongs to. After a bit of experimentation, I noticed that if saturation is very low, the colours are less vivid and would only match winter or summer, depending on their lightness. If the saturations is very high, still the darkest colours would be right for winter, and the lightest - for summer, but the majority of shades will be a match for autumn (darker) and spring (lighter). Based on these observation, I built a simple algorithm that assigns a given colour to one of the 4 seasons, based on its s and l values. 

This is not based on any scientific research, and the colour matching is only a guidance. The treshold values were set by me, based on my experimentation and observations, not any existing formulas, as there aren't any - to the best of my knowledge. As the colour matching is only a suggestion, the algorithm seems to be good enough to suggest suitable colours, and should be sufficient for this project. 