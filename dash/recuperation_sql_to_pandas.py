def sql_to_pandas():
    import sqlalchemy
    import pandas as pd

    # Create a connection string
    conn_string = "postgresql://docker:docker@db/mydatabase"

    # Create the connection object
    conn = sqlalchemy.create_engine(conn_string)

    # Execute a SELECT statement to retrieve the data from the table
    df = pd.read_sql_query("SELECT * FROM film", conn)

    return df

if __name__ =='__main__' : 
    sql_to_pandas()




