# Ski Shop <img align="right" width="75" height="75" src="static/readme_images/favicon.png">

# Site Goals
---

Ski Shop is an online ecommerce shop developed in Django.

This shop is initially targetting the Irish market.

The shop is populated with great value offers of leading brands of skis, snowboards and accessories.

- **For the purpose of the project submission I have retained the products and images form Boutique Ado, but when in production the products will be ski and snowboard products and images.**

The shop has most of the functionality you would expect from an online store.

Products by Category
Search
Basket
Checkout

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

------------------------

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

There are Logged Status changes to the navigation experience for My Account:

Not Logged In          |  Logged In   | SuperUser     
:-----------------:|:-----------------:|:-----------------:
![](/static/readme_images/notloggedin.webp)  |  ![](/static/readme_images/loggedin.webp)  | ![](/static/readme_images/superuser.webp)

------------------------------

# Manual Testing
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



### Non Logged in Users
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677583391/app_ziguur.jpg)

Note the Menu only has Register and Login Options.

- Logged in Users (SuperUser)

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677583100/admin_ttzvvd.jpg)

Note the menu now has Urban Centres and Admin.

-----------------------------

### Logged in Users
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677582898/user_diquz2.jpg)

Note Admin is not available to regular staff users.

----------------------------------

### Search Results Page
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677585347/result_tjuurr.jpg)

This is a Filtered List of Routes set in Card Format which is arrived at from 3 main options:

1. Search in Nav in Header

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677584835/search_w4fudn.jpg)

2. The Google Map is a visual interactive Search option for Commuters on Home Page

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677615191/map_dcunfc.jpg)

3. The Dynamic Filter Search on Home Page

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677585139/table_gzb7g2.jpg)

------------------------------

### Single Page
---

This is a Single Route(Post_detail) page

------------------------

### Timetable
---

The timetable is usually presented in a 2 table presentation.

- Inbound
- Outbound

The Site Visitor can toggle between the 2 with the Change Direction button.

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677615623/single_txqwjj.jpg)

------------------------------

### Links to Cheaper Fares and The Mobile App
---

This allows the Site Visitor to avail of cheaper fares and use advanced Journey Planning in the App.

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677587181/other_olkv9k.jpg)

----------------------------

### PDF and Back Button
---
There is a PDF button on this page to enable the Site Visitor to view or download a PDF version of the timetable.

These is also a Back Button on this page to take a Site Visitor to a previous Page.

Page 1           |  Page 2
:-----------------:|:-----------------:
![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677615937/Page1_fphufa.jpg)  |  ![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677615939/page2_cwlxnw.jpg)

-------------------

### Comments and Likes
---

The Site Visitor can view Comments and Likes Count for this Route/Post

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677587188/comment_vmojhm.jpg)

If the User is Logged in then they can Add Comments and Likes

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677588046/addcomment_ggwec3.jpg)

-----------------------

## Urban Centres
---

This is a CRUD for the Urban Centres.

**The Urban Centres with "Show On Map" set to true appear on the Google Interactive Map**

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677616115/urban_xgp21l.jpg)

------------------

## Admin
---

This is the Main Admin Panel.

**The Header and the Footer are not visible on this page as it is a Back End utility**

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677616240/admin_wrvwej.jpg)

----------------

## Footer
---

This is the footer which always visible. This has links to:

- Social media
- Office contact links

Partners are not links so as not to take site visitors away to other sites.

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677587184/footer_axwceh.jpg)

-----------------------------------------------

**Because the Header is sticky the Nav bar is always visible**

----------------------------------------------------

# Responsive
---
 
This GUI application is responsive using Bootstrap and looks good on different device screen sizes.

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677616512/responsive_swgo3h.jpg)

--------------------------------

# Project Walkthrough and Manual Testing
---

## Routes (Posts)
---

### Admin
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677595886/admin_xy6zky.jpg)

- Add a new Post

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677619680/postpage1_btind3.jpg)

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677621027/postpage2_qkzkyl.jpg)

**For testing purposes all HTML code for the Timetable in Post Content and other data can be taken from 

[Local Link Cork](https://locallinkcork.com/schedule/10000-quality-hotel-to-youghal/)

------------------------------------

### All Users
---

This post being published is now available to all Users:

- Visible on Home Page

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677685822/tablepost_gjszgk.jpg)

- Searchable on Map (Click Youghal)

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677686014/youghal_hjhppr.jpg)

- Searchable on Nav Bar search (type in quality)

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677686014/youghal_hjhppr.jpg)

- Route (Post Detail) Timetable is updated

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677686328/postdetail_vckdas.jpg)

- Route (Post Detail) PDF Version button links to PDF

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677686529/pdfyoughal_djimjg.jpg)

-----------------------------------------

### Logged in Users
---

This post being published is now available to logged in Users for Comments and Likes

- Route (Post Detail) is ready for Comments and Likes

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677686919/commentsadd_ux1nfj.jpg)

-----------------------------------------

### Admin
---

Comments submitted by Logged In Users need to be Approved by Admin

- Select comment to change
- Action Approve Comments

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677698140/commentapp_txlvnm.jpg)

------------------------------------------------------

## Urban Centres
---

### Signals and Model
---

Initially the map icons were populated from a JSON file. 

This was by way of signals.py whuch amended the json file to match urban model.

I did this because I was initially struggling with populating icons straight from the urban Model.

Unfortunately when deployed to Heroku this created an error as the json file was unavailable or impossible to read.

Because this may be some Heroku particular peculiarity I opted to retain signals.py.

I had to go back and research creating an option for the map icons to be read straight from the urban model.

Having successfully managed that now the Map icons are populated directly from Urban Model.

I have left the signals code available in case I need JSON file for distribution in further developments.

In javascript file I have hard coded this option:

```
// Set this flag to true if you want to fetch the data from the Django model
  const fromModel = true;
```

### Logged in Users
---

This is a CRUD for the Urban Centres.

**The Urban Centres With "Show On Map" set to true appear on the Google Interactive Map**

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677616115/urban_xgp21l.jpg)

**The Map currently has a Bus Icon over Youghal**

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687361/bus_ihyaad.jpg)

#### Delete
---

Select Youghal in Urban Centre and Click Delete.

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687987/youghallist_t3finw.jpg)

- It has dissappeared from the Urban Centre List

- The Bus Icon has now dissappeared on the Map also

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687678/youghalbus_sfpzw2.jpg)

#### Add
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687815/youghaladd_xi0030.jpg)

- It now appears in the Urban Centre List

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687987/youghallist_t3finw.jpg)

- It now appears as a Bus Icon on the Map

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687361/bus_ihyaad.jpg)

#### Toggle
---

Select Youghal in Urban List and Click Toggle

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687987/youghallist_t3finw.jpg)

- The Urban Centre and slug and Latitude and Longitude have a strikethrough
- The Show On Map is now False

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677688281/toggle_fcvmmx.jpg)

- The Bus Icon has now dissappeared on the Map also

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687678/youghalbus_sfpzw2.jpg)

Select Youghal in Urban List and Click Toggle again

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677688281/toggle_fcvmmx.jpg)

- Strikethrough is now gone
- The Show On Map is now True

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687987/youghallist_t3finw.jpg)

- The Bus Icon has now appeared on the Map also

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687361/bus_ihyaad.jpg)

#### Edit
---

Select Youghal in Urban List and Click Edit

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677687987/youghallist_t3finw.jpg)

The Edit Page appears

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677688911/edit_p5atnq.jpg)

Here you can change:

- Title (the slug will automatically be reset also)
- Latitude
- Longitude
- Showmap tick

Changing the co-ordinates will move the Bus Icon.

**Any Urban Centres created or edited with co-ordinates outside of LLC area of operation will appear on the map but will not be viewable by a user as the Google Map has bounds restricting the viewing area of the map to the LLC area of operation**

## Register
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677697897/register_julgvd.jpg)

Just select Register in Nav and then click Sign Up

## Login
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677697709/login_a024ya.jpg)

Just select Login in Nav and then click Sign In

## Logout
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677689824/signout_kpevtl.jpg)

Just select Logout in Nav and then click Sign Out

------------------------------------

**In Chrome Developer Tools, the Console had no errors**

------------------------------------

# Testing
---

## Urban CRUD Testing
---

Try to spoof the Urban CRUD while not logged in on other Browser

### List
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678107369/spooflist_wejupz.jpg)

### Add
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678107268/spoofadd_evus0n.jpg)

### Edit
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678107067/spoofedit_iymef5.jpg)

## Validator Testing
---

- HTML:             All pages were passed through the official https://validator.w3.org/ and no errors were found.

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677705268/htmlhome_vvn56z.jpg)

The Default Django Admin Panel does generate this warning:

Consider avoiding viewport values that prevent users from resizing documents.

<meta name="viewport" content="user-scalable=no, width=device-width, initial-scale=1.0, maximum-scale=1.0">

As this has no negative impact on the app I am ignoring this.

- CSS:              All pages were passed through the official https://jigsaw.w3.org/css-validator/ and no errors were found.

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677749645/csstest_mtpvhd.jpg)

## Lighthouse Testing
---

- Accessibility:    By running the site pages through Lighthouse in Inspect on Chrome I got the following results:

home desktop                |  home mobile
:-----------------:|:-----------------:
![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677842817/homedesktop_w7v8uk.jpg)  |  ![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677843042/homemobile_b04jcf.jpg)

**The Performance on Mobile is not good. But Google Maps even though slowing things down is an essential part of the design**

search results desktop               |  search results mobile
:-----------------:|:-----------------:
![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677843239/searchdesktop_kqolyw.jpg)  |  ![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677843392/searchmobile_tjgudt.jpg)

**Performance could be better. Images are being fed from Cloudinary which seems to be a bottleneck**

post detail desktop               |  post detail mobile
:-----------------:|:-----------------:
![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677843666/postdetaildesktop_mf1pv8.jpg)  |  ![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677843738/postdetailmobile_o2moac.jpg)

urban desktop               |  urban mobile
:-----------------:|:-----------------:
![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677844413/urbandesktop_bhwhft.jpg)  |  ![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677844049/urbanmobile_cn5zak.jpg)

admin desktop               |  admin mobile
:-----------------:|:-----------------:
![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677844158/admindesktop_gtbfaf.jpg)  |  ![](https://res.cloudinary.com/dxbarumnj/image/upload/v1677844248/adminmobile_xwymtn.jpg)

**Scores are not great but this is Django admin panel**

## Pycodestyle Testing
---

The 3 warnings that are listed are apparently in relation to the docker file and have nothing to do with the code in run.py and so can be ignored.

**All files are clear of Problems apart from settings.py**

## pep8 Testing
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678014870/pep8_bd4uzz.jpg)

**All files are clear of Problems apart from settings.py**

3 of the offending lines part of Django core.
1 offending line is Cloudinary.

## Javascript Testing
---

JSHint.com

```
    /* global google: false */
    /* global jQuery: false */
```

**google declaration is part of Google Maps API and to satisfy JSHint it is set to false**
**jQuery declaration is external and to satisfy JSHint it is set to false**

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678135372/jshint_yiyvjj.jpg)

----

## LLC Staff Final Verification
---

When the html code is pasted into the post content, the user can a make a visual comparison in the browser to ensure the results are as expected.

The user is the designer of the timetable (within given parameters of course).

Because the outcome in post content reflects the users Google sheet design, it is up to the user to decide if the outcome is what they planned.

If not, they can amend the HTML table code.

---------------------------------

## Development Transition
---

### Initial Workflow and Design Concept
---

This concept project has been developed by me in Wordpress and is live at:

[Local Link Cork](https://www.locallinkcork.ie/) 

Using Elementor as a Site Builder.

Wordpress and particularly Elementor are restrictive and sometimes do not play nice.
The site is slow in performance and requires too many work arounds.

The workflow to get a revised Timetable from Excel to Wordpress is too convoluted and messy.

So we are now moving to Django.

Automation is now much easier and full control of the workflow is possible.

-----------------------------------

### Planned Final Workflow and Design
---

This Project is not the final step but it is a major step forward.

The ultimate goal will be to take a revised or new Timetable directly from Excel and Publish.

### Following from Wordpress Project and HTML Builder Project
---

Wordpress          |  Github
:-----------------:|:-----------------:
[Local Link Cork](https://www.locallinkcork.ie/)  |  [Github](https://github.com/TMartin88/htmltablebuilder)

Wordpress Post Classic Block           |  HTML View
:-----------------:|:-----------------:
![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678050388/classic_j3tdmz.jpg)  |  ![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678050479/classichtml_vthrz7.jpg)

### Concept Design from Brainstorming
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678051947/conceptdesign_w5nnf8.jpg)

### Final Table Design in ElephantSQL
---

![](https://res.cloudinary.com/dxbarumnj/image/upload/v1678048605/Schedule_Manager_Database_Diagram_crow_s_foot_hikixk.jpg)

---------------------------------
 
## Bug Fixes
---

### Solved Bugs
---

- January 28th 2023 Summernote Runserver Errors
    - Fix 65443ec74bc87004ec1252b65d4872434b8aa062 remove references

- January 29th 2023 Summernote Runserver Errors
    - Fix 427f1f4efc14aa27a00e0c6da97b062b5a929ea9 summernote references sorted

- January 30th 2023 AllAuth not working
    - Fix 5f7ff1d767fedea494db5070f50f16477b9c1336 all auth sorted

- February 9th 2023 Swap Direction causing errors in developer tools console
    - Fix e20790a7221381dd3ce90cd86015e0dbf3e415a9 only applies now to post-detail page

- February 20th 2023 Registration not working
    - Fix 8bf2e771a6f096549d68ad277616932c583871a3 disable email verification in settings

- March 1st 2023 Double quotes typo in base.html
    - Fix 91d95f5fbfc7c5da579a931a4f5f9951cf6ea02e syntax fixed

- March 1st 2023 Search results page incorrect use of alt tags
    - Fix 08d271a6f9c14289d7298a53b78c3291cbed68ae syntax fixed

- March 3rd 2023 Search results page incorrect use of aria labels
    - Fix c8cac1283adf114aa23fed77ea246446faba84eb labels fixed

- March 3rd 2023 post_detail page incorrect use of alt tags
    - Fix 9ee5350e801fa97e92a5c105d1d3ccb92e33719f tags fixed

- March 3rd 2023 post_detail page aria label error
    - Fix dbc888e4fae2cac66c0b4f9acf489b944aecf6a8 error fixed

### Unfixed Bugs
---

- No known unfixed bugs.

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
    - Key: CLOUDINARY_URL Value: "cloudinary url"
    - Key: DATABASE_URL Value: "postgres url"
    - Key: Port Value: 8000
    - Key: SECRET_KEY Value: *******
    - Key: DISABLE_COLLECTSTATIC Value: 1
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

[Please click this link to see it in Heroku](https://schedulemanager.herokuapp.com/)

## Future Features
---

- To bring Fares Calculation https://github.com/TMartin88/farescalculator into this Project
- To bring HTML Builder https://github.com/TMartin88/htmltablebuilder into this project
- To remove the Copy and Paste of Timetable to Post content and write it in by code instead.
- To fully automate the workflow of Timetable updates or additions to Live Published Online.

---------------------------------

## Performance Improvements
---

- Lighthouse to bring all site ratings close to 100% on all fronts
    - Google Maps
    - Cloudinary Images

---------------------------------
 
## Credits
---

- [Slug Tutorial](https://learndjango.com/tutorials/django-slug-tutorial)
- [Full Text Search](https://testdriven.io/blog/django-search/)
- Post Engine assistance from "I Think Therefore I Blog"
- CRUD assistance from "Hello Django"
- [General Problem Solving](https://www.w3schools.com/django/)
- [Advanced Filters](https://www.w3schools.com/bootstrap4/bootstrap_filters.asp)
- [My Earlier development in Wordpress](https://locallinkcork.com/)
- [My Earlier experimental work with Google Maps API](https://github.com/TMartin88/dynamicmaps)
- [Default Form to Current Logged in User](https://stackoverflow.com/questions/70559902/django)
- [Signals for Json](https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/)
- [Signals for Json](https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/master/checkout/signals.py)
- [Skip to Site Content](https://www.a11yproject.com/)

---------------------------------