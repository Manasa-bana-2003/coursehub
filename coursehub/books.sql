CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  description TEXT UNIQUE,
  author VARCHAR(255) NOT NULL,
  availability BOOLEAN NOT NULL,
  edition VARCHAR(255) NOT NULL,
  count INT NOT NULL
);


INSERT INTO books (name, description, author, availability, edition, count)
 VALUES
('101 Ways To Be A Software Engineer', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aut repudiandae assumenda distinctio quas tempore, voluptatibus accusamus dolores temporibus, recusandae eligendi similique. Optio, eius? Sint vel nemo, quisquam architecto fugit odio!', 'Mr. Johnny Test', TRUE, '1', 3),
('JAVA For Absolute Beginners', 'Step into the basics of java programming along with globally famed programmer', '', TRUE, '1', 5),
('Python for beginners','The basic knowledge of python will be learned form this book','Guido van rossum', TRUE,'3', 10 );
