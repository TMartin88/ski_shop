 # Ski Shop <img align="right" width="75" height="75" src="static/readme_images/favicon.png">

# Site Goals
---

Ski Shop is an online ecommerce shop developed in Django.

This shop is initially targetting the Irish market.

The shop is populated with great value offers of leading brands of skis, snowboards and accessories.

The shop has most of the functionality you would expect from an online store.

Products by:
- Category
- Search
- Basket
- Checkout

------------------------------------

![](/static/readme_images/shopfront.webp)

------------------------------------

# User Stories
---

## Shoppers
---

- As a shopper, I want to be able to view a list of products, so that so that I can review them with a view to purchase.
    - This is in place with search and product categories
- As a shopper, I want see details about a product, so that I can make informed decisions on whether to purchase or not.
    - There is a product detail page that tells the shopper more about products.
- As a shopper, I want see how much I have spent, so that I can make sure I am happy with the amount. 
    - The basket tots up all purchases in the basket and a toast notifies the shopper.
- As a shopper, I want have a shopping basket, so that I can see what I intend to buy and the cost.
    - The basket keeps the shopper informed of the cost..
- As a shopper, I want have a checkout option, so that so that I can pay for my basket contents.
    - The shopper has secure checkout
    - Payment through stripe
    - Notification  
- As a shopper, I want see delivery costs, so that I am not caught out by extra unforeseen costs.
    - the shopper can see the delivery costs clearly displayed
    - once we start to ship internationally we will have a shipping calculator
- As a shopper, I want to view by categories, so that I can easily identify products of interest to me.
    - Products are displayed with categorie splits.
- As a shopper, I want to be able to create a profile, so that my shopping experience can be a more personal experience.
    - The shopper can register and create a profile.

## Shop Owner
---

- As a shop owner, I want shoppers to register as account holders, so that I can personalise their shopping experience.
    - the functionality for registration is straighforward and easy.
- As a shop owner, I want a web store, so that buyers can browse the store and buy products.
    - The shop is hosted live on heroku and available for users to shop online.
- As a shopowner, I want to keep my shopper informed throughout the shopping experience, so that the shoppers are well informed and feel valued.
    - The shopping experience keeps th euser well informed.
- As a shop owner, I want to manage products, so that I can keep the site up to date.
    - Product management as all the functionality required
- As a shop owner, I want manage sizes and size availability for products, so that product and size availability is accurate for shoppers.
    - There is a basic sizes functionality in place
    - In the next version there will be a powerful size suite which allows for assigning sizes to products
    - This suite is already in place
    - It is not implemented into the shopping experience just yet.

--------------------------------

# UX/UI & Features
---

## Design Choices
---

This is a GUI application which has been designed to work across all devices.

Bootstrap allows for seamless responsiveness.

The site header and brand is preserved at the top of the page.

Good quality images are used for products to attract user attention.

The Main Background image is very striking and exciting.


## Wireframe
---

Using Balsamiq as a design tool, the home page wireframe is designed to grab the attention of a shopper.

It is a simple design without any clutter, with a Shop now button and Subscribe popup. 

Site Navigation is split into 2 areas.

Product Nav and My Account Nav.

The header is visible at all times so the shopper can always see the Basket.

In addition there is a popup to encourage the shopper to Subscribe.


![](/static/readme_images/websitesample.png)

 
## Database Schema
---

AllAuth

![](/static/readme_images/allauth.webp)

Product/Product Size

![](/static/readme_images/productsizemodel.webp)

Order/Profile

![](/static/readme_images/ordermodel.webp)

Shipping

![](/static/readme_images/shippingmodel.webp)

The database is designed to allow the shop owner to set specific sizes that are relevant to certain products.

Also the shipping is calculated based on Package Weight.

It is assumed that all of the products of the basket will be shipped at the same time.

In this version only Standard Shipping is applied.

In future versions the shopper at checkout will have the opportunity to select other shipping methods such as Express Shipping.

All Users have indiviudual profiles and the country can be used in shipping calculations.

## Responsive
---
 
This GUI application is responsive using Bootstrap and looks good on different device screen sizes.

![](/static/readme_images/responsive.webp)


## Shopping Concept
---

Shoppers can buy Ski related products in a simple secure way. They can get calculated shipping costs and can purchase products with relevant sizes.

For example Skis.

They are available in sizes that are appropriate to Skis.

Small 100-109 cm, Medium 150-159 cm and Large 180-190 cm.

These sizes are available in Beginner Intermediate and Expert.

![](/static/readme_images/productsizelist.webp)

**There is more detailed information on this in Product Size section**

When the shoppers purchase items the checkout process is secure using Stripe for payments and retaining orders stored against the shoppers profile.

**There is more detailed information on this in Checkout section**

--------------------------------

## Site Navigation
---

### Main Menu
---
 
Site navigation is primarily by way of:

- Main Menu.
    - All Products
    - Skis
    - Snowboards
    - Accessories
    - Others

- Top Line
    - Search
    - My Account
    - Basket

There are Logged In Status changes to the navigation experience for My Account:

Not Logged In          |  Logged In   | SuperUser     
:-----------------:|:-----------------:|:-----------------:
![](/static/readme_images/notloggedin.webp)  |  ![](/static/readme_images/loggedin.webp)  | ![](/static/readme_images/superuser.webp)

------------------------------

# Manual Testing and Walkthrough
---

## My Account

Signin  |  Signed In         
:-----------------:|:-----------------:
![](/static/readme_images/signin.webp)  | ![](/static/readme_images/signedin.webp) 
This is all working as expected.

My Profile          |  Profile Updated
:-----------------:|:-----------------:
![](/static/readme_images/myprofile.webp)  |  ![](/static/readme_images/profileupdated.webp)
       
This is all working as expected.

Logout         |  Profile Updated
:-----------------:|:-----------------:
 ![](/static/readme_images/logout.webp)  |  ![](/static/readme_images/loggedout.webp)

This is all working as expected.

Register        |  Error Trap | Registered
:-----------------:|:-----------------:|:-----------------:
 ![](/static/readme_images/register.webp)  |  ![](/static/readme_images/errortrap.webp) | ![](/static/readme_images/registered.webp)


This is all working as expected.

### Logged in Superuser
---

**IMPORTANT! There is additional functionality to superusers. Shop Managers are superusers and responsible for Product Maintenance**

#### Product Management

Select Category        |  Add Product
:-----------------:|:-----------------:
 ![](/static/readme_images/addproduct1.webp)  |  ![](/static/readme_images/addproduct2.webp)

This is all working as expected.

Product Added

![](/static/readme_images/productadded.webp)


This is all working as expected. 

Edit Product       |  Editing Product
:-----------------:|:-----------------:
 ![](/static/readme_images/editproduct.webp)  |  ![](/static/readme_images/editingproduct.webp)

**Note Price Change**

Edited Product

![](/static/readme_images/editedproduct.webp)

**Note that Has Sizes has been selected as True, the default size option is now visible**

**But this is not the same as assigning Product Sizes to a Product see the following image**

Product with sizes

![](/static/readme_images/productwithsizes.webp)

These sizes are available for selection because they are sizes that have been assigned to the product.

This is all working as expected.

-----------------------------

#### Sizes Management

**Please note that sizes share the same category model as Products**

Add Size        |  Size Added
:-----------------:|:-----------------:
 ![](/static/readme_images/addsize.webp)  |  ![](/static/readme_images/sizeadded.webp)

This is all working as expected.

Edit Size       |  Size Edited
:-----------------:|:-----------------:
 ![](/static/readme_images/editsize.webp)  |  ![](/static/readme_images/sizeedited.webp)

 This is all working as expected. Rollers Included now in description.

Delete Size (Wooly Hat)     |  Size Deleted
:-----------------:|:-----------------:
 ![](/static/readme_images/woolyhat.webp)  |  ![](/static/readme_images/sizedeleted.webp)


This is all working as expected. Wooly Hats is now gone.

-----------------------------

#### Product Sizes Management

**Please note that because sizes share the same category model as Products, sizes can only be assigned to Products of the same category**

Add Product Size        |  Product Size Added
:-----------------:|:-----------------:
 ![](/static/readme_images/addproductsize.webp)  |  ![](/static/readme_images/productsizeadded.webp )

This is all working as expected.

Edit Product Size       |  Product Size Edited
:-----------------:|:-----------------:
 ![](/static/readme_images/editproductsize.webp)  |  ![](/static/readme_images/productsizeedited.webp)

 This is all working as expected.

 **Please note there is a bug here the available sizes to edit should be filtered by the category and ski bag should not be an option**

Delete Product Size      |  Product Size Deleted
:-----------------:|:-----------------:
 ![](/static/readme_images/productsizeedited.webp)  |  ![](/static/readme_images/productsizedeleted.webp)


This is all working as expected.

-----------------------------

## Has Sizes

![](/static/readme_images/hassizes.webp)

The Product has sizes boolean indicates whether Sizes are available for selection for this product or not.

Product Size Allocated  | Default Size Select    |  No Size Select
:-----------------:|:-----------------:|:-----------------:
 ![](/static/readme_images/productwithsizes.webp)  |  ![](/static/readme_images/editedproduct.webp)  |  ![](/static/readme_images/hasnosize.webp)

The default sizes available are: XS, S, M, L, XL and they are hard coded.

With the Product Size functionality implemented in the shopping experience the sizes available are dynamic.

As in each product can have its own size options.

Like for instance Skis have size options like this:

![](/static/readme_images/productsizelist.webp)

In this way products can be assigned sizes that are relevant to that type of product.

-----------------------------

## Django Admin

**Please note all Product, Sizes and Product Size Management functionality is also in the admin section.**

Django Admin       |  Product Size Admin
:-----------------:|:-----------------:
 ![](/static/readme_images/admin.webp)  |  ![](/static/readme_images/adminproductsize.webp)

  **Please note all Shipping Methods and Shipping Costfunctionality is also in the admin section.**

 ### Shipping Methods

![](/static/readme_images/shippingmethods.webp)

### Shipping Costs

![](/static/readme_images/shippingcosts.webp)

The Shipping Costs have Weight Bands to which different costs are applied.

The package weight dictates which band is used.

At the moment only Standard Shipping is being applied.

In future versions the shopper can select from various shipping methods at checkout.

**Note Admin is only available to superusers**

![](/static/readme_images/denied.webp)

This is all working as expected.

-----------------------------

## Search Results Page
---

![](/static/readme_images/search.webp)


 This is all working as expected.

----------------------------------


## Product Categories Main nav
---

All Products          |  Skis   | Snowboards  |  Accessories  | Others
:-----------------:|:-----------------:|:-----------------:|:-----------------:|:-----------------:
![](/static/readme_images/allproducts.webp)  |  ![](/static/readme_images/skis.webp)  | ![](/static/readme_images/snowboards.webp) | ![](/static/readme_images/accessories.webp) | ![](/static/readme_images/Others.webp)

------------------------

## Shopping (Showing No Size, default Size and Relevant sizes examples)
---

Shopping for Skis

 ![](/static/readme_images/skiproducts.webp)

Shopping for Snowboards

 ![](/static/readme_images/snowboards.webp)

Shopping for Ski Mask

 ![](/static/readme_images/goggles.webp)

Skis with Sizes       |  Snowboards Default Sizes      |  Mask No Sizes
:-----------------:|:-----------------:|:-----------------:
 ![](/static/readme_images/sizedropdown.webp)  |  ![](/static/readme_images/snowboardsize.webp) |  ![](/static/readme_images/hasnosize.webp)


## Shipping/Delivery Costs
---

### Shipping Cost Calculated

There are 2 variables in settings

```
FREE_DELIVERY_THRESHOLD = 500
FLAT_DELIVERY_CHARGE = 150
```

All orders above the threshold have free delivery.
The Flat Delivery Charge is applied where the order is less than the threshold and either the shopper is not logged in or there is no standard delivery set for this shoppers country.

Otherwise the rates are applied from the shipping cost model.

## Shopping Basket
---

### This is where the user is Logged in and their profile country is in shipping costs.
---

Add Skis with Product Size to Basket       |  Add Snowboard with Default Size to Basket 
:-----------------:|:-----------------:
 ![](/static/readme_images/skisizebasket.webp)  |  ![](/static/readme_images/snowboardsizebasket.webp)


**Note there is no Delivery cost because the threshold is exceeded**

Remove Skis from Basket |  Calculated Standard Delivery Applied 
:-----------------:|:-----------------:
![](/static/readme_images/skisremovefrombasket.webp) |  ![](/static/readme_images/stadarddelivery.webp)

**Note on the left image there is now a prompt to purchase more to avoid delivery cost**

**Note on the right image and Calculated Standard Delivery is applied**

### This is where the user is Not Logged in or their profile country is not in shipping costs..
---

Add Snowboard with Default Size to Basket        |  Flat Delivery Charge 
:-----------------:|:-----------------:
 ![](/static/readme_images/snowboardsizebasket2.webp)  |  ![](/static/readme_images/flatdeliverycharge.webp)

**Note on the left image there is now a prompt to purchase more to avoid delivery cost and Flat Delivery notice**

**Note on the right image there is Flat Delivery Charge applied**

## Shopping Checkout
---
Checkout      |  Complete Order
:-----------------:|:-----------------:
 ![](/static/readme_images/checkouttop.webp)  |  ![](/static/readme_images/success.webp)

**Note on the left image that the country is New Zealand which has a designated shipping cost hence no Flat charge**

 This is all working as expected.

------------------------

## Newsletter with Mailchimp
---

![](/static/readme_images/mailchimp.webp)

 This is all working as expected.

------------------------

## Facebook
---

![](/static/readme_images/facebook.webp)

 This is all working as expected.

 **In Chrome Developer Tools, the Console had no errors**

------------------------

# Testing
---

## CRUD Testing
---

Try to spoof the Management CRUD while not logged in on other Browser

![](/static/readme_images/signinchallenge.webp)

This signin challenge appears for all spoof attempts.

------------------------

## Validator Testing
---

- HTML:             All pages were passed through the official https://validator.w3.org/ and no errors were found.

![](/static/readme_images/htmlchecker.webp)

The Default Django Admin Panel does generate this warning:

Consider avoiding viewport values that prevent users from resizing documents.

<meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">

As this has no negative impact on the app I am ignoring this.

- CSS:              All pages were passed through the official https://jigsaw.w3.org/css-validator/ and no errors were found.

![](/static/readme_images/cssw3c.webp)

## Lighthouse Testing
---

- Accessibility:    By running the site pages through Lighthouse in Inspect on Chrome I got the following results:

home desktop                |  home mobile
:-----------------:|:-----------------:
![](/static/readme_images/desktophome.webp)  |  ![](/static/readme_images/mobilehome.webp)


search results desktop               |  search results mobile
:-----------------:|:-----------------:
![](/static/readme_images/desktopsearch.webp)  |  ![](/static/readme_images/mobilesearch.webp)


product management desktop               |  product management mobile
:-----------------:|:-----------------:
![](/static/readme_images/productmanagmentdesk.webp)  |  ![](/static/readme_images/productmanagmentmob.webp)

**Performance is low here for mobile particularly. THis iwll be improved in production when I introduce proper appropriate images for products**


size management desktop               |  size management mobile
:-----------------:|:-----------------:
![](/static/readme_images/sizemanagementdesk.webp)  |  ![](/static/readme_images/sizemanagementmob.webp)
admin desktop               |  admin mobile


django admin desktop               |  django admin mobile
:-----------------:|:-----------------:
![](/static/readme_images/djangoadmindesk.webp)  |  ![](/static/readme_images/djangoadminmob.webp)
admin desktop               |  admin mobile


## Pycodestyle Testing
---

The 3 warnings that are listed are apparently in relation to the docker file and have nothing to do with the code in run.py and so can be ignored.

## python3 -m flake8 Testing
---

- settings.py ignored
- vscode warnings are ignored
- unused admin.py files are ignored
- migrations line too long warnings are ignored
- products ignored as from boutique Ado
- profile ignored as from Boutique Ado
- checkout ignored as from Bouique Ado

The following code line from checkout views.py is too long but anytime I tried to fix it , the checkout broke so I have left it.

```
self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
```
The following code line from ski_shop urls.py is required ofr 404 for work.

```
./ski_shop/urls.py:33:1: F811 redefinition of unused 'handler404' from line 20
```

## Javascript Testing
---

JSHint.com


![](/static/readme_images/jshint.webp)

----

# Marketing Strategy

## E-Commerce Business Model
-------

We have recognised that an online presence with a top end Online Shop is essential for Shoppers to enjoy shopping on our store.

This online store offers easy navigation, robust search functionality, secure payment processing, and detailed product descriptions.

Continuous improvement will ensure that this online shop will maximise the traffic coming to our store.

We offer a wide range of ski equipment, including skis, boots, poles, helmets, goggles, and clothing.


## Customer Service

We provide excellent customer support, including assistance with product selection, sizing, and addressing any concerns or inquiries.


## Target Market

Our target market includes skiers of all ages and skill levels, catering to both beginners and experienced enthusiasts.

Initially targetting Ireland only.


## Revenue

Our revenue comes exclusively from our online store as we do not have a high street presence.


## Fulfillment and Shipping

Once a shopper clicks Complete Purchase then the logistics kick in. How do we get the products to the shopper?

While our market is in Ireland we will do this through the postal service and some courier services.

A Shipping calculator will be provided.


### Dropshipping

This is an important consideration once we progress to the international market. In this instance we will not have any stock at all and all shipping will be handled by our wholesalers.

This will require an integration with wholesalers so that the correct shipping cost as calcualted by the wholesaler is provided to the shopper in our online checkout business process.


##  Define Unique Selling Proposition (USP)
We have identified our unique selling proposition, which includes a combination of competitive prices, exceptional customer service, and a wide selection of exclusive products.

## SEO and Content Marketing
We will continually optimize our website for search engines by targeting relevant skiing-related keywords. We will also create informative and engaging content, such as blog posts, guides, and tutorials, to attract and educate potential customers.

## Social Media Marketing
We will leverage platforms like Instagram, Facebook, and Twitter to showcase our products, share skiing tips, post customer testimonials, and run targeted advertising campaigns.
We will use Social Media tools like Hootsuite to manage all of our Social media platforms

## Email Marketing

We will build an email list by offering exclusive discounts, updates on new products, and informative content to subscribers. We will send regular newsletters to engage with our audience and encourage repeat purchases.

## Retargeting and Remarketing

We will implement strategies to reach potential customers who have shown interest in our products by displaying targeted ads on other websites they visit or through social media platforms.

## Affiliate Marketing

We will collaborate with skiing-related websites, blogs, and influencers to drive traffic to our store. We will offer them a commission for each sale generated through their referral.
We will regularly contribute articles for Winter Sport websites and Magazines.
We will be a presence at Tradeshows and Ski and Snowboarding events.

## Customer Loyalty Program

We will implement a loyalty program to incentivize repeat purchases. We will offer discounts, rewards, and exclusive perks to encourage customer retention.

## Customer Reviews and Testimonials

We will encourage customers to leave reviews and testimonials on our website. Also a rating system for our products.

**Note this has not yet been developed.

--------

## Development Transition
---

### Initial Workflow and Design Concept
---

This online shop has all the standard functionality and look and feel of an online shop.

The additional development is based around expanding size, colour options and functionality.

Also Shipping where shipping calculations are more sophisticated.
-----------------------------------

### Planned Final Workflow and Design and Future features
---

This Project is not the final step but the building blocks are in place.

Helpful tools like Size Calculators for the various product categories will be developed.

Colors as well as sizes will be implemented in future developments.

Shipping will be expanded to allow for International Markets.

---------------------------------
 
## Bug Fixes
---

### Solved Bugs
---

- April 24th 2023 Color Functionality not working
    - Fix 6596e38b8e1639c6c8ef2f9ab76d0e23e246c01c remove color functionality

- April 27th 2023 ProcFile incorrectly placed
    - Fix 881a09a4a251f29a21db12a89dc98d628b437492 move Procfile

- May 12th 2023 Path is wrong
    - Fix 08eb54557a06c2ffcd70f817c5470b6f708e2540 incorrect path fixed

- June 8th 2023 Fix email send
    - Fix 681bddcc755f2d262d234fa3899b45de0d50e694 email send fixed

- June 10th 2023 Div class incorrect
    - Fix 681bddcc755f2d262d234fa3899b45de0d50e694 div class fixed

- June 14th 2023 Product size not working
    - Fix 681bddcc755f2d262d234fa3899b45de0d50e694 remoove fixed


### Unfixed Bugs
---

- Product Size editing the size dropdown selection box should be filtered by category.
- The Mailchimp popup is not performing correctly on Mobile Phone.

----

## Deployment

### Deployment to Heroku
---

The site is deployed to Heroku. 

#### Initial Deployment
---

In Heroku

- Sign up for Heroku Account or Login
- Create New App in Heroku
- Use a unique App name that does not already exist.
- Select Region.
- Create App.
- Postgres.
- In Settings Reveal Config Vars
    - Key: AWS_ACCESS_KEY_ID Value: ********
    - Key: AWS_SECRET_ACCESS_KEY Value: ********
    - Key: DATABASE_URL Value: ********
    - Key: EMAIL_HOST Value: smtp.gmail.com
    - Key: EMAIL_HOST_PASS Value: ********
    - Key: EMAIL_HOST_USER: ********
    - Key: EMAIL_PORT Value: 587
    - Key: EMAIL_USE_TLS Value: True
    - Key: HEROKU_POSTGRESQL_PUCE_URL Value: ********
    - Key: SECRET_KEY Value: ********
    - Key: STRIPE_PUBLIC_KEY Value:********
    - Key: STRIPE_SECRET_KEY Value: ********
    - Key: STRIPE_WH_SECRET Value: ********
    - Key: USE_AWS Value: True

- Manual Deploy (Select Github as deployment method)
- Search for Django Repo
- Deploy Branch
- Check Build Log for errrors.
- Run App

In Gitpod

- Create Procfile
    - Gunicorn

#### Final Deployment
---

In Heroku
- Login to Heroku Account
- In Settings Reveal Config Vars Remove the following:
    - Key: DISABLE_COLLECTSTATIC Value: 1
- Enable Automatic Deploys

In Gitpod

- In Settings ensure Debug = False
- Ensure all is Pushed and check Git Status

[Please click this link to see it in Heroku](https://skishop.herokuapp.com/)

## Performance Improvements
---

- Lighthouse to bring all site ratings close to 100% on all fronts
    - Product Images

---------------------------------
 
## Credits
---

- Pexels for images
- CRUD assistance from "Hello Django"
- [General Problem Solving](https://www.w3schools.com/django/)
- [Advanced Filters](https://www.w3schools.com/bootstrap4/bootstrap_filters.asp)
- [Signals for Json](https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/)
- [Signals for Json](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/checkout/signals.py)
- Some code I reused from my Project 4 

---------------------------------