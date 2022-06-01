# My First Website in Flask
#### Video DEMO:  https://youtu.be/JonVdECNGu4
#### Description:

I have built websites in the past using HTML/CSS and The Wordpress Templates that were provided later on.  I decided to give website building a try, after so many years,
using Flask, HTML, Javascript, SQL, CSS etc.  In this project I did use bootstrap CSS to create the template of this project as I did enjoy the interface.  However,
I did have to decypher the samples and only keep what I wanted as the skeleton of my website.
I wanted to keep things simple as if I were to create a website, I wouldn't know what I would want to show the world.  Instead, I created a mini porfolio of the things I
learned in Harvard CS50 opensource and impliment it in a Website.

At first I was intimidated by Flask.  Routes and redirecting and returns.  To my novice mind, it was like directing traffic.  However, once I was able to try and fail
numerous times, reading documentation and youtube tutorials to explain documentation further; I was able to find my "a-ha!" moment.  Flask is definitely much easier to learn
versus Javascript.  After this course, I feel my next step to programming will be learning more on Python and Javascript.  I am very intimidated by Javascript, however that
will not stop me from learning to understand it.

Below are the pages to my final project and what I used to create it.

**application.py**
The main programming source of the application using routes in flask

**sqldata.db**
SQL Database created for the connect.html page

**templates/about.html**
HTML/CSS page about me

**templates/connect.html**
HTML/CSS page utilizing a form to connect and save to a SQL database

**templates/index.html**
Index, first page the viewer reads.  Has a Javascript Hello ____ form for users to fill out!

**templates/layout.html**
Layout template for all pages that utilize Jinja to connect so I do not have to copy and paste the same template across the website

**templates/links.html**
Filler page showing my favorite websites throughout this course

**templates/oops.html**
Error page that connects with the connect.html page.  Ensures that users are inputting the correct information and all the information necessary for the SQL database

**templates/thankyou.html**
Verification page to the users in the connect.html page to ensure that they know their information came through

**static/bootstrap.bundle.min.js**
Utilized bootstrap tools to create the framework of the website as learned in week 8 of CS50

**static/bootstrap.min.css**
Utilized bootstrap tools to create the design of the website as learned in week 8 of CS50

**static/navbar.css**
Utilized bootstrap tools to create the design of the website as learned in week 8 of CS50

I am happy that I was able to start a course and finish it.  Although it took me 2 years to complete.  I am thankful that my current job hired me back
which allowed me to have the funds and create time to finish this course.
I am also happy that the skills I learned in this course, applied to solving problems in my current job.
Example:  Nikon Cameras do have an integer overflow issue that was solved the wrong way.  There is a way to manually reset the system, however the way
Nikon programmers did it, really causes issues to the user.

When Nikon Cameras reach folder number 999, and the file number reaches image number 999, the camera tells the user that the XQD and CF cards are full.
However because we use high capacity XQD and CF cards of 64gig.  We know for a fact that we can store up to 1200 RAW/NEF files and 6000 JPG files.
The camera tells the users that the memory cards are full because it cannot read if there are other folders in the memorycard.  Also, it cannot make folder 1000 because
there are only 3 integers in the folder numbers.
Solution:  We have to manually reset the folder to start at 001 to tell the camera "it is okay, we can create this folder".
My guess is some users tether the camera to a central server that has multiple folders and this was a situation that was programmed to not allow folders to be overwritten
in the event a user has multiple folders ranging from 001-999.

This concludes my readme file.  I hope to learn more about Flask and utilize it in the future with programming.
I am also looking forward to what else there is on EdX.org