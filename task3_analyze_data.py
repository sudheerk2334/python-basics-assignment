import pandas as pd

import numpy as np



# Load cleaned dataset

df = pd.read_csv("cleaned_ai_learning_lab.csv")



# 1. Create total_score column

df["total_score"] = (

  df["assignment_score"] +

  df["quiz_score"]

)



# 2. Create performance_level column

conditions = [

  df["total_score"] >= 160,

  (df["total_score"] >= 120) & (df["total_score"] < 160),

  (df["total_score"] >= 80) & (df["total_score"] < 120),

  df["total_score"] < 80

]



labels = [

  "Excellent",

  "Good",

  "Average",

  "Needs Support"

]



df["performance_level"] = np.select(

  conditions,

  labels,

  default="Needs Support"

)



# 3. Print average assignment score

print("Average Assignment Score:")

print(df["assignment_score"].mean())



# 4. Print average quiz score

print("\nAverage Quiz Score:")

print(df["quiz_score"].mean())



# 5. Print average study hours

print("\nAverage Study Hours:")

print(df["study_hours"].mean())



# 6. Print number of students in each performance level

print("\nPerformance Level Counts:")

print(df["performance_level"].value_counts())



# 7. Print average score topic-wise

print("\nAverage Total Score Topic-wise:")

print(

  df.groupby("topic")["total_score"]

   .mean()

)



# 8. Print average score batch-wise

print("\nAverage Total Score Batch-wise:")

print(

  df.groupby("batch")["total_score"]

   .mean()

)



# 9. Print students who need support

print("\nStudents Needing Support:")



needs_support = df[

  df["performance_level"] == "Needs Support"

]



print(

  needs_support[

    [

      "student_name",

      "topic",

      "total_score",

      "performance_level"

    ]

  ]

)
