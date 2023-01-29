import sqlalchemy
import pandas as pd

def sql_to_pandas():

    """This function connects to a PostgreSQL database and returns a pandas dataframe"""
    
    # Create a connection string
    conn_string = "postgresql://docker:docker@db/mydatabase"

    # Create the connection object
    conn = sqlalchemy.create_engine(conn_string)

    # Execute a SELECT statement to retrieve the data from the table
    df = pd.read_sql("SELECT * FROM film", conn)

    return df

if __name__ == '__main__' : 
    sql_to_pandas()




