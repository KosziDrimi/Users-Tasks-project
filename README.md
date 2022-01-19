# TasksApp

Simple programme offering the possibility to:
- download data from the [link](https://jsonplaceholder.typicode.com/) API,
- create the sqlite database,
- save the downloaded data to database,
- write the processed data to csv file,
- create the API from the file using fastapi-csv.

In order to create database and csv file please:
- install all required dependencies (`pip install -r requirements.txt`),
- and run `python database.py` as well as `python create_csv.py` commands.

And to create the API:
- run `uvicorn api_csv:app` on your command line,
- and open the browser at local host specified (`http://127.0.0.1:8000/users_tasks`) to view it. 

Documentation for the API can be found on: `http://127.0.0.1:8000/docs`. 
It shows the available query parameters allowing filtering the data according to the specific needs. 

Technologies: Python 3.9.1, fastapi-csv 0.1.0, SQLite.