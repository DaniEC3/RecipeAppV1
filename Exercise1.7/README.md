# Exercise 1.7 - Recipe App with SQLAlchemy ORM

## Overview

For Exercise 1.7 I refactored the Recipe App to use SQLAlchemy's ORM
instead of writing raw SQL queries. Recipes are mapped to a
`final_project_recipes` table through a declarative `Recipe` model and all
CRUD operations now flow through a shared SQLAlchemy session. The command
line experience from earlier iterations remains, but database work is
centralized in model methods and helper functions so validations and
difficulty calculations occur in one place.

------------------------------------------------------------------------

## Tasks Completed

### 1. SQLAlchemy Configuration

- Configure an engine for the coursework MySQL instance using the
  `mysql+mysqlconnector` dialect string and credentials.
- Declare a `Recipe` model with columns for id, name, ingredients,
  cooking time, and difficulty, plus helper methods for calculating
  difficulty tiers and returning ingredient lists.
- Create the `final_project_recipes` table automatically on startup via
  `Base.metadata.create_all` so the schema is available for the ORM.

### 2. CLI Features Backed by the ORM

- Preserve the interactive menu for listing, adding, updating, searching,
  and deleting recipes, redirecting each action to SQLAlchemy session
  queries.
- Present recipe output using the model's `__str__` override so every CLI
  view shares consistent formatting and emoji-enhanced styling.
- Populate the database with a default "Tea" recipe on first launch to
  demonstrate the ORM mapping and to ensure searches have baseline data.

### 3. Data Validation and Difficulty Calculation

- Add detailed input validation for names, cooking times, and
  ingredients, including maximum lengths and numeric checks to prevent
  invalid records.
- Recalculate difficulty tiers through the model's `calculate_difficulty`
  helper whenever cooking time or ingredients change to keep stored
  metadata accurate.
- Use ORM session commits for persistence after each create, update, or
  delete action, guaranteeing the database and CLI remain synchronized.

------------------------------------------------------------------------

## Demo

Running `recipe_app.py` opens the familiar menu-driven interface, but all
interactions—showing recipes, inserting new entries, searching by
ingredient, editing, or deleting—are now powered by SQLAlchemy ORM
sessions. Console prompts guide the user through every workflow while the
database updates occur transparently in the background.

------------------------------------------------------------------------

## Folder Organization

Inside the **Exercise 1.7** folder:

- `recipe_app.py` contains the SQLAlchemy model, database session setup,
  and the complete CLI with ORM-backed CRUD features and validations.
- `SQL_CheatSheet.md` and the `Notes/` directory hold reference material
  gathered while learning SQLAlchemy and refining the final project.

------------------------------------------------------------------------

## Learnings

- How to map Python classes to MySQL tables using SQLAlchemy's declarative
  base and dialect connection strings.
- How ORM sessions simplify CRUD logic by handling commits, queries, and
  object state tracking.
- How to centralize validation and computed fields (like difficulty) on
  the model to keep CLI interactions consistent and resilient.
