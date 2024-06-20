# api_dataanalytics_dataload

##This code repository handles data processing and provides an API.

###What it does:

Loads data: It can load data from JSON files into a PostgreSQL database.
Prepares an API: It uses the FastAPI framework to create an API that can be used to access the data.
Fetches data from external APIs: It can also retrieve data from external APIs for further processing.
Benefits:

Designed for Docker: This code is designed to run in Docker containers, making it easy to deploy and scale.
Modular Design: It uses separate containers for each task (database, data loading, API, and data acquisition), promoting maintainability.
Additional Notes:

The code can be modified to handle Change Data Capture (CDC) and incremental data loads.
Containers used:

PostgreSQL: Stores the loaded data.
Load data from JSON to database: Processes JSON files and loads the data into the database.
Prepare API using FastAPI: Creates a web API for accessing the data.
Data acquisition from API: Fetches data from external APIs.
