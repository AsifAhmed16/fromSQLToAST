# SQLToAST Conversion Application with Django, React and PostgreSQL

This is a simple SQL To AST conversion application built with Django as backend React as frontend and PostgreSQL as database has been used. 
Here users can input PostgreSQL SQL queries, and the  application will display the modified SQL with hashed column names and the map.
The module - /backend/api/  parses PostgreSQL queries to generate an Abstract Syntax Tree (AST), modifies this AST by hashing the column names, maintains a MAP of original column names, and rebuilds the SQL query from the modified AST.
The application is containerized using Docker for easy deployment and scalability.


## Prerequisites

Before you begin, ensure you have the following installed on your machine:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Postgres](https://www.postgresql.org/)

## Getting Started

1. Clone the repository:

    ```bash
   
    git clone https://github.com/AsifAhmed16/fromSQLToAST
   
    cd fromSQLToAST
   
    ```

2. Copy the example environment file and customize it inside taskManagement application directory:

    ```bash
   
    cp .env.example .env
   
    ```

    Update the `.env` file with your specific configuration, such as database credentials and Django settings.


3. Build and start the Docker containers:

    ```bash
   
    docker-compose up -d --build
   
    ```

   Access the application by the url:
    [http://localhost:3000/](http://localhost:3000/)

   REST API Endpoint:
    [http://localhost:8000/api/](http://localhost:8000/api/)

   Access the Django admin panel:
    [http://localhost:8000/admin/](http://localhost:8000/admin/)


4. Test the backend logic and codes:

    ```bash
   
   cd fromSQLToAST
   
   cd backend 
   
    python manage.py test api
   
    ```

    Update the `.env` file with your specific configuration, such as database credentials and Django settings.


5. Deployment Instruction - in GCP (Google Cloud Platform):

    ```bash

    1. Login into your account.   
    2. Create a new VM Instance with basic requirements. (Give it a unique name, select Region and Zone)
    3. Take an E2 instance for - General Purpose. 8 vCPU + 12 GB memory can be an ideal choice.
    4. Take a Disk size of - 50 GB
    5. Take an image - Ubuntu 22.04 LTS.
    6. Create the Instance and access it by ssh.
    7. Install Postgres database and set credentials.
    8. Install Git and clone codes from that repository
    9. write command - 'cd fromSQLToAST'. and create a .env file inside the folder.
    10. Install Docker amd Docker Compose
    11. Run the command - 'docker-compose up -d --build'

    ```


6. Functionalities and Features

    ```bash

   1. Parsing SQL to AST: 
      A django REST API function that takes a SQL query string as input and returns its AST representation. (using https://github.com/andialbrecht/sqlparse)

   2. Modifying AST:
      For every column name in the AST, it will be replaced with a hashed value. Maintain a map (originalColumnName: hashedColumnName) for each transformation.

   3. Rebuild SQL from modified AST:  
      A function that takes the modified AST and returns the SQL query string with the hashed column names using the Parsing history stored in POSTGRES Database.

   4. Unit Tests:
      Unit tests to validate the correctness of functions. There are some options to improvement.
   
    ```


7. Deliverables

    ```bash

   1. Frontend:
        Used React.js. A User-friendly interface with a text area for SQL input and areas to display the modified SQL and the map.

   2. Backend:
        Used Django REST Framework. Implemented the parsing, modification, and rebuilding functions as API endpoints. Store and retrieve the original-to-hashed column names map in postgres database.

   3. Docker & Deployment:
        Containerized the application using Docker. Provide a docker-compose.yml for ease of setup. Instructions for deploying the app on GCP(Google Cloud Platform) is available below.

   4. Tests & Documentation:
        Unit tests for the backend logic are available. Full documentation is available.
  
    Additional Functionalities -
        .env.example file is available ato understand how the .env file were used.
   
    ```

## Usage

- The API is available at [http://localhost:8000/api/](http://localhost:8000/api/)
