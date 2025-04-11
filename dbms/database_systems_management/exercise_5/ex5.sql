-- exercise 5 --
-- Answer to the question 1
CREATE OR REPLACE FUNCTION check_max_courses()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    course_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO course_count
    FROM sc
    WHERE sno = NEW.sno;

    IF course_count >= 10 THEN
        RAISE EXCEPTION 'Student % has already enrolled in 10 courses', NEW.sno;
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_max_courses
BEFORE INSERT ON sc
FOR EACH ROW
EXECUTE FUNCTION check_max_courses();

-- Answer to the question 2
CREATE OR REPLACE FUNCTION check_ma_database()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
DECLARE
    dept VARCHAR(10);
    course_name VARCHAR(50);
BEGIN
    SELECT sdept INTO dept FROM student WHERE sno = NEW.sno;
    SELECT Chame INTO course_name FROM course WHERE Cno = NEW.cno;

    IF dept = 'MA' AND course_name = 'database' THEN
        RAISE EXCEPTION 'MA students are not allowed to enroll in the database course';
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_block_ma_database
BEFORE INSERT ON sc
FOR EACH ROW
EXECUTE FUNCTION check_ma_database();

-- Answer to the question 3
CREATE OR REPLACE FUNCTION enforce_min_credits()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    IF NEW.Ccredit < 2 THEN
        NEW.Ccredit := 2;
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_min_credits
BEFORE INSERT OR UPDATE ON course
FOR EACH ROW
EXECUTE FUNCTION enforce_min_credits();

-- Answer to the question 4
CREATE OR REPLACE FUNCTION log_grade_changes()
RETURNS TRIGGER
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO grade_log (sno, cno, oldgrade, newgrade, datetime)
    VALUES (
        COALESCE(NEW.sno, OLD.sno),
        COALESCE(NEW.cno, OLD.cno),
        OLD.grade,
        NEW.grade,
        CURRENT_TIMESTAMP
    );
    RETURN NEW;
END;
$$;

CREATE TRIGGER trg_grade_log
AFTER INSERT OR UPDATE ON sc
FOR EACH ROW
EXECUTE FUNCTION log_grade_changes();