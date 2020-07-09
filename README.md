# [ColourPerfect](https://colourperfect.herokuapp.com/)


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

### Wireframes

Wireframes for the homepage: 

![mobile](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/wireframes/mobile-home.png)
![tablet](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/wireframes/tablet-home.png)
![desktop](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/wireframes/desktop-home.png)

All the wireframes can be found in the [wireframes folder](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/tree/master/wireframes).

#### Differences between wireframes and the application

* Navbar links and buttons - in wireframes login/logout and register/your account are navigation links, however in the project these actions are available in user drop down menu situated next to the basket and wishlist. This is a better solution because it allows to keep all the actions connected to the user's account in one place and the navigation links are only connected to the specific content pages.

* Navbar layout - in wireframes this is spanned across two rows in desktop view, however eventually I chose to have everything in one row as there was enough space to do this and there was no need to make the navbar take more space. In the mobile view, the basket is in the bottom row together with search field(this expands when clicked on), wishlist button and user account drop-down. Again, the space was enough so I decided this was a better user experience where all those actions are next to each other. 

* Beauty test - all the questions are displayed at once, instead one by one, with next button, like in the wireframes. There are only 5 questions, and the top content is not as big as expected so it felt like a better user experience to display all the questions at once. 


## Features

All the features were added to enhance the UX and make the website easy to use and intuitive to move around. 

### Existing Features

* **Fixed navbar**

  This element appears on all the pages. It contains a clickable logo that takes user to the homepage, and links to the remaining pages, as well as a search box, where user can search for products. The navbar is expanded on large devices and on smaller ones it is collapsed, however search box, account, basket and wishlist links are still visible. When the hamburger menu is clicked a the remaining navbar links appear. When a user clicks a link the navbar collapses back. If there are some items in the basket - a badge displaying basket total appears on the basket icon. 

* **Footer**

  Like navbar, this element also appears on all the pages. It contains a Delivery&Returns link, which takes user to the delivery section of the about page. Apart from that, there is a clickable customer service number, and social icon links (these only link to social media main pages, as the shop is no real and does not have any social pages). The footer stick to the bottom of the page regardless the size of the page and the size of the footer itself (which changes on different devices).

#### Login&Authentication system

  Django Allauth was used to provide login and authentication functionality to the project. 

* **Registration**

  - When 'Register' link is clicked on the navbar, a user is taken to the registration form page, where they can complete registration form, or click a link to the login page instead
  - When the registration form is submitted and it's valid, a user receives an email with verification link, otherwise - an error message shows informing user why the form has not been submitted
  - User is automatically logged in when registration is successful

* **Login**

- When 'Login' link is clicked on the navbar, a user is taken to the login form page, where they can complete login form, or click a link to the registration page instead; they can also login with their Google account or request password reset
- If login details are correct, a user is logged in, otherwise error message appears
- User can reset their password clicking 'Forgot password' button
- 'Sign in with Google' buttons allows to sign in with Google account, without creating an account in the application

* **Logout**

- When logout link is clicked, a modal appears informing about the email address the user is currently logged in and asking for confirmation to log out, if it is confirmed - the user is logged out

User can also change their password and manage their emails from their profile view. 

#### Home page

* Right below the hero image there are 3 important features listed, tohether with the link to the beauty test so user can quickly understand the main focus on the colour matching
* If user is logged in, a welcome message appears on the homepage, right below the hero image
* There are 3 random products in matching colours for each season displayed
* When a user hovers over a product image, the product name apparea, and if they hover over the colour dot - colour name is displayed
* When suggested product card is clicked, user is taken to the product page
* All categories and brands are displayed in alphabetical order for easy access - when clicked they take user to products filtered by the category or brand


#### Search page

* This page can be accessed by clicking on a brand or category link, or searching for a phrase using th searchbox (or of course by typing a correct ULR)
* The header informs what the results are for (brand, category or the searched term)
* Products are displayed as cards and when clicked, take user to the product page
* If user is logged in, products that are on their wishlist (regardless the colour) are marked with a little heart icon that takes user to their wishlist
* If product image link is broken, a replacement image is displayed instead
* If there are no products found, there is an information about it displayed

#### Beauty type test

* The page describes shortly what beauty types are and offers 5 quiz questions
* If all the questions are answered, and submit button clicked - user is taken to the result page

* **Result page**

  - Matching season tohether with a picture is displayed
  - Season description and radom 12 matching colours are displayed
  - 3 random products in matching colours are displayed, when clicked, they take user to the product page

#### About page 

* The page gives a quick information about the main focus of the website 
* Categories and Brands links are available from here as well so that user can get to the products quickly
* Beauty types are shortly described and user is encouraged to take the beauty test; there is a button that takes them directly to that page
* Delivery, returns and contact information is displayed

#### Profile/Your account

* This page is only available to authenticated users
* This page contains delivery details form - if the details were previously saved, they are displayed in the form
* The details can be updated by completing/changing the form information and clicking 'Update' button
* Additionally, 3 most recent (if there are any) orders are displayed, and when user clicks on them, they are expanded and show the order details
* User can click 'Full order history' to see all the past orders - they are displayed in the same way as recent orders - as expandable rows
* Finally, user account details are displayed together with 'Change password' and 'Manage your emails' buttons

#### Basket

* Basket page is availabe for both, authenticated and not authenticated users, as it is possible to checkout as a guest
* For authenticated user, basket content is saved in the database, so that they can access it even after closing their browser or accessing the webiste from different device
* On the top of the page basket total is displayed, right next to the checkout button. This is repeated also at the bottom for the ease of use
* Each item image and name (which is also a link to the product page) are displayed, together with chosen colour (if product has colours)
* User can update the quantit of each product, or delete it completely from the basket - total and subtotal is automatically updated if this happens
* Checkout button takes a user to the checkout page

#### Checkout 

* This page contains checkout form, which is prefilled if the user saved this information before and is logged in, otherwise the form is empty
* If user is logged in, there is a possibility to save their details
* If user is not logged in - log in and register links are displayed
* 'Payment' field has to be completed in order to process Stripe payment. Since the Stripe functionality is only for testing, only 4242 4242 4242 4242 card number works. 
* From this page user can go back to their basket if they need to change somethin
* User is informed how much their card will be charged
* If a user clicks 'Confirm Order&Pay' button, the payment is done and user is redirected to the checkout success page 
