# pyquote
This repository aims to scrap quotes from [Wikiquote](https://en.wikiquote.org), 
and images from [Unsplash](https://unsplash.com),
then display them in a website built in flask. Further I want this program to 
form available file for the commandline app "fortune".

This is a project for python&DL 2022 USTC course. And I'd like to develop it further.

# Web app deployed on Heroku
<https://pyquote.herokuapp.com>

# Usage
## Search Page
Here you enter the *keyword* then click **GO** button, the app will get the
quotes and image links which is immediately inserted into the postgresql database. 

## Show Page
After clicking the **GO** button the app will redirect to the respective show
page, with a specific url. 
- Clicking on the title **pyquote** will go back to the search page.
- Refreshing the page will change the quote and the background image displayed
  randomly.

## Error Handling
If search on *wikiquote* return no item, redirect to the search page and an
error message will be flashed.
