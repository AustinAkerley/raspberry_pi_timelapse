#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error

def convert_blob_to_image(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

def write_from_table(id, photo_name):
    print("Reading BLOB data from python_employee table")

    try:
        connection = mysql.connector.connect(host='3.15.202.90',
                                             database='timelapse',
                                             user='rpi',
                                             password='N2IThmNTxYmC9oXN')

        cursor = connection.cursor()
        sql_fetch_blob_query = """SELECT * from photos where id = %s"""

        cursor.execute(sql_fetch_blob_query, (id,))
        record = cursor.fetchall()
        print("hi")
        for row in record:
            print("Id = ", row[0], )
            print("date_time = ", row[1])
            image = row[2]
            print("Storing employee image and bio-data on disk \n")
            convert_blob_to_image(image, photo_name)

    except mysql.connector.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


write_from_table(1, "garden.jpeg")
