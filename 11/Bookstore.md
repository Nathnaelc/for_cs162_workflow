### Online Bookstore and Inventory Management

- **Book** table: Stores information about books in the inventory.
- **Customer** table: Stores information about customers.
- **Order** table: Records customer orders.
- **OrderDetail** table: Stores details of items in each order.

[![Online Bookstore app](https://mermaid.ink/img/pako:eNqNUsuOwyAM_BXkc_sDHPdx7KnXSJUFboLCowLnsEr77-uUtEq3HNYX7LGxZ8AzmGQJNFD-cthnDF1UYh8pjep63e_TrD6nwilQVloNWDb5WdVgscLZxV6xY0_vME48pPyO9xTztvzsE7K6ZGe2qIssF5IZV-xWjyevBo-IoUGDAjr_p4nHUh5KjzxZkmEboTXfmGCWxKk9x0VxJsNPyeuwR_9Gu1JTp38Qhx2IakGs_Nu8gB3wQIE60OJazGMHXVzq5N3T8Sca0MKHdjBdLDKtP_0KflsnfEGf0RcB6R4e6nLcd-T2C5h6q_o?type=png)](https://mermaid.live/edit#pako:eNqNUsuOwyAM_BXkc_sDHPdx7KnXSJUFboLCowLnsEr77-uUtEq3HNYX7LGxZ8AzmGQJNFD-cthnDF1UYh8pjep63e_TrD6nwilQVloNWDb5WdVgscLZxV6xY0_vME48pPyO9xTztvzsE7K6ZGe2qIssF5IZV-xWjyevBo-IoUGDAjr_p4nHUh5KjzxZkmEboTXfmGCWxKk9x0VxJsNPyeuwR_9Gu1JTp38Qhx2IakGs_Nu8gB3wQIE60OJazGMHXVzq5N3T8Sca0MKHdjBdLDKtP_0KflsnfEGf0RcB6R4e6nLcd-T2C5h6q_o)

This application serves as an online bookstore and inventory management system. It enables customers to browse and purchase books, while also allowing administrators to manage the inventory, track orders, and handle customer data. It provides a seamless shopping experience for book enthusiasts and efficient inventory control for the bookstore.

Question 1: What are the titles and prices of all books in the "Science Fiction" genre?

-- Answer to Question 1:
SELECT title, price
FROM Book
WHERE genre = 'Science Fiction';

| title | price |
| ----- | ----- |
| Dune  | 22.50 |

Question 2: How many books have been ordered in total?

-- Answer to Question 2:
SELECT SUM(quantity) as total_books_ordered
FROM OrderDetail;

| total_books_ordered |
| ------------------- |
| 8                   |

Question 3: List the names and email addresses of customers who made orders on a specific date.

-- Answer to Question 3:
SELECT C.name, C.email
FROM Customer C
INNER JOIN "Order" O ON C.id = O.customerId
WHERE O.date = '2023-10-10';

| name         | email            |
| ------------ | ---------------- |
| Mera Johnson | Mera@example.com |
