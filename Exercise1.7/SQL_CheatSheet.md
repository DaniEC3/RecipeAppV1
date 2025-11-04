# SQL Essential Commands Cheat Sheet

A comprehensive reference guide for MySQL/SQL commands.

---

## 📁 DATABASE OPERATIONS

```sql
-- List all databases
SHOW DATABASES;

-- Create a new database
CREATE DATABASE database_name;

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS database_name;

-- Select/use a database
USE database_name;

-- Delete a database (BE CAREFUL!)
DROP DATABASE database_name;

-- Drop database if it exists
DROP DATABASE IF EXISTS database_name;

-- Show current database
SELECT DATABASE();
```

---

## 📊 TABLE OPERATIONS

```sql
-- List all tables in current database
SHOW TABLES;

-- List tables from another database (without USE)
SHOW TABLES FROM database_name;

-- Describe table structure
DESCRIBE table_name;
-- or
DESC table_name;

-- Show table structure with full CREATE statement
SHOW CREATE TABLE table_name;

-- Show columns from a table
SHOW COLUMNS FROM table_name;
SHOW COLUMNS FROM database_name.table_name;

-- Show indexes on a table
SHOW INDEX FROM table_name;

-- Show table status/info
SHOW TABLE STATUS FROM database_name;
SHOW TABLE STATUS LIKE 'table_name';

-- Get detailed column information
SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'database_name' 
AND TABLE_NAME = 'table_name';
```

---

## 🏗️ CREATE TABLE (DDL - Data Definition Language)

```sql
-- Create a table
CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS table_name (...);

-- Alter table - Add column
ALTER TABLE table_name ADD COLUMN column_name VARCHAR(50);

-- Alter table - Drop column
ALTER TABLE table_name DROP COLUMN column_name;

-- Alter table - Modify column
ALTER TABLE table_name MODIFY COLUMN column_name VARCHAR(100);

-- Alter table - Rename column
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;

-- Rename table
RENAME TABLE old_name TO new_name;

-- Drop table
DROP TABLE table_name;

-- Drop table if exists
DROP TABLE IF EXISTS table_name;

-- Truncate table (delete all rows, keep structure)
TRUNCATE TABLE table_name;
```

---

## 📝 INSERT DATA (DML - Data Manipulation Language)

```sql
-- Insert single row
INSERT INTO table_name (column1, column2, column3)
VALUES ('value1', 'value2', value3);

-- Insert multiple rows
INSERT INTO table_name (column1, column2, column3)
VALUES 
    ('value1', 'value2', value3),
    ('value4', 'value5', value6),
    ('value7', 'value8', value9);

-- Insert with all columns (in order)
INSERT INTO table_name VALUES (value1, 'value2', value3);

-- Insert from another table
INSERT INTO table_name1 (column1, column2)
SELECT column1, column2 FROM table_name2;
```

---

## 🔍 SELECT QUERIES (DQL - Data Query Language)

### Basic SELECT

```sql
-- Select all columns from a table
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2, column3 FROM table_name;

-- Select with WHERE condition
SELECT * FROM table_name WHERE column1 = 'value';

-- Select with multiple conditions (AND)
SELECT * FROM table_name 
WHERE column1 = 'value' AND column2 > 100;

-- Select with OR condition
SELECT * FROM table_name 
WHERE column1 = 'value1' OR column1 = 'value2';
```

### Advanced WHERE Clauses

```sql
-- IN clause
SELECT * FROM table_name WHERE column1 IN ('value1', 'value2', 'value3');

-- LIKE (pattern matching)
SELECT * FROM table_name WHERE name LIKE 'John%';  -- Starts with
SELECT * FROM table_name WHERE name LIKE '%John';  -- Ends with
SELECT * FROM table_name WHERE name LIKE '%John%'; -- Contains

-- BETWEEN
SELECT * FROM table_name WHERE age BETWEEN 18 AND 65;

-- NULL check
SELECT * FROM table_name WHERE column1 IS NULL;
SELECT * FROM table_name WHERE column1 IS NOT NULL;
```

### Aggregations

```sql
-- Count rows
SELECT COUNT(*) FROM table_name;

-- Count with condition
SELECT COUNT(*) FROM table_name WHERE column1 = 'value';

-- Count distinct values
SELECT COUNT(DISTINCT column1) FROM table_name;

-- Aggregate functions
SELECT 
    COUNT(*) AS total,
    AVG(column1) AS average,
    SUM(column1) AS sum_total,
    MIN(column1) AS minimum,
    MAX(column1) AS maximum
FROM table_name;
```

### GROUP BY & HAVING

```sql
-- GROUP BY
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1;

-- HAVING (filter groups)
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1 
HAVING COUNT(*) > 5;
```

### Sorting & Limiting

```sql
-- ORDER BY
SELECT * FROM table_name ORDER BY column1 ASC;   -- Ascending
SELECT * FROM table_name ORDER BY column1 DESC;  -- Descending
SELECT * FROM table_name ORDER BY column1, column2;  -- Multiple columns

-- LIMIT
SELECT * FROM table_name LIMIT 10;        -- First 10 rows
SELECT * FROM table_name LIMIT 10 OFFSET 5;  -- Skip 5, take 10

-- Aliases
SELECT column1 AS alias_name, column2 AS another_alias FROM table_name;
```

### DISTINCT

```sql
-- Select DISTINCT values
SELECT DISTINCT column1 FROM table_name;
```

---

## ✏️ UPDATE DATA (DML)

```sql
-- Update single row
UPDATE table_name 
SET column1 = 'new_value', column2 = 100
WHERE id = 1;

-- Update multiple rows
UPDATE table_name 
SET column1 = 'new_value'
WHERE column2 = 'condition';

-- Update with calculation
UPDATE table_name 
SET column1 = column1 + 10
WHERE id = 1;

-- ⚠️  WARNING: Always use WHERE clause! Without it, updates ALL rows!
```

---

## 🗑️ DELETE DATA (DML)

```sql
-- Delete specific rows
DELETE FROM table_name WHERE id = 1;

-- Delete with condition
DELETE FROM table_name WHERE column1 = 'value';

-- Delete multiple rows
DELETE FROM table_name WHERE column1 IN ('value1', 'value2');

-- ⚠️  WARNING: Always use WHERE clause! Without it, deletes ALL rows!
```

---

## 🔗 JOINS

```sql
-- INNER JOIN (only matching rows)
SELECT * FROM table1
INNER JOIN table2 ON table1.id = table2.table1_id;

-- LEFT JOIN (all from left, matching from right)
SELECT * FROM table1
LEFT JOIN table2 ON table1.id = table2.table1_id;

-- RIGHT JOIN (all from right, matching from left)
SELECT * FROM table1
RIGHT JOIN table2 ON table1.id = table2.table1_id;

-- FULL OUTER JOIN (all from both) - MySQL doesn't support, use UNION
SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.table1_id
UNION
SELECT * FROM table1 RIGHT JOIN table2 ON table1.id = table2.table1_id;
```

---

## 🔐 CONSTRAINTS & INDEXES

```sql
-- Primary Key
CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ...
);

-- Foreign Key
CREATE TABLE table1 (
    id INT PRIMARY KEY,
    FOREIGN KEY (other_id) REFERENCES table2(id)
);

-- Unique constraint
ALTER TABLE table_name ADD UNIQUE (column_name);

-- Index
CREATE INDEX index_name ON table_name (column_name);

-- Drop index
DROP INDEX index_name ON table_name;
```

---

## 📋 USEFUL UTILITY COMMANDS

```sql
-- Show current user
SELECT USER();

-- Show MySQL version
SELECT VERSION();

-- Show current time
SELECT NOW();
SELECT CURDATE();  -- Current date
SELECT CURTIME();  -- Current time

-- Show process list (running queries)
SHOW PROCESSLIST;

-- Show variables
SHOW VARIABLES;
SHOW VARIABLES LIKE 'character_set%';

-- Explain query execution plan
EXPLAIN SELECT * FROM table_name WHERE column1 = 'value';

-- Show warnings
SHOW WARNINGS;

-- Show errors
SHOW ERRORS;
```

---

## 💡 COMMON DATA TYPES

```sql
-- Numeric
INT, INTEGER           -- Integer
BIGINT                 -- Large integer
DECIMAL(10,2)          -- Fixed-point decimal
FLOAT                  -- Floating-point
DOUBLE                 -- Double precision

-- String
VARCHAR(n)             -- Variable-length string (max n chars)
CHAR(n)                -- Fixed-length string (n chars)
TEXT                   -- Large text

-- Date/Time
DATE                   -- Date (YYYY-MM-DD)
TIME                   -- Time (HH:MM:SS)
DATETIME               -- Date and time
TIMESTAMP              -- Timestamp (auto-updates)

-- Boolean
BOOLEAN, BOOL          -- Boolean (stored as TINYINT)
TINYINT(1)             -- Often used for boolean
```

---

## 🎯 QUICK REFERENCE

| Task | Command |
|------|---------|
| List databases | `SHOW DATABASES;` |
| Use database | `USE database_name;` |
| List tables | `SHOW TABLES;` |
| Describe table | `DESCRIBE table_name;` |
| Select all | `SELECT * FROM table_name;` |
| Count rows | `SELECT COUNT(*) FROM table_name;` |
| Insert row | `INSERT INTO table_name (col1, col2) VALUES ('val1', 'val2');` |
| Update row | `UPDATE table_name SET col1='value' WHERE id=1;` |
| Delete row | `DELETE FROM table_name WHERE id=1;` |

---

## ⚠️ IMPORTANT NOTES

1. **Always use WHERE clause** with UPDATE and DELETE - without it, ALL rows are affected!
2. **Use transactions** for critical operations
3. **Backup before DROP/DELETE** operations
4. **Use parameterized queries** in applications to prevent SQL injection
5. **Use LIMIT** when testing DELETE/UPDATE on large tables

---

*Last updated: 2024*
