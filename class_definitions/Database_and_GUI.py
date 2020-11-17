"""
Author: Elijah Morishita
elmorishita@dmacc.edu
11/16/2020
This program places a database from a GUI
"""

import sqlite3
import tkinter as tk
from tkinter import messagebox
from sqlite3 import Error

window = tk.Tk()  # Creates a window




def onButtonClick():

    def create_connection(db):
        """ Connect to a SQLite database
        :param db: filename of database
        :return connection if no error, otherwise None"""
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as err:
            print(err)
        return None


    def select_all_persons(conn):
        """Query all rows of person table
        :param conn: the connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM person")

        rows = cur.fetchall()

        return rows # return the rows

    def select_all_students(conn):
        """Query all rows of person table
        :param conn: the connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM student")

        rows = cur.fetchall()

        return rows # return the rows

    conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)
    with conn:
        rows = select_all_students(conn)
        for row in rows:
            print(row)

def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    firstname = tk.Entry(window)
    firstname.pack()

    lastname = tk.Entry(window)
    lastname.pack()
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    firstname = tk.Entry(window)
    firstname.pack()

    lastname = tk.Entry(window)
    lastname.pack()

    major = tk.Entry(window)
    major.pack()

    start_date = tk.Text(window)
    start_date.pack()


    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid # returns the row id of the cursor object, the student id


button1 = tk.Button(text="Create Database & Table", command=lambda: onButtonClick())
button1.pack(fill=tk.Y, side=tk.LEFT)

button2 = tk.Button(text="View Person Table", command=lambda: create_person())
button2.pack(fill=tk.Y, side=tk.LEFT)

button3 = tk.Button(text="View Student Table", command=lambda: create_student())
button3.pack(fill=tk.Y, side=tk.LEFT)


def quit():
    tk.Button(window, text="Quit", command=window.destroy).pack()

button4 = tk.Button(text="Exit", command=lambda: quit())
button4.pack(fill=tk.Y, side=tk.LEFT)


tk.mainloop()

window.mainloop()
