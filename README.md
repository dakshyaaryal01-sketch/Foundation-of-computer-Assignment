# College Club Membership Database

## Project Overview

This project demonstrates the design of a normalized relational database for managing student club memberships in a college environment. The objective is to improve data organization, reduce redundancy, and maintain data consistency compared to the previous single-table system used by the college.

The system separates student information, club information, and membership records into multiple related tables. This structure follows database normalization principles to improve data integrity and efficiency.

---

## Problem Description

The college initially stored all club membership information in a single table. While this approach was simple, it caused several issues:

* **Data redundancy** – Student and club information were repeated multiple times.
* **Update anomalies** – Changing club details required updating many rows.
* **Insertion anomalies** – A club could not be added unless a student joined it.
* **Deletion anomalies** – Removing a student could accidentally remove club data.

To solve these problems, the database structure was redesigned using normalization techniques.

---

## Database Design

The improved database design separates information into three main tables:

### 1. Student Table

Stores basic information about students.

Attributes include:

* StudentID
* StudentName
* Email

Each student has a unique **StudentID**, which serves as the primary key.

---

### 2. Club Table

Stores information related to college clubs.

Attributes include:

* ClubID
* ClubName
* ClubRoom
* ClubMentor

Each club has a unique **ClubID**, which identifies it in the system.

---

### 3. Membership Table

This table connects students with clubs and records when they joined.

Attributes include:

* MembershipID
* StudentID
* ClubID
* JoinDate

The table uses foreign keys to reference the Student and Club tables.

---

## Technologies Used

* MySQL / SQL Database
* GitHub for version control
* Markdown documentation

---

## How to Run the SQL File

1. Open **MySQL Workbench**, **phpMyAdmin**, or any SQL client.

2. Create a new database.

3. Select the database using the SQL command:

   USE CollegeClubDB;

4. Run the provided SQL script to create the tables and insert sample data.

5. Verify the tables using:

   SELECT * FROM Student;
   SELECT * FROM Club;
   SELECT * FROM Membership;

---

## Folder Structure

```
project-folder
│
├── README.md
├── database.sql
└── report.pdf
```

* **README.md** – Project description and instructions
* **database.sql** – SQL script containing table creation and sample data
* **report.pdf** – Written assignment report

---

## Learning Outcomes

This project demonstrates:

* Understanding of relational database design
* Application of normalization principles
* Creation of primary and foreign key relationships
* Implementation of SQL database structures

---

## Author

Dakshya Aryal
Student – Softwarica College of IT & E-commerce
Affiliated with Coventry University
