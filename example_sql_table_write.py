#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
import time

def convert_image_to_blob(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def write_to_table(id, date_time, photo, photo_name):
    print("Inserting BLOB into python_employee table")
    try:
        connection = mysql.connector.connect(host='3.15.202.90',
                                             database='timelapse',
                                             user='rpi',
                                             password='N2IThmNTxYmC9oXN')
        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO photos
                          (id, date_time, image, photo_name) VALUES (%s,%s,%s,%s)"""

        photo_long_blob = convert_image_to_blob(photo)

        # Convert data into tuple format
        insert_blob_tuple = (id, date_time, photo_long_blob, photo_name)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

id = 0
date_time = time.strftime('%Y-%m-%d %H:%M:%S')
photo = "./garden.jpeg"
photo_name = "example_pic"

write_to_table(id, date_time, photo, photo_name)
