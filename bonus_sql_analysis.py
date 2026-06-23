# bonus_sql_analysis.py

import sqlite3
import pandas as pd

# Load cleaned CSV file
df = pd.read_csv("cleaned_ai_learning_lab.csv")

# Create total_score column if not already present
df["total_score"] = df["assignment_score"] + df["quiz_score"]

# Connect to SQLite database
with sqlite3.connect("learning_lab.db") as conn:

    # Store DataFrame into SQLite table
    df.to_sql(
        "student_learning",
        conn,
        if_exists="replace",
        index=False
    )

    cursor = conn.cursor()

    # -----------------------------
    # Query 1: Average assignment score by topic
    # -----------------------------
    print("\nQuery 1: Average Assignment Score by Topic")

    query1 = """
    SELECT topic, AVG(assignment_score)
    FROM student_learning
    GROUP BY topic;
    """

    result1 = cursor.execute(query1).fetchall()

    for row in result1:
        print(row)

    # -----------------------------
    # Query 2: Student count by batch
    # -----------------------------
    print("\nQuery 2: Student Count by Batch")

    query2 = """
    SELECT batch, COUNT(*)
    FROM student_learning
    GROUP BY batch;
    """

    result2 = cursor.execute(query2).fetchall()

    for row in result2:
        print(row)

    # -----------------------------
    # Query 3: Students with total score below 80
    # -----------------------------
    print("\nQuery 3: Students with Total Score Below 80")

    query3 = """
    SELECT student_name, total_score
    FROM student_learning
    WHERE total_score < 80;
    """

    result3 = cursor.execute(query3).fetchall()

    for row in result3:
        print(row)

print("\nSQLite analysis completed successfully.")
print("Database created: learning_lab.db")
