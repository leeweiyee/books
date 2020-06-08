COPY books
FROM '/data/books_copy.csv'
DELIMITER ',' CSV HEADER;