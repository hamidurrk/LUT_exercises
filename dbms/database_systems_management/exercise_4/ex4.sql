-- exercise 4 --

-- Answer to the question 1
CREATE OR REPLACE PROCEDURE get_total_credits(
    IN student_no CHAR(8),
    OUT total_credits SMALLINT
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT COALESCE(SUM(C.Ccredit), 0) INTO total_credits
    FROM sc
    JOIN course C ON sc.cno = C.Cno
    WHERE sc.sno = student_no;
END;
$$;

-- Answer to the question 2
CREATE OR REPLACE PROCEDURE increase_grades()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE sc
    SET grade = LEAST(ROUND(grade * 1.1), 100)::SMALLINT;
END;
$$;

-- Answer to the question 3
CREATE OR REPLACE PROCEDURE convert_grades_to_5_point()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE sc
    SET grade = CASE
        WHEN grade >= 90 AND grade <= 100 THEN 5
        WHEN grade >= 80 AND grade < 90 THEN 4
        WHEN grade >= 70 AND grade < 80 THEN 3
        WHEN grade >= 60 AND grade < 70 THEN 2
        WHEN grade >= 50 AND grade < 60 THEN 1
        WHEN grade >= 0 AND grade < 50 THEN 0
        ELSE NULL
    END;
END;
$$;





-- Answer to the question 4
CREATE OR REPLACE FUNCTION get_total_credits_func(student_no CHAR(8))
RETURNS SMALLINT
LANGUAGE plpgsql
AS $$
DECLARE
    total SMALLINT;
BEGIN
    SELECT COALESCE(SUM(C.Ccredit), 0) INTO total
    FROM sc
    JOIN course C ON sc.cno = C.Cno
    WHERE sc.sno = student_no;
    RETURN total;
END;
$$;