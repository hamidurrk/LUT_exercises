
-- ----------------------- Answer to the question 1 of exercise 3 -----------------------

-- Query 1
SELECT s.sno, s.sname  
FROM student s  
JOIN sc ON s.sno = sc.sno  
WHERE sc.cno = '2' AND sc.grade >= 90;  

-- Query 2
SELECT a.cno AS course, b.cpno AS indirect_prerequisite  
FROM course a  
JOIN course b ON a.cpno = b.cno  
WHERE b.cpno IS NOT NULL;  

-- Query 3
SELECT s.sno, s.sname, c.cname, sc.grade  
FROM student s  
JOIN sc ON s.sno = sc.sno  
JOIN course c ON sc.cno = c.cno;  

-- Query 4
SELECT cno, cname, credit  
FROM course  
WHERE cname LIKE 'DB\_%g_' ESCAPE '\';  

-- Query 5
SELECT s.sno, s.sname  
FROM student s  
JOIN sc ON s.sno = sc.sno  
JOIN course c ON sc.cno = c.cno  
WHERE c.cname = 'Information System';  

-- Query 6
SELECT sc.sno, sc.cno  
FROM sc  
WHERE grade > (  
    SELECT AVG(grade) FROM sc AS sub  
    WHERE sub.sno = sc.sno  
);  

-- Query 7
SELECT s.sname  
FROM student s  
JOIN sc sc1 ON s.sno = sc1.sno AND sc1.cno = '1'  
JOIN sc sc2 ON s.sno = sc2.sno AND sc2.cno = '2';  


-- Query 8
SELECT c.cname, COUNT(*) AS enrollments  
FROM course c  
JOIN sc ON c.cno = sc.cno  
GROUP BY c.cno  
HAVING COUNT(*) > 100;  

-- Query 9
SELECT c.cname  
FROM course c  
WHERE NOT EXISTS (  
    SELECT s.sno FROM student s  
    WHERE NOT EXISTS (  
        SELECT * FROM sc  
        WHERE sc.sno = s.sno AND sc.cno = c.cno  
    )  
);  

-- Query 10
SELECT sname FROM student WHERE sdept = 'CS'  
UNION  
SELECT sname FROM student WHERE sage < 19;  

-- Query 11
SELECT sname FROM student WHERE sdept = 'CS'  
EXCEPT  
SELECT sname FROM student WHERE sage <= 19;  

-- Query 12
SELECT sname FROM student  
WHERE sno IN (  
    SELECT sno FROM sc WHERE cno = '1'  
    INTERSECT  
    SELECT sno FROM sc WHERE cno = '2'  
);  
















-- ----------------------- Answer to the question 2 of exercise 3 -----------------------

-- Student Table
CREATE TABLE IF NOT EXISTS student (  
    sno CHAR(8) PRIMARY KEY,  
    sname VARCHAR(10) NOT NULL,  
    sage INT,  
    sgender CHAR(1),  
    sdept VARCHAR(10)  
);  

-- Course Table
CREATE TABLE IF NOT EXISTS course (  
    cno CHAR(4) PRIMARY KEY,  
    cname VARCHAR(50) NOT NULL,  
    cpno CHAR(4),  
    credit SMALLINT  
);  

-- SC Table  
CREATE TABLE IF NOT EXISTS sc (  
    sno CHAR(8) REFERENCES student(sno),  
    cno CHAR(4) REFERENCES course(cno),  
    grade SMALLINT,  
    PRIMARY KEY (sno, cno)  
);  
























-- ----------------------- Answer to the question 3 of exercise 3 -----------------------

-- Query 1
INSERT INTO student (sno, sname, sgender, sage, sdept)  
VALUES ('20200011', 'Mike', 'M', 20, 'IS');  

-- Query 2
INSERT INTO sc (sno, cno, grade)  
VALUES ('20200011', '1', NULL);  

-- Query 3
INSERT INTO Dept_age (Sdept, Avg_age)  
SELECT sdept, AVG(sage)  
FROM student  
GROUP BY sdept;  

-- Query 4
UPDATE student  
SET sage = 22, sdept = 'MA'  
WHERE sno = '20200011';  

-- Query 5
UPDATE sc  
SET grade = 0  
WHERE sno IN (  
    SELECT sno FROM student WHERE sdept = 'CS'  
);  

-- Query 6
DELETE FROM sc  
WHERE sno IN (  
    SELECT sno FROM student WHERE sdept = 'CS'  
);   

-- Query 7
CREATE VIEW Student_Stats AS  
SELECT  
    s.sno,  
    s.sname,  
    COUNT(sc.cno) AS num_courses,  
    AVG(sc.grade) AS avg_grade,  
    SUM(c.credit) AS total_credits  
FROM student s  
LEFT JOIN sc ON s.sno = sc.sno  
LEFT JOIN course c ON sc.cno = c.cno  
GROUP BY s.sno, s.sname;  