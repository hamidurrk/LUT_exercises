-- Query 1
SELECT * FROM student WHERE sdept IS NULL;

-- Query 2
SELECT sname, sdept, sage FROM student WHERE sage NOT BETWEEN 19 AND 22;

-- Query 3
SELECT COUNT(*) AS total_enrollments FROM sc;

-- Query 4
SELECT cname, cno, credit 
FROM course 
WHERE cname LIKE 'DB\_%i__' ESCAPE '\';

-- Query 5
SELECT cno FROM sc 
GROUP BY cno 
HAVING COUNT(*) > 100;

-- Query 6
SELECT sno, AVG(grade) AS average_score 
FROM sc 
GROUP BY sno 
HAVING AVG(grade) > 80;

-- Query 7
SELECT c.cname 
FROM course c 
JOIN sc ON c.cno = sc.cno 
WHERE sc.sno = '20200001';

-- Query 8
SELECT cno, AVG(grade) AS average_score 
FROM sc 
GROUP BY cno 
ORDER BY average_score DESC;