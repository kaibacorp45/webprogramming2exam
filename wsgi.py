import click
from flask import Flask
from App import create_db, db, app
from App import Book
import csv

@app.cli.command("init")
def initialize():
    create_db(app)
    print('database intialized')
    book_list = []
    with open('books.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        isbnB = ""
        book_title = ""
        book_author = ""
        year = ""
        publisherN = ""
        image_s = ""
        image_m = ""
        image_l = ""
        
        for line in csv_reader:
            isbnB = line['ISBN']
            if isbnB == "":
                isbnB = None
    
            book_title = line['Book-Title']
            if book_title =="":
                 book_title = None
            
            book_author = line['Book-Author']
            if book_author == "":
                book_author = None
    
            year = line['Year-Of-Publication']
            if year == "":
                year = None
    
            publisherN = line['Publisher']
            if publisherN =="":
                publisherN = None
            
            image_s = line['Image-URL-S']
            if image_s =="":
                image_s = None
    
            image_m = line['Image-URL-M']
            if image_m =="":
                image_m = None
    
            image_l = line['Image-URL-L']
            if image_l =="":
                image_l = None
    
            book_list.append(Book(isbn = isbnB, title = book_title, author = book_author, publication_year = year, publisher = publisherN))

        for b in book_list:
          db.session.add(b)
        db.session.commit()
          
