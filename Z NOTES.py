'''
2 types of requests:


QUESTION ON INTERVIEW:
*****
GET request: initally web page is loaded: getting information from the database
POST request: sends information to the database so it can post it (make changes) (update address)
****


web apps just use get and post requests


Django is a server-side web framework that encompasses all the elements that can help build interactive websites

*****
Models: 
*****



download pip install stuff: 
    pip install -r requirements.txt

create requirements file to download: 
    pip freeze > requirements.txt


PASSWORD = yorkie12


to add stuff to database: make migration, migrate



URL points to view
View acts as a function for database
View uses template




Pages - **on final interview**
    When we add a new page to our project, the first thing we do
    is make an entry in the url.py file
        That will give us the address of the new page along with
        the name of the view that is associated with that page
            The view is the central thing within all that's happening
                Allows us to interact with the database

        url.py file: put the location of the address, will tell it
        what view is associated with that location, and the name of
        the file

    Once we know the view associated with that address, we have to 
    know the function within the view that will handle everything 
    (the data) for that page we listed

    2 requests: 
        GET (read data from database)
        POST (write data to database)

    View is important because it grabs information from the database
    and uses the template, fills it up with the data, and then we can
    see it on the browser


    3 step process to add a view page:
        1. create address in url.py and tell it what view is assocated with that address
        2. create a function in the view
        3. create the corresponding html file for the template

        In our project:
            1. add topics url to the urls.py file
            2. Define a topics function in the views.py file
            3. Create the topics template topics.html that inherits from base.html




Dictionaries: **ON FINAL**
    key is the variable used in the template/html file
    value is the variable used in the view function


Template tags:
Template variables

'''