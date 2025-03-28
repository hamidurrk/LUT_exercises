-- exercise 3 --

-- Answer to the question 1
-- -- a
CREATE TABLE orders_2021h1 PARTITION OF Orders
    FOR VALUES FROM ('2021-01-01') TO ('2021-07-01');
-- -- b
CREATE TABLE orders_2021h2 PARTITION OF Orders
    FOR VALUES FROM ('2021-07-01') TO ('2022-01-01');
-- -- c
CREATE TABLE orders_2022h1 PARTITION OF Orders
    FOR VALUES FROM ('2022-01-01') TO ('2022-07-01');
-- -- d
CREATE TABLE orders_2022h2 PARTITION OF Orders
    FOR VALUES FROM ('2022-07-01') TO ('2023-01-01');
-- N.B. The lower bound is inclusive and the upper bound is exclusive

-- Answer to the question 2
ALTER TABLE orders_2021h2 
    ADD CONSTRAINT shippeddate_not_null CHECK (shippeddate IS NOT NULL);

-- Answer to the question 3
ALTER TABLE orders_2022h1 
    ADD CONSTRAINT freight_positive CHECK (freight > 0::MONEY);

-- Answer to the question 4
-- Main partition for 2023h1
CREATE TABLE orders_2023h1 PARTITION OF Orders
    FOR VALUES FROM ('2023-01-01') TO ('2023-07-01')
    PARTITION BY LIST (shipcountry);

-- Subpartitions under orders_2023h1
-- -- a
CREATE TABLE orders_2023h1_na PARTITION OF orders_2023h1
    FOR VALUES IN ('USA', 'CANADA');
-- -- b
CREATE TABLE orders_2023h1_eu PARTITION OF orders_2023h1
    FOR VALUES IN ('Germany', 'Finland');
-- -- c
CREATE TABLE orders_2023h1_default PARTITION OF orders_2023h1
    DEFAULT;

-- Answer to the question 5
ALTER TABLE Orders 
    ADD CONSTRAINT Orders_pk PRIMARY KEY (orderid);