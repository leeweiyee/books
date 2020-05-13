COPY books
FROM '/data/books.csv'
DELIMITER ',' CSV HEADER;