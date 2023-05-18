import sys
import pandas as pd
import numpy
from sqlalchemy import create_engine

CSV_FILE = sys.argv[1]
SQL_FILE = 'create_table_' + CSV_FILE[:-4] + '.sql'

# Generate a .sql file that contains the CREATE TABLE statement and all the INSERT INTO statements needed to populate the database from the CSV file.
def generate_sql_file(csv_file):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)
    # For the column Id change the data type to int
    if 'Id' in df.columns:
        df['Id'] = df['Id'].astype(int)
    # Gnenerate the CREATE TABLE statement
    create_table_statement = generate_create_table_statement(df)
    # Generate the INSERT INTO statements
    insert_into_statements = generate_insert_into_statements(df)
    # Write the CREATE TABLE statement and the INSERT INTO statements to a .sql file
    with open(SQL_FILE, 'w') as f:
        f.write(create_table_statement)
        for statement in insert_into_statements:
            f.write(statement)

def generate_create_table_statement(df):
    # Generate the CREATE TABLE statement and infer the data types
    create_table_statement = 'CREATE TABLE IF NOT EXISTS ' + CSV_FILE[:-4] + ' (\n'
    for column in df.columns:
        if df[column].dtype == 'int64':
            create_table_statement += column + ' INT,\n'
        elif df[column].dtype == 'float64':
            create_table_statement += column + ' FLOAT,\n'
        else:
            if len(df[column].unique()) > 10:
                create_table_statement += column + ' TEXT,\n'
            else:
                create_table_statement += column + ' VARCHAR(255),\n'
    create_table_statement = create_table_statement[:-2] + '\n);'
    return create_table_statement

def generate_insert_into_statements(df):
    # Generate the INSERT INTO statements based on the data in the DataFrame
    # iterate over the rows in the DataFrame and find the data type of each value
    insert_into_statements = []
    for index, row in df.iterrows():
        insert_into_statement = 'INSERT INTO ' + CSV_FILE[:-4] + ' VALUES ('
        for value in row:
            if type(value) == str:
                value = value.replace("'", "").strip()
                insert_into_statement += "'" + value + "', "
            elif pd.isnull(value):
                insert_into_statement += 'NULL, '
            else:
                # test if value have no decimal places
                if value % 1 == 0:
                    insert_into_statement += str(int(value)) + ', '
                else:
                    insert_into_statement += str(value) + ', '

        insert_into_statement = insert_into_statement[:-2] + ');\n'
        insert_into_statements.append(insert_into_statement)
    return insert_into_statements

generate_sql_file(CSV_FILE)