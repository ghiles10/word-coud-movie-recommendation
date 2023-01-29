# word cloud movie reccomendation 
## Presentation

The goal of this project is to gather information about movies using web scraping techniques. The collected data is stored in a .txt file and processed using PySpark. A user interface was created using Dash, where users can select a movie from a list and view a word cloud of its reviews. Additionally, a film recommendation system was developed using Principal Component Analysis (PCA) and K-Means clustering algorithms. The films were grouped into clusters and displayed on the PCA axes for visualization.

The web app is hosted on the local machine at http://localhost:8050

## Project structure

### database

A database has been created using data scraped from the Allo Ciné website. It includes a table that contains information about movies, such as the number of reviews, individual reviews, release date, and rating. Additionally, this table may also store other relevant information about the movies, such as the cast and crew, production company, and genre. The database allows for easy access and analysis of the data, making it a valuable resource for movie enthusiasts and industry professionals alike.

### Word Cloud
A word cloud has been generated using the word cloud module. The resulting cloud displays the most frequently used words in the movie synopsis, providing the user with a convenient tool to assist in selecting a movie based on their preferences. The data processing was performed using Pyspark, and the final display of the cloud was achieved through its use

### ACP & K means for recommendation 

Movie recommendations are generated based on the similarity between films. A Principal Component Analysis (PCA) and K Means clustering algorithm were utilized to form clusters and visualize these clusters in the PCA axes, providing the user with a means to gauge their preferences and select films with similar characteristics.
For this purpose, the data is processed using pandas and sklearn.  

## Getting Started

A Makefile has been created for ease of use in launching the application. To start the application, simply run the command ```make run```
Run ```make delete``` to delete the data collected 
