-- Display all students
SELECT * FROM Student;

-- Display all clubs
SELECT * FROM Club;

-- Insert a new student
INSERT INTO Student VALUES (8, 'Kiran', 'kiran@email.com');

-- Insert a new club
INSERT INTO Club VALUES (5, 'Art Club', 'R404', 'Ms. Tara');

-- JOIN Query: Show Student Name, Club Name, Join Date
SELECT 
    Student.StudentName,
    Club.ClubName,
    Membership.JoinDate
FROM Membership
JOIN Student ON Membership.StudentID = Student.StudentID
JOIN Club ON Membership.ClubID = Club.ClubID;
