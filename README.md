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
* As a user I want to have a possibility to see products categories and filter by them, so that I can browse sections I am interested in
* As a user I want to have a possibility to see products brands and filter by them, so that I can browse products I am interested in
* As a user I want to be able to add items to my cart so I can purchase them
* As a user I want to be able to register and log in so that my shipping details are saved and I do not need to enter them every time I want to make a purchase
* As a user I want to be able to login with my Google account
* As a user I want to be able to pay for my order using credit card
* As a user I want to receive a confirmation email when I checkout
* As a user I want to be able to view my order history
* As a user I want to be able to checkout without having an account 
* As a user I want to have a wishlist so that I can save products I do not want to buy right now but might in the future
* As a user I want to be able to quickly find contact details so that I can get in touch with customer service


The page navigation is designed to be intuitive and enable a user to perform required actions quickly and easily. The website offers many ways to view offered products, so that it is easy for user to find what they look for. There are also many suggestions, if the user does not exactly know what they look for. 

The main focus and a quality that distinguishes ColourPerfect from other e-commerce make-up websites, are colours. Therefore logo was designed to be colourful and [Magonia Grove Color Palette](https://www.color-hex.com/color-palette/91838) was used. Also, the first colour from this palette (#fc4f6f) became a theme colour (buttons, footer, links etc. are in this colour). The background colour is white so that all the colours are well presented and the main focus is on them. 

### Colour matching

The idea of colour matching to different beauty types comes from the four seasons analysis. According to this theory there are 4 main types of beauty: spring, summer, autumn and winter. Different colours match better with those beauty types. Generally more vivid, and light colours (juicy, fruity colours) are better for the spring type, vivid but dark colours are recommended for autumn types, calmer and dark colours are suggested for winter types, and finally - calmer and light colours (pastels) are good match for the summer type. This is of course very generalised. 

Having this knowledge, I looked into different colour representations (e.g. hex, rgb, hsl) to see which would be the best to use in an algorithm that can determine which beauty type is a match for given colour. In a simplified version warm colours are for warm types (spring and autumn) and blue colours are for cold types (winter and summer). However, this is a big simplification, since, for example, blue is considered a cold colour, however some shades can have warmer undertones and look much better on warm beauty types (e.g. marine blue is recommended for the autumn types). For this reason, dividing colours in a simple way, such that those that have bigger red value are warm and those with bigger blue value are cold, would not be sufficient and would return incorrect results, even additionally differentiate lighter colours from darker shades. Therefore, I looked into hsl values and how the colours change when one of the three values is changed. I used [the w3schools hsl page](https://www.w3schools.com/html/html_colors_hsl.asp#:~:text=HSL%20Color%20Values&text=Hue%20is%20a%20degree%20on,100%25%20is%20the%20full%20color.) for that. I noticed that hue value is not a criterion, for the similar reasons why division to cold and warm colours was not sufficient. However, saturation and lightness seemed to be the key values that could be used to determine which of the four categories a colour belongs to. After a bit of experimentation, I noticed that if saturation is very low, the colours are less vivid and would only match winter or summer, depending on their lightness. If the saturations is very high, still the darkest colours would be right for winter, and the lightest - for summer, but the majority of shades will be a match for autumn (darker) and spring (lighter). Based on these observation, I built a simple algorithm that assigns a given colour to one of the 4 seasons, based on its s and l values. 

This is not based on any scientific research, and the colour matching is only a guidance. The threshold values were set by me, based on my experimentation and observations, not any existing formulas, as there aren't any - to the best of my knowledge. As the colour matching is only a suggestion, the algorithm seems to be good enough to suggest suitable colours, and should be sufficient for this project. 

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

  This element appears on all the pages. It contains a clickable logo that takes user to the homepage, and links to the remaining pages, as well as a search box, where user can search for products. The navbar is expanded on large devices and on smaller ones it is collapsed, however search box, account, basket and wishlist links are still visible. When the hamburger menu is clicked the remaining navbar links appear. When a user clicks a link the navbar collapses back. If there are some items in the basket - a badge displaying basket total appears on the basket icon. 

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

* Right below the hero image there are 3 important features listed, together with the link to the beauty test so user can quickly understand the main focus on the colour matching
* If user is logged in, a welcome message appears on the homepage, right below the hero image
* There are 3 random products in matching colours for each season displayed
* When a user hovers over a product image, the product name appears, and if they hover over the colour dot - colour name is displayed
* If user is logged in, products that are on their wishlist (regardless the colour) are marked with a little heart icon that takes user to their wishlist
* When suggested product card is clicked, user is taken to the product page
* All categories and brands are displayed in alphabetical order for easy access - when clicked they take user to products filtered by the category or brand

#### Product page

* From this page product can be added to the wishlist or to the basket
* If a product has colours, they are displayed as the best colours for the matching season
* If there are no matching colours for a season there is a message informing about that and encouraging user to choose a colour anyway.
* If a product has no colours, or no description, an information is displayed
* If a product is added to the basket, a pop up appears with an information what was added, and with 'mini basket' view from where user can go straight to checkout
* Quantity input is read only so that the user cannot type the number, can only use the buttons. The reason for this is defensive design, otherwise additional validators would be necessary, checking if the field was completed properly (only numbers, number within bounds etc.). Since this is not a wholesale and it is expected that the customer will buy one or only a few same items, this solution should be good from the UX point of view. 


#### Search page

* This page can be accessed by clicking on a brand or category link, or searching for a phrase using the searchbox (or of course by typing a correct ULR)
* The header informs what the results are for (brand, category or the searched term)
* Products are displayed as cards and when clicked, take user to the product page
* If user is logged in, products that are on their wishlist (regardless the colour) are marked with a little heart icon that takes user to their wishlist
* If product image link is broken, a replacement image is displayed instead
* If there are no products found, there is an information about it displayed

#### Beauty type test

* The page describes shortly what beauty types are and offers 5 quiz questions
* If all the questions are answered, and submit button clicked - user is taken to the result page

* **Result page**

  - Matching season together with a picture is displayed
  - Season description and random 12 matching colours are displayed
  - 3 random products in matching colours are displayed, when clicked, they take user to the product page
  - If user is logged in, products that are on their wishlist (regardless the colour) are marked with a little heart icon that takes user to their wishlist

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

* Basket page is available for both, authenticated and not authenticated users, as it is possible to checkout as a guest
* For authenticated user, basket content is saved in the database, so that they can access it even after closing their browser or accessing the website from different device
* If a product has colours, a colour must be chosen before being added to the basket
* One products but added in two different colours are two different basket items
* On the top of the page basket total is displayed, right next to the checkout button. This is repeated also at the bottom for the ease of use
* Each item image and name (which is also a link to the product page) are displayed, together with chosen colour (if product has colours)
* User can update the quantity of each product, or delete it completely from the basket - total and subtotal is automatically updated if this happens
* Checkout button takes a user to the checkout page

#### Checkout 

* This page contains checkout form, which is prefilled if the user saved this information before and is logged in, otherwise the form is empty
* If user is logged in, there is a possibility to save their details
* If user is not logged in - log in and register links are displayed
* 'Payment' field has to be completed in order to process Stripe payment. Since the Stripe functionality is only for testing, only 4242 4242 4242 4242 card number works. 
* From this page user can go back to their basket if they need to change something
* User is informed how much their card will be charged
* If a user clicks 'Confirm Order&Pay' button, the payment is done and user is redirected to the checkout success page, which displays order number and (for logged in user) order history link
* On checkout success a success message is displayed and a confirmation email with order and delivery details is sent. 

#### Wishlist

* This page is only available to logged in users.
* If user has not added anything to their wishlist yet, an information about it is displayed.
* Regardless, if product has colours or not, it can be added without a colour - unlike a basket item. This is because a customer might want to save only the product to their wishlist, without choosing a colour at that point.
* Similarly to the basket, one product with different colours, or one product with a chosen colour and without chosen colour, are two different wishlist items.
* If an item was added with colour, the colour is displayed in the bottom right corner
* If an item is clicked, user is taken to the product page
* Wishlist items can be deleted by clicking the x icon in the top right corner

### Features Left to Implement

* Admin view that would allow to add products using the application frontend - right now objects can be added using Django admin view, but this is not non-technical user friendly. Also, in this case Colour model should have a method that would use the assign_season function to find which season it belongs to, and then the season field value would be created automatically. 

* More ways to browse products - for example sorting options, searching only by name or description, price etc. 

## Information Architecture

### Data

The dataset comes from [Makeup API](https://makeup-api.herokuapp.com/) and the json file was taken from [Kaggle](https://www.kaggle.com/oftomorrow/herokuapp-makeup-products). The data needed to be changed before being added to the database - the colours needed to be sorted into 4 seasons. I wrote scripts that take care of assigning different colours to different season based on their HSL values, and then sort existing colours in the json file. Next, the data was added to the database using chunks of data from the json file, in a way that categories and colours are foreign keys in the products objects. These scripts can be found in the [data](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/tree/master/data) folder. Then, fixtures were created.

### Database 

SQLite (development) and PostgreSQL (production) databases were used, as with many relationships between the objects, relational database was a suitable choice. Django database-abstraction API was used to interact with the database.

I tried to depict relationships between the objects in the below graphic:

![information-structure](https://i.imgur.com/ZPqtfXg.jpg) 


* Although not authenticated user can use the core functionality of the website, many models depend on **User** model (this is a Django model not created by me).
* **User** can have one **Basket**, one **Wishlist** and one **Profile** (**User** is a foreign key in **Basket**, **Wishlist** and **Profile**)
* **Basket** can have many **Basket Items** (**Basket** is a foreign key in a **Basket Item**)
* **Wishlist** can have many **Wishlist Items** (**Wishlist** is a foreign key in a **Wishlist Item**)
* **Profile** can have many **Orders** (**Profile** is a foreign key in **Order** if it is created for an authenticated user)
* **Order** can have many **Order Items** (**Order** is a foreign key in **Order Item**)
* **Product** is independent from **User**, however **Basket**, **Wishlist** and **Order Item** have **Product** as a foreign key
* **Colour** is a foreign key for **Basket**, **Wishlist** and **Order Item**, and has many to many relationship to **Product** (product can have many colours and many products can have the same colour)
* **Category** has many to many relationship to **Product** - many products can have the same categories, and one product can have many categories (although this is rare in the dataset)
* **Brand** is a foreign key for **Product** - a product can have one brand

For the detailed information about models and their fields please see models files:

* [Basket and Basket Item Models](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/basket/models.py)
* [Wishlist and Wishlist Item Models](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/wishlist/models.py)
* [Profile Model](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/profiles/models.py)
* [Order and Order Item Models](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/checkout/models.py)
* [Product, Category, Brand and Colour Models](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/products/models.py)

## Technologies Used

### Languages

  * [Python](https://www.python.org/)
  * HTML
  * CSS
  * JavaScript

### Frameworks & Libraries

  * [Django](https://www.djangoproject.com/)
  * [jQuery](https://jquery.com/)
  * [Bootstrap](https://getbootstrap.com/)
  * [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
  * [Font Awesome](https://fontawesome.com/)
  * [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
  * [Gunicorn](https://gunicorn.org/)
  * [Psycopg](https://pypi.org/project/psycopg2/)
  * [Colour](https://pypi.org/project/colour/)
  * [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  * [Django mathfilters](https://pypi.org/project/django-mathfilters/)
  

### Tools

  * [Stripe](https://stripe.com/ie)
  * [AWS S3 Buckets](https://aws.amazon.com/s3/)
  * [Visual Studio Code](https://code.visualstudio.com/) 
  * [Git](https://git-scm.com/)
  * [Balsamiq](https://balsamiq.com/)
  

**Note to assessor**: This project used git branching for development. Although 'no fast forward' (--no-ff) merging was used to make this visible in the history, the branches are still visible on GitHub for easier access. It is best practice, however, to remove merged branches. 

## Testing

Please see the separate [testing.md document](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce/blob/master/testing.md)

## Deployment

This project was developed using the [Visual Studio Code IDE](https://code.visualstudio.com/), committed to Git and pushed to GitHub, and is hosted on Heroku platform, with static files being hosted using AWS. 


### How to run this project locally

In order to run this project you will need:

* [Python3](https://www.python.org/download/releases/3.0/) installed
* [PIP](https://pypi.org/project/pip/) installed
* [Git](https://git-scm.com/) installed

To clone this project from GitHub:

1. Follow [this link](https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce) to the Project GitHub repository.
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository.
4. In your local IDE open terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 3.

  ```
  https://github.com/Alicja-Malinowska/ColourPerfect-e-commerce.git
  ```
7. Press Enter. Your local clone will be created.

   More about cloning can be found on this [GitHub Help page](https://help.github.com/en/articles/cloning-a-repository).

Next steps:

*Note*: The project was developed in Windows environment. The below steps might be slightly different for a different OS. 

1. Create a virtual environment so that installations are done only for the project rather than globally. This process will depend on IDE you use. For VS Code intructions can be found on this [Python Environments page](https://code.visualstudio.com/docs/python/environments).

2. Use requirements.txt file to install all dependencies.

```
  pip install -r requirements.txt
```

3. Create environment variables:

  * DJANGO_SECRET - read more about [Django SECRECT_KEY](https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-SECRET_KEY)
  * STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY - read more in [Stripe Docs](https://stripe.com/docs/keys)
  * DEVELOPMENT = set this to 'True'


### Heroku deployment

If you would like to share this app with the world, Heroku platform is one option to do it.

1. Create an account on Heroku and next, create a new app.
2. Go to 'Resources' tab in Heroku and look for 'Heorku Postgres' in the 'Ad-ons' section, and add it to your project.
3. Make sure you have dj-database-url installed (this helps with database connection), gunicorn (WSGI HTTP Server), and Psycopg, a PostgreSQL database adapter - this should come from requirements.txt file. 
6. Change a default database in settings.py using your Postrgres database URL that can be found on Heroku in Settings/Config Vars. Note that this URL should not be exposed publicly, so make sure not to commit your changes to Git while the URL is in your settings.py file.
7. You can now run migrations and get the data from the fixtures to the new database. Make sure to load makeup fixture last, as it depends on the other 3 fixtures.
```
python manage.py migrate
```
```
python manage.py loaddata <fixture_name>
```
8. Create a superuser by running the following command in your terminal:
```
python manage.py createsuperuser
```
9. You can now remove your Postgres URL database, and get it from an environment variable 'DATABASE_URL', as this is already saved on Heroku. For development, use the SQLite as a default database. 
11. Note that the Procfile file is essential for the deployment to be successful. 
12. The static files are not hosted on Heroku, therefore collecting static needs to be disabled in Heroku before deployment.
For this you will need [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Login to Heroku and use the following command:
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app <app_name>
```
13. Add your Heroku app address to ALLOWED_HOSTS in your settings.py file. 
14. Set config vars in Settings on Heroku. You will need to add there your DJANGO_SECRET, STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY. 
4. To see deployment options, go to 'Deploy' tab in your project on Heroku.
5. One of the options is to use Heroku CLI, you can also connect to GitHub to automatically deploy every time you push to GitHub.
6. You will need to login into Heroku using terminal

```
heroku login
```
7. After all your changes are added and commited in git deploy your app by pushing it to heroku.

```
git push heroku master
```
8. You can see your app by clicking 'Open app' on Heroku platform.

### Hosting static files with AWS

1. In order to be able to use AWS storage, you need to have an AWS account, you can create on [their website](https://aws.amazon.com/). 
2. Once you have logged in, go to the Management Console and look for S3, and create a bucket with public access. 
3. In your bucket's properties click 'Static website hosting' and choose 'Use this bucket to host a website' option. 
4. In permissions tab, add CORS configuration, and generate bucket policy.
5. In Access Control List click 'Everyone' in Public access section and check 'list objects', then save. 
6. Go to another AWS service - IAM, and create a group, next create a policy and attach it to the group. 
7. Create a user and add it to the group, next download the CVS file with user's credentials. In this file you will find Access key ID ad Secret access key - save these as config variables on Heroku. 
8. Next, set up another variable on Heroku called 'USE_AWS' and set it to True - this ensures that settings.py uses S3 configurations when the project is deployed to Heroku. At this point, you can also delete COLLECT_STATIC variable. 

9. To connect Django to your S3 bucket, you need to have boto3 and django-storages installed - you should have this installed from requirements.txt. 
10. Note that 'storages' need to be in installed app in settings.py file. 
11. In settings.py change AWS_STORAGE_BUCKET_NAME to your bucket name and AWS_S3_REGION_NAME to your region. Region codes can be found on [AWS Docs website](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html).

### Sending emails

To send emails from the application, you need to connect it to your email account (e.g. Gmail). You need to set two more conf variables on Heroku:

* EMAIL_HOST_USER - set it to your email address
* EMAIL_HOST_PASSWORD - set it to your app password generated by your email provider (please note this is NOT your email account password)

# Credits

### Content

* [Description of 4 seasons theory](https://anuschkarees.com/blog/2013/09/24/colour-analysis-part-i-finding-your-type) 
* [Season beauty types description](https://www.rm-style.com/color-analysis-seasons-subgroups/?lang=en)
* Returns text taken from [Boots.ie website](https://www.boots.ie/customer-services/returns-exchange)


### Media

* The logo svg shape comes from [Flaticon](https://www.flaticon.com/authors/good-ware)
* [Hero image](https://www.pexels.com/photo/makeup-beauty-lipstick-make-up-3190/)
* [Bronzer photo](https://www.pickpik.com/makeup-brush-bronzer-cosmetics-make-up-schmink-brush-makeup-90733)
* [Blush photo](https://pixabay.com/photos/makeup-cosmetics-beauty-brushes-3907712/)
* [Eyeshadow photo](https://pixabay.com/photos/eyeshadow-makeup-beauty-palette-680002/)
* [Lipstick photo](https://pixabay.com/photos/lipstick-cosmetics-lips-make-up-1367775/)
* [Nail Polish photo](https://pixabay.com/photos/beauty-nail-polish-pink-2638343/)
* Test result photos all come from [Pixabay](https://pixabay.com/)
* [404 image](https://www.lifestyleasia.com/ind/beauty-grooming/makeup/things-to-do-in-lockdown-how-to-fix-broken-makeup/)
* [500 image](http://home.bt.com/lifestyle/wellbeing/cervical-cancer-charity-urges-public-to-post-smeared-lipstick-selfies-11363957622755)



### Acknowledgements

Thanks to my Mentor [Simen Daehlin](https://github.com/Eventyret) for giving me an idea to rearrange my navbar and other frontend tips. 

