# task4_visual_report.py

import pandas as pd
import matplotlib.pyplot as plt
import json

# Load cleaned dataset
df = pd.read_csv("cleaned_ai_learning_lab.csv")

# Create total_score column
df["total_score"] = df["assignment_score"] + df["quiz_score"]

# -----------------------------
# 1. Bar Chart: Average total_score by topic
# -----------------------------
avg_score = df.groupby("topic")["total_score"].mean()

plt.figure(figsize=(8, 5))
avg_score.plot(kind="bar")
plt.title("Average Total Score by Topic")
plt.xlabel("Topic")
plt.ylabel("Average Total Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("topic_score_chart.png")
plt.close()

# -----------------------------
# 2. Bar Chart: Student count by performance_level
# -----------------------------
performance_count = df["performance_level"].value_counts()

plt.figure(figsize=(8, 5))
performance_count.plot(kind="bar")
plt.title("Student Count by Performance Level")
plt.xlabel("Performance Level")
plt.ylabel("Student Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("performance_level_chart.png")
plt.close()

# -----------------------------
# 3. Pie Chart: Attendance distribution
# -----------------------------
attendance_dist = df["attendance"].value_counts()

plt.figure(figsize=(7, 7))
attendance_dist.plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Attendance Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("attendance_chart.png")
plt.close()

# -----------------------------
# 4. Line Chart: Average study_hours by topic
# -----------------------------
avg_study = df.groupby("topic")["study_hours"].mean()

plt.figure(figsize=(8, 5))
avg_study.plot(kind="line", marker="o")
plt.title("Average Study Hours by Topic")
plt.xlabel("Topic")
plt.ylabel("Average Study Hours")
plt.grid(True)
plt.tight_layout()
plt.savefig("study_hours_chart.png")
plt.close()

# -----------------------------
# 5. Create summary dictionary
# -----------------------------
summary = {
    "total_students": int(df.shape[0]),
    "average_assignment_score": round(
        df["assignment_score"].mean(), 2
    ),
    "average_quiz_score": round(
        df["quiz_score"].mean(), 2
    ),
    "average_study_hours": round(
        df["study_hours"].mean(), 2
    ),
    "most_common_topic": df["topic"].mode()[0]
}

# Save summary to JSON
with open("learning_summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("Charts and summary report generated successfully.")
print("Generated files:")
print("- topic_score_chart.png")
print("- performance_level_chart.png")
print("- attendance_chart.png")
print("- study_hours_chart.png")
print("- learning_summary.json")
