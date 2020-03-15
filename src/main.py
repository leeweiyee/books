import csv

class Book:
    def __init__(self, id, title, authors, average_rating, publication_date, publisher):
        self.id = id
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.publication_date = publication_date
        self.publisher = publisher

if __name__ == "__main__":
    with open("data/books.csv", "r") as file:
        reader = csv.reader(file)
        next(reader) # skip first row
        for row in reader:
            book = Book(
                id=row[0],
                title=row[1],
                authors=row[2],
                average_rating=row[3],
                publication_date=row[10],
                publisher=row[11],
            )
            print(book)