# word cloud movie reccomendation 
## Presentation

The goal of this project is to gather information about movies using web scraping techniques. The collected data is stored in a PostgreSQL database and processed using PySpark. A user interface was created using Dash, where users can select a movie from a list and view a word cloud of its reviews. Additionally, a film recommendation system was developed using Principal Component Analysis (PCA) and K-Means clustering algorithms. The films were grouped into clusters and displayed on the PCA axes for visualization.

The project is deployed in a Docker container by creating a Docker Compose which orchestrates the containers. This makes it easy to install and run the project on any computer with Docker.

The web app is hosted on the local machine at http://localhost:8001
The database on postgresql can be accessed at http://localhost:8080

## Project structure

### PostgreSQL database

A database has been created using data scraped from the Allo Ciné website. It includes a table that contains information about movies, such as the number of reviews, individual reviews, release date, and rating. Additionally, this table may also store other relevant information about the movies, such as the cast and crew, production company, and genre. The database allows for easy access and analysis of the data, making it a valuable resource for movie enthusiasts and industry professionals alike.

### Web Application


docker compose -f "docker-compose.yml" up --build

