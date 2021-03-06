import csv
from datetime import datetime, timedelta

if __name__ == "__main__":
    with open('data/books.csv', 'r') as infile, open('data/books_copy.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        outfile.write(next(infile))
        for row in csv.reader(infile):
            dt = datetime.strptime(row[10], "%m/%d/%y")
            if dt > datetime.now():
                dt = dt.replace(year=dt.year-100)
            row[10] = dt.date()
            writer.writerow(row)


# This section of the file is no longer needed because we used the postgres image's /docker-entrypoint-initdb.d to
# initialise the database with our csv data
#
# import csv
# from sqlalchemy import create_engine, text, Table, MetaData, Column, String, Integer, Float
#
# engine = create_engine("postgresql+psycopg2://goodreads:goodreads@localhost:5432/goodreads")
# conn = engine.connect()
#
# def create_tables():
#     metadata = MetaData()
#     books = Table("books", metadata,
#         Column("id", Integer, primary_key = True),
#         Column("title", String),
#         Column("authors", String),
#         Column("average_rating", Float),
#         Column("publication_date", String),
#         Column("publisher", String)
#     )
#     metadata.create_all(engine)
#
# def delete_tables():
#     conn.execute("DROP TABLE books")
#
# class Book:
#     def __init__(self, id, title, authors, average_rating, publication_date, publisher):
#         self.id = id
#         self.title = title
#         self.authors = authors
#         self.average_rating = average_rating
#         self.publication_date = publication_date
#         self.publisher = publisher
#
# if __name__ == "__main__":
#     delete_tables()
#     create_tables()
#     with open("data/books.csv", "r") as file:
#         reader = csv.reader(file, skipinitialspace=True)
#         next(reader)  # skip first row
#         for row in reader:
#             book = {
#                 "id": row[0],
#                 "title": row[1],
#                 "authors": row[2],
#                 "average_rating": row[3],
#                 "publication_date": row[10],
#                 "publisher": row[11],
#             }
#             statement = text("INSERT INTO books VALUES (:id, :title, :authors, :average_rating, :publication_date, :publisher)")
#             conn.execute(statement, book)