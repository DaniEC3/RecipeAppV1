"""
Database Inspection Tool
This script shows how to check databases, tables, and their structures
using both direct MySQL queries and SQLAlchemy methods.
"""

from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
import mysql.connector

# ============================================
# METHOD 1: Using MySQL Connector (Direct SQL)
# ============================================

def check_databases_with_connector():
    """Check databases using mysql.connector"""
    print("\n" + "="*60)
    print("METHOD 1: Using mysql.connector (Direct SQL)")
    print("="*60)
    
    conn = mysql.connector.connect(
        host='localhost',
        user='cf-python',
        passwd='password'
    )
    cursor = conn.cursor()
    
    # List all databases
    print("\n📁 Available Databases:")
    print("-" * 60)
    cursor.execute("SHOW DATABASES")
    for db in cursor.fetchall():
        print(f"  - {db[0]}")
    
    # Check tables in a specific database
    print("\n📊 Tables in 'my_database':")
    print("-" * 60)
    cursor.execute("USE my_database")
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    if tables:
        for table in tables:
            print(f"  - {table[0]}")
    else:
        print("  No tables found")
    
    # Describe table structure
    print("\n📋 Structure of 'practice_recipes' table:")
    print("-" * 60)
    cursor.execute("DESCRIBE practice_recipes")
    columns = cursor.fetchall()
    print(f"{'Field':<20} {'Type':<20} {'Null':<10} {'Key':<10} {'Default':<10} {'Extra':<10}")
    print("-" * 80)
    for col in columns:
        print(f"{col[0]:<20} {str(col[1]):<20} {str(col[2]):<10} {str(col[3]):<10} {str(col[4] if col[4] else 'NULL'):<10} {str(col[5] if col[5] else ''):<10}")
    
    # Count rows in table
    cursor.execute("SELECT COUNT(*) FROM practice_recipes")
    count = cursor.fetchone()[0]
    print(f"\n📈 Total rows in 'practice_recipes': {count}")
    
    cursor.close()
    conn.close()


# ============================================
# METHOD 2: Using SQLAlchemy Engine
# ============================================

def check_databases_with_sqlalchemy():
    """Check databases using SQLAlchemy"""
    print("\n" + "="*60)
    print("METHOD 2: Using SQLAlchemy")
    print("="*60)
    
    # Create engine
    engine = create_engine(
        "mysql+mysqlconnector://cf-python:password@localhost/my_database",
        echo=False
    )
    
    # List all databases using raw SQL
    print("\n📁 Available Databases:")
    print("-" * 60)
    with engine.connect() as conn:
        result = conn.execute(text("SHOW DATABASES"))
        for row in result:
            print(f"  - {row[0]}")
    
    # List tables in current database using inspector
    print("\n📊 Tables in 'my_database':")
    print("-" * 60)
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    if tables:
        for table in tables:
            print(f"  - {table}")
    else:
        print("  No tables found")
    
    # Get table columns
    print("\n📋 Columns in 'practice_recipes' table:")
    print("-" * 60)
    columns = inspector.get_columns('practice_recipes')
    print(f"{'Name':<20} {'Type':<30} {'Nullable':<10} {'Primary Key':<12}")
    print("-" * 72)
    for col in columns:
        pk = "Yes" if col.get('primary_key', False) else "No"
        nullable = "Yes" if col.get('nullable', True) else "No"
        col_type = str(col['type'])
        print(f"{col['name']:<20} {col_type:<30} {nullable:<10} {pk:<12}")
    
    # Get primary keys
    print("\n🔑 Primary Keys:")
    print("-" * 60)
    pk_constraint = inspector.get_pk_constraint('practice_recipes')
    if pk_constraint['constrained_columns']:
        print(f"  Primary Key: {', '.join(pk_constraint['constrained_columns'])}")
    else:
        print("  No primary key found")
    
    # Count rows
    print("\n📈 Row Count:")
    print("-" * 60)
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM practice_recipes"))
        count = result.scalar()
        print(f"  Total rows in 'practice_recipes': {count}")


# ============================================
# METHOD 3: Using SQLAlchemy Session
# ============================================

def check_with_session():
    """Check data using SQLAlchemy session"""
    print("\n" + "="*60)
    print("METHOD 3: Using SQLAlchemy Session")
    print("="*60)
    
    from sqlalchemy import orm, Column
    from sqlalchemy.types import Integer, String
    from sqlalchemy.orm import sessionmaker
    
    engine = create_engine(
        "mysql+mysqlconnector://cf-python:password@localhost/my_database",
        echo=False
    )
    
    Base = orm.declarative_base()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    class Recipe(Base):
        __tablename__ = "practice_recipes"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(50))
        ingredients = Column(String(255))
        cooking_time = Column(Integer)
        difficulty = Column(String(20))
    
    # Get all recipes
    print("\n🍳 All Recipes in Database:")
    print("-" * 60)
    recipes = session.query(Recipe).all()
    if recipes:
        for recipe in recipes:
            print(f"  ID: {recipe.id}, Name: {recipe.name}, Cooking Time: {recipe.cooking_time} min")
    else:
        print("  No recipes found")
    
    print(f"\n📈 Total recipes: {session.query(Recipe).count()}")
    
    session.close()


# ============================================
# USEFUL SQL COMMANDS REFERENCE
# ============================================

def print_sql_reference():
    """Print comprehensive SQL commands reference"""
    print("\n" + "="*80)
    print("ESSENTIAL SQL COMMANDS REFERENCE")
    print("="*80)
    
    sql_commands = """
════════════════════════════════════════════════════════════════════════════════
📁 DATABASE OPERATIONS
════════════════════════════════════════════════════════════════════════════════

# List all databases
SHOW DATABASES;

# Create a new database
CREATE DATABASE database_name;

# Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS database_name;

# Select/use a database
USE database_name;

# Delete a database (BE CAREFUL!)
DROP DATABASE database_name;

# Drop database if it exists
DROP DATABASE IF EXISTS database_name;

# Show current database
SELECT DATABASE();


════════════════════════════════════════════════════════════════════════════════
📊 TABLE OPERATIONS
════════════════════════════════════════════════════════════════════════════════

# List all tables in current database
SHOW TABLES;

# List tables from another database (without USE)
SHOW TABLES FROM database_name;

# Describe table structure
DESCRIBE table_name;
-- or
DESC table_name;

# Show table structure with full CREATE statement
SHOW CREATE TABLE table_name;

# Show columns from a table
SHOW COLUMNS FROM table_name;
SHOW COLUMNS FROM database_name.table_name;

# Show indexes on a table
SHOW INDEX FROM table_name;

# Show table status/info
SHOW TABLE STATUS FROM database_name;
SHOW TABLE STATUS LIKE 'table_name';

# Get detailed column information
SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
WHERE TABLE_SCHEMA = 'database_name' 
AND TABLE_NAME = 'table_name';


════════════════════════════════════════════════════════════════════════════════
🏗️  CREATE TABLE (DDL - Data Definition Language)
════════════════════════════════════════════════════════════════════════════════

# Create a table
CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    age INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# Create table if it doesn't exist
CREATE TABLE IF NOT EXISTS table_name (...);

# Alter table - Add column
ALTER TABLE table_name ADD COLUMN column_name VARCHAR(50);

# Alter table - Drop column
ALTER TABLE table_name DROP COLUMN column_name;

# Alter table - Modify column
ALTER TABLE table_name MODIFY COLUMN column_name VARCHAR(100);

# Alter table - Rename column
ALTER TABLE table_name RENAME COLUMN old_name TO new_name;

# Rename table
RENAME TABLE old_name TO new_name;

# Drop table
DROP TABLE table_name;

# Drop table if exists
DROP TABLE IF EXISTS table_name;

# Truncate table (delete all rows, keep structure)
TRUNCATE TABLE table_name;


════════════════════════════════════════════════════════════════════════════════
📝 INSERT DATA (DML - Data Manipulation Language)
════════════════════════════════════════════════════════════════════════════════

# Insert single row
INSERT INTO table_name (column1, column2, column3)
VALUES ('value1', 'value2', value3);

# Insert multiple rows
INSERT INTO table_name (column1, column2, column3)
VALUES 
    ('value1', 'value2', value3),
    ('value4', 'value5', value6),
    ('value7', 'value8', value9);

# Insert with all columns (in order)
INSERT INTO table_name VALUES (value1, 'value2', value3);

# Insert from another table
INSERT INTO table_name1 (column1, column2)
SELECT column1, column2 FROM table_name2;


════════════════════════════════════════════════════════════════════════════════
🔍 SELECT QUERIES (DQL - Data Query Language)
════════════════════════════════════════════════════════════════════════════════

# Select all columns from a table
SELECT * FROM table_name;

# Select specific columns
SELECT column1, column2, column3 FROM table_name;

# Select with WHERE condition
SELECT * FROM table_name WHERE column1 = 'value';

# Select with multiple conditions (AND)
SELECT * FROM table_name 
WHERE column1 = 'value' AND column2 > 100;

# Select with OR condition
SELECT * FROM table_name 
WHERE column1 = 'value1' OR column1 = 'value2';

# Select with IN clause
SELECT * FROM table_name WHERE column1 IN ('value1', 'value2', 'value3');

# Select with LIKE (pattern matching)
SELECT * FROM table_name WHERE name LIKE 'John%';  -- Starts with
SELECT * FROM table_name WHERE name LIKE '%John';  -- Ends with
SELECT * FROM table_name WHERE name LIKE '%John%'; -- Contains

# Select with BETWEEN
SELECT * FROM table_name WHERE age BETWEEN 18 AND 65;

# Select with NULL check
SELECT * FROM table_name WHERE column1 IS NULL;
SELECT * FROM table_name WHERE column1 IS NOT NULL;

# Select DISTINCT values
SELECT DISTINCT column1 FROM table_name;

# Count rows
SELECT COUNT(*) FROM table_name;

# Count with condition
SELECT COUNT(*) FROM table_name WHERE column1 = 'value';

# Count distinct values
SELECT COUNT(DISTINCT column1) FROM table_name;

# Aggregate functions
SELECT 
    COUNT(*) AS total,
    AVG(column1) AS average,
    SUM(column1) AS sum_total,
    MIN(column1) AS minimum,
    MAX(column1) AS maximum
FROM table_name;

# Select with GROUP BY
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1;

# Select with HAVING (filter groups)
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1 
HAVING COUNT(*) > 5;

# Select with ORDER BY
SELECT * FROM table_name ORDER BY column1 ASC;   -- Ascending
SELECT * FROM table_name ORDER BY column1 DESC;  -- Descending
SELECT * FROM table_name ORDER BY column1, column2;  -- Multiple columns

# Select with LIMIT
SELECT * FROM table_name LIMIT 10;        -- First 10 rows
SELECT * FROM table_name LIMIT 10 OFFSET 5;  -- Skip 5, take 10

# Aliases
SELECT column1 AS alias_name, column2 AS another_alias FROM table_name;


════════════════════════════════════════════════════════════════════════════════
✏️  UPDATE DATA (DML)
════════════════════════════════════════════════════════════════════════════════

# Update single row
UPDATE table_name 
SET column1 = 'new_value', column2 = 100
WHERE id = 1;

# Update multiple rows
UPDATE table_name 
SET column1 = 'new_value'
WHERE column2 = 'condition';

# Update with calculation
UPDATE table_name 
SET column1 = column1 + 10
WHERE id = 1;

# ⚠️  WARNING: Always use WHERE clause! Without it, updates ALL rows!


════════════════════════════════════════════════════════════════════════════════
🗑️  DELETE DATA (DML)
════════════════════════════════════════════════════════════════════════════════

# Delete specific rows
DELETE FROM table_name WHERE id = 1;

# Delete with condition
DELETE FROM table_name WHERE column1 = 'value';

# Delete multiple rows
DELETE FROM table_name WHERE column1 IN ('value1', 'value2');

# ⚠️  WARNING: Always use WHERE clause! Without it, deletes ALL rows!


════════════════════════════════════════════════════════════════════════════════
🔗 JOINS
════════════════════════════════════════════════════════════════════════════════

# INNER JOIN (only matching rows)
SELECT * FROM table1
INNER JOIN table2 ON table1.id = table2.table1_id;

# LEFT JOIN (all from left, matching from right)
SELECT * FROM table1
LEFT JOIN table2 ON table1.id = table2.table1_id;

# RIGHT JOIN (all from right, matching from left)
SELECT * FROM table1
RIGHT JOIN table2 ON table1.id = table2.table1_id;

# FULL OUTER JOIN (all from both) - MySQL doesn't support, use UNION
SELECT * FROM table1 LEFT JOIN table2 ON table1.id = table2.table1_id
UNION
SELECT * FROM table1 RIGHT JOIN table2 ON table1.id = table2.table1_id;


════════════════════════════════════════════════════════════════════════════════
🔐 CONSTRAINTS & INDEXES
════════════════════════════════════════════════════════════════════════════════

# Primary Key
CREATE TABLE table_name (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ...
);

# Foreign Key
CREATE TABLE table1 (
    id INT PRIMARY KEY,
    FOREIGN KEY (other_id) REFERENCES table2(id)
);

# Unique constraint
ALTER TABLE table_name ADD UNIQUE (column_name);

# Index
CREATE INDEX index_name ON table_name (column_name);

# Drop index
DROP INDEX index_name ON table_name;


════════════════════════════════════════════════════════════════════════════════
📋 USEFUL UTILITY COMMANDS
════════════════════════════════════════════════════════════════════════════════

# Show current user
SELECT USER();

# Show MySQL version
SELECT VERSION();

# Show current time
SELECT NOW();
SELECT CURDATE();  -- Current date
SELECT CURTIME();  -- Current time

# Show process list (running queries)
SHOW PROCESSLIST;

# Show variables
SHOW VARIABLES;
SHOW VARIABLES LIKE 'character_set%';

# Explain query execution plan
EXPLAIN SELECT * FROM table_name WHERE column1 = 'value';

# Show warnings
SHOW WARNINGS;

# Show errors
SHOW ERRORS;
    """
    
    print(sql_commands)


if __name__ == "__main__":
    try:
        # Run all methods
        check_databases_with_connector()
        check_databases_with_sqlalchemy()
        check_with_session()
        print_sql_reference()
        
        print("\n" + "="*60)
        print("✅ Database inspection complete!")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure:")
        print("  1. MySQL server is running")
        print("  2. Database 'my_database' exists")
        print("  3. User 'cf-python' with password 'password' has access")
        print("  4. Table 'practice_recipes' exists (if checking tables)")
