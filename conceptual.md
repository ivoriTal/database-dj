### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  PostgreSQL is an open-source, advanced object-relational database management system (RDBMS).

- What is the difference between SQL and PostgreSQL?
  SQL is a standard language for managing relational databases, while PostgreSQL is a specific RDBMS that implements and extends SQL.

- In `psql`, how do you connect to a database?
  Use the command: `\c database_name`

- What is the difference between `HAVING` and `WHERE`?
  `WHERE` filters individual rows before grouping, while `HAVING` filters grouped results after grouping.

- What is the difference between an `INNER` and `OUTER` join?
  `INNER` join returns only matching rows from both tables, while `OUTER` join returns all rows from one or both tables, including non-matches.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  `LEFT OUTER` keeps all rows from the left table, while `RIGHT OUTER` keeps all rows from the right table.

- What is an ORM? What do they do?
  ORM (Object-Relational Mapping) is a technique that lets you query and manipulate data from a database using an object-oriented paradigm.

- What are some differences between making HTTP requests using AJAX and from the server side using a library like `requests`?
  - AJAX: Client-side, asynchronous, limited by browser security
  - Server-side: Server-side, synchronous, not limited by browser security

- What is CSRF? What is the purpose of the CSRF token?
  CSRF (Cross-Site Request Forgery) is an attack that forces users to perform unwanted actions. CSRF tokens prevent this by ensuring requests come from your site.

- What is the purpose of `form.hidden_tag()`?
  It generates hidden form fields, including the CSRF token, to protect against CSRF attacks in Flask-WTF forms.
