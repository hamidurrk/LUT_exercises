-- exercise 2 --

-- Answer to the question 1
CREATE OR REPLACE VIEW IS_students AS
SELECT *
FROM student
WHERE sdept = 'IS';

-- Answer to the question 2
CREATE OR REPLACE VIEW IS_F_students AS
SELECT *
FROM IS_students
WHERE sgender = 'F'
WITH CASCADED CHECK OPTION;

-- Answer to the question 3
INSERT INTO IS_F_students (sno, sname, sage, sgender, sdept)
VALUES ('20200007', 'Amy', 19, 'F', 'IS');

-- Answer to the question 4
SELECT f.sno, f.sname, sc.cno, sc.grade
FROM IS_F_students AS f
JOIN sc ON f.sno = sc.sno;

-- Answer to the question 5
ALTER TABLE student
RENAME COLUMN sno TO sid;

-- Answer to the question 6
ALTER TABLE sc
ADD COLUMN id SERIAL;

-- Answer to the question 7
ALTER TABLE course
DROP COLUMN cno;

-- Answer to the question 8

-- According to the lecture instructions:
-- 1) Retrieving definitions
\d student 
\d sc 

-- 2) Checking referential constraints
-- -- Let's assume that the foreign key constraint is named as "sc_sno_fkey"

-- 3) Listing all programs accessing the table
-- -- Let's assume no program is accessing the table since it is not mentioned in the question.

-- 4) Unloading the data and dropping the table
-- -- a) Dropping foreign key constraint
ALTER TABLE sc
DROP CONSTRAINT sc_sno_fkey;
-- -- b) Unloading the data in a backup table
CREATE TABLE student_backup AS
SELECT *
FROM student;
-- -- c) Dropping the table
DROP TABLE student;

-- 5) Recreating the table adding the new column
CREATE TABLE student (
    sno         CHAR(8)      NOT NULL,   -- or primary key
    sname       VARCHAR(50),
    sage        INT,
    enrollment  INT DEFAULT 2023,  -- new column
    sgender     CHAR(1),
    sdept       VARCHAR(10),
    CONSTRAINT student_pkey PRIMARY KEY (sno)
);

-- 6) Uploading the data from the backup table to the new table
INSERT INTO student (sno, sname, sage, sgender, sdept)
SELECT sno, sname, sage, sgender, sdept
FROM student_backup;

-- 7) Re-creating the foreign key constraint
ALTER TABLE sc
ADD CONSTRAINT sc_sno_fkey
FOREIGN KEY (sno) REFERENCES student(sno);

-- (Optional) Dropping the backup table
DROP TABLE student_backup;

-- End of the answer to the question 8 --

-- Alternative solution to the question 8 (INCLUDED BUT NOT LIMITED TO MYSQL)
-- -- MySQL supports AFTER syntax for adding columns after a specific column
ALTER TABLE student
ADD COLUMN enrollment INT DEFAULT 2023 AFTER sage;
