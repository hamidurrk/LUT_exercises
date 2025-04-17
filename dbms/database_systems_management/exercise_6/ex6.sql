-- exercise 6 --
-- Answer to the question 1
CREATE ROLE owner LOGIN;
CREATE ROLE manager LOGIN;
CREATE ROLE users LOGIN;

-- Answer to the question 2
GRANT ALL PRIVILEGES ON TABLE student TO owner WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON TABLE student TO manager WITH GRANT OPTION;

-- Answer to the question 3
GRANT SELECT ON TABLE student TO users;
-- N.B. We will have to execute this as the manager role
SET ROLE manager;

-- Answer to the question 4
CREATE ROLE tom LOGIN VALID UNTIL '2026-01-01';
CREATE ROLE jerry LOGIN VALID UNTIL '2026-01-01';
CREATE ROLE spike LOGIN VALID UNTIL '2026-01-01';

-- Answer to the question 5
GRANT UPDATE ON TABLE student TO tom; -- Also executed as manager

-- Answer to the question 6
GRANT manager TO jerry WITH ADMIN OPTION;

-- Answer to the question 7
SET ROLE jerry; -- Switching to jerry temporarily

GRANT manager TO spike;

RESET ROLE; -- Switching back to the original role

-- Answer to the question 8
REVOKE INSERT, UPDATE, DELETE ON student FROM manager CASCADE;

-- Answer to the question 9
REVOKE ADMIN OPTION FOR manager FROM jerry;

-- Answer to the question 10
REVOKE manager FROM jerry;