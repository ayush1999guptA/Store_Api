## ##Store_Api

This Api runs on python frameworks Flask,Flask_restful,Flask_JWT. They all serve their own purpose in this project.  Sqlite3 ,the python default database is used throughout the project  .Postman was used as the testing platform.

**#Prerequisits**

It is recommended that a virtual environment must be built of python 3.5 or  higher with flask, flask_restful,flask_jwt installed . Commands are as follows

 - pip install Flask
 - pip install Flask-restful
 - pip install Flask-JWT
 
**#How to run**


After cloning the repository to your local host you need to create a virtual environment in that folder and first run the create_table.py. After this a database will be created name data.db .Now run app.py you will get the following set of lines -
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 145-425-097
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 
i will use 127.0.0.1:5000 here as it is my local host you can use what your terminal shows you.


**#Requests**

There are so many requests that i will divide on the basis of there paths.
they are mainly GET,POST,PUT,DELETE.


@127.0.0.1:5000/household
This path only have one request.

 - GET :- This will return a json object which contains all the items that is in this available in the category in the store. status code returned-200ok
 
@127.0.0.1:5000/household/itemname
Instead of itemname ,the actual name of a product is to be given to the API . This path contains 4 requests.
 - GET:- it will return the json object which will contain name of the item, price of the item ,discount% on that item ,discounted price of that item. status code returned if item present 200,if not present in the database 404.
 - (JWT)POST:-it will take a json object in the format {"price":10.99} it will create a item with name "itemname" and price "10.99" ("discount%"=0 and "discounted price"=''10.99").status code returned if item already does not exist in the database 201,if already exists 400.
 - (JWT)PUT:-it will take a json object in the format{"price":4.99},it will then update the price of the item with name"itemname".or if does not exist in the database it will create a item with name"itemname" and price "4.99".status code return when updated 202,if created 201.
 - (JWT)DELETE:-it will delete item with name "itemname" from the database.status code if deleted 202 ,if not present 404.
 
@127.0.0.1:5000/electronics 
This path only have one request.

 - GET :- This will return a json object which contains all the items that is in this available in the category in the store. status code returned-200ok
 
 @127.0.0.1:5000/electronics/itemname
 Instead of itemname ,the actual name of a product is to be given to the API . This path contains 4 requests.
 - GET:- it will return the json object which will contain name of the item, price of the item ,discount% on that item ,discounted price of that item. status code returned if item present 200,if not present in the database 404.
 - (JWT)POST:-it will take a json object in the format {"price":10.99} it will create a item with name "itemname" and price "10.99" ("discount%"=0 and "discounted price"=''10.99").status code returned if item already does not exist in the database 201,if already exists 400.
 - (JWT)PUT:-it will take a json object in the format{"price":4.99},it will then update the price of the item with name"itemname".or if does not exist in the database it will create a item with name"itemname" and price "4.99".status code return when updated 202,if created 201.
 - (JWT)DELETE:-it will delete item with name "itemname" from the database.status code if deleted 202 ,if not present 404.
 
@127.0.0.1:5000/dairy
This path only have one request.

 - GET :- This will return a json object which contains all the items that is in this available in the category in the store. status code returned-200ok

@127.0.0.1:5000/dairy/itemname
 Instead of itemname ,the actual name of a product is to be given to the API . This path contains 4 requests.
 - GET:- it will return the json object which will contain name of the item, price of the item ,discount% on that item ,discounted price of that item. status code returned if item present 200,if not present in the database 404.
 - (JWT)POST:-it will take a json object in the format {"price":10.99} it will create a item with name "itemname" and price "10.99" ("discount%"=0 and "discounted price"=''10.99").status code returned if item already does not exist in the database 201,if already exists 400.
 - (JWT)PUT:-it will take a json object in the format{"price":4.99},it will then update the price of the item with name"itemname".or if does not exist in the database it will create a item with name"itemname" and price "4.99".status code return when updated 202,if created 201.
 - (JWT)DELETE:-it will delete item with name "itemname" from the database.status code if deleted 202 ,if not present 404.
 
@127.0.0.1:5000/grocery
This path only have one request.

 - GET :- This will return a json object which contains all the items that is in this available in the category in the store. status code returned-200ok

@127.0.0.1:5000/grocery/itemname
Instead of itemname ,the actual name of a product is to be given to the API . This path contains 4 requests.
 - GET:- it will return the json object which will contain name of the item, price of the item ,discount% on that item ,discounted price of that item. status code returned if item present 200,if not present in the database 404.
 - (JWT)POST:-it will take a json object in the format {"price":10.99} it will create a item with name "itemname" and price "10.99" ("discount%"=0 and "discounted price"=''10.99").status code returned if item already does not exist in the database 201,if already exists 400.
 - (JWT)PUT:-it will take a json object in the format{"price":4.99},it will then update the price of the item with name"itemname".or if does not exist in the database it will create a item with name"itemname" and price "4.99".status code return when updated 202,if created 201.
 - (JWT)DELETE:-it will delete item with name "itemname" from the database.status code if deleted 202 ,if not present 404.
 

@127.0.0.1:5000/users
This path only contains 1 request.

 - (JWT)GET:-it will show how many employees is currently in the database but will only show their username not their password.


@127.0.0.1:5000/userregistry
This path contains 3 requests .there is an existing user in the database with username Admin and password Therock@69 which will further be used to create another users.
 - (JWT)POST:-This request will accept a json object of type {"username":"Admin","password":"Therock@69"}.This will create a new employee in the database. status code returned will be 400 if username already taken ,202 when the username is created.
 - (JWT)PUT:-This request can be used to change password of a user ,it will take a json object of type {"username":"Admin","oldpassword":"Therock@69","new password":"dnakljndkan"}. This will create a user if username does not exist or if it exist it will change its password.status code returned will be 
202 if password changed ,201 if new user created,401 if old password is incorrect.
 - (JWT)DELETE:-This request will accept a json object of type {"username":"Admin","password":"Therock@69"}.It will delete the user which was passed as an object with its password.status code returned will be 202 if user is deleted and 404 if user is not present or its pass is incorrect.

@127.0.0.1:5000/auth
If you were thinking what did the JWT means before each request ,it means that that particular request will need a authorization token which will be generated by the API that jwt token will be given to you through this end point.this end point contains 1 request.

 - POST:- this will require a json object which contains detail of the employee of type{"username":"Admin", "password":"Therock@69"}. Now the employee will get the json token and can access to the restricted requests and make changes to the database. status code returned will 200 for correct password,401 for incorrect password and 400 for username not existing in the database

@127.0.0.1/discount/dairy
This endpoint contains 3 requests .

 - (JWT)POST:- this will require a json object of type{"discount":20}.It will then apply 20% discount on every product belonging to this category.
 - (JWT)PUT:-This will require a json object of type{"discount":30}.It will then update the existing to 30% discount on every product belonging to this category.
 - (JWT)DELETE:-this request will remove any kind of discount to the category.

@127.0.0.1/discount/housesold
This endpoint contains 3 requests .

 - (JWT)POST:- this will require a json object of type{"discount":20}.It will then apply 20% discount on every product belonging to this category.
 - (JWT)PUT:-This will require a json object of type{"discount":30}.It will then update the existing to 30% discount on every product belonging to this category.
 - (JWT)DELETE:-this request will remove any kind of discount to the category.

@127.0.0.1:5000/discount/grocery
This endpoint contains 3 requests .

 - (JWT)POST:- this will require a json object of type{"discount":20}.It will then apply 20% discount on every product belonging to this category.
 - (JWT)PUT:-This will require a json object of type{"discount":30}.It will then update the existing to 30% discount on every product belonging to this category.
 - (JWT)DELETE:-this request will remove any kind of discount to the category.

@17.0.0.1:5000/discount/electronics
This endpoint contains 3 requests .

 - (JWT)POST:- this will require a json object of type{"discount":20}.It will then apply 20% discount on every product belonging to this category.
 - (JWT)PUT:-This will require a json object of type{"discount":30}.It will then update the existing to 30% discount on every product belonging to this category.
 - (JWT)DELETE:-this request will remove any kind of discount to the category.

  

 
 
 
 

 
 

