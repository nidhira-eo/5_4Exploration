import os
import psycopg2

# Connect to database
conn = psycopg2.connect(
    host = "drhscit.org",
    database = os.environ['DB'],
    user = os.environ['DB_UN'],
    password = os.environ['DB_PW']
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Create a new table for reviews
cur.execute('DROP TABLE IF EXISTS reviews;')
cur.execute('CREATE TABLE reviews (name VARCHAR (150) NOT NULL,'
                                 'review TEXT,'
                                 'rating INTEGER);'
                                )
# From Exploration: Insert data
cur.execute('INSERT INTO reviews(name,review,rating)'
            'VALUES(%s,%s,%s)'
            ('Fox Mulder','Loved the pizza!',5))

cur.execute('INSERT INTO reviews(name,review,rating)'
            'VALUES(%s,%s,%s)'
            ('Xavier File','Great dessert choices!',4))

# Commit the transaction to save the changes
conn.commit()


# From exploration: Select data





#Close the cursor and connection
cur.close()
conn.close()
