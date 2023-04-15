DROP TABLE books;
DROP TABLE authors;

CREATE TABLE authors(
    id SERIAL Primary Key, 
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);


CREATE TABLE books(
    id SERIAL PRIMARY KEY, 
    title VARCHAR(255),
    author_id INT NOT NULL REFERENCES authors(id) ON DELETE CASCADE,
    genre VARCHAR(255),
    quantity INT,
    buying_price FLOAT,
    selling_price FLOAT,
    language VARCHAR(255)
);

