# Exercise 1.6 - Recipe App with MySQL Persistence

## Overview

For Exercise 1.6 I extended the Recipe App by wiring it to a MySQL
backend. Recipes and their difficulty scores are now stored in a
`recipes` table so the information survives across runs of the program.
The command-line workflow from the earlier exercises was enhanced with
CRUD features that operate on the database while still maintaining the
in-memory recipe and ingredient collections used by the UI helpers.

------------------------------------------------------------------------

## Tasks Completed

### 1. Bootstrapping the Database

- Connect to MySQL with the credentials provided for the coursework
  (`cf-python` / `password`).
- Automatically create the `task_database` schema and the `recipes`
  table if they do not exist yet.
- Load any existing rows into the application lists when the program
  launches so the CLI reflects the persisted data immediately.

### 2. Persisting Recipe Creation

- Prompt the user for the recipe name, cooking time, and a
  comma-separated list of ingredients.
- Calculate the difficulty tier using the same logic from previous
  exercises and attach it to the record.
- Insert the new recipe into MySQL via parameterized `INSERT` statements
  and keep the shared ingredient catalogue in sync.

### 3. Searching and Reporting Utilities

- Provide menu options for printing the full recipe catalog or the
  alphabetical list of unique ingredients.
- Search helpers allow users to look up recipes by an exact name or by
  selecting an ingredient from the indexed list, issuing SQL queries to
  retrieve matching rows.
- Display each result with the stored cooking time, difficulty, and
  formatted ingredient list.

### 4. Updating and Deleting Records

- Offer interactive prompts for updating a recipe's name, cooking time,
  or ingredient list while recalculating difficulty.
- Synchronize edits to the database using parameterized `UPDATE`
  statements keyed by the recipe's id.
- Allow users to remove recipes, clearing them from both the in-memory
  lists and the persistent table with a `DELETE` query.

------------------------------------------------------------------------

## Demo

Running `recipe_mysql.py` presents a menu-driven interface that now
stores every change in MySQL. The console prompts walk through listing
recipes, adding new ones, searching, updating, and deleting data, all
while reflecting the persisted state.

------------------------------------------------------------------------

## Folder Organization

Inside the **Exercise 1.6** folder:

- `recipe_mysql.py` contains the main CLI application, database setup,
  search helpers, and CRUD utilities that keep MySQL synchronized with
  the runtime lists.
- `testing.py` is an auxiliary script used for experimenting with raw
  MySQL queries while learning the connector API.

------------------------------------------------------------------------

## Learnings

- How to create and use MySQL databases and tables programmatically from
  Python with `mysql.connector`.
- How to combine in-memory data structures with persistent storage so a
  CLI stays responsive while keeping long-term records.
- How to implement interactive CRUD operations that leverage SQL queries
  and update application state safely.
