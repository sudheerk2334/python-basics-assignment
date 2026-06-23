import pandas as pd

import numpy as np



# Load dataset

df = pd.read_csv("ai_learning_lab.csv")



# 1. Remove duplicate rows

df = df.drop_duplicates()



# 2. Strip extra spaces

columns_strip = ["student_name", "topic", "tool_used"]

for col in columns_strip:

  df[col] = df[col].astype(str).str.strip()



# 3. Convert columns to title case

columns_title = ["attendance", "lab_completed", "api_used"]

for col in columns_title:

  df[col] = df[col].astype(str).str.strip().str.title()



# 4. Replace invalid assignment_score values

df["assignment_score"] = pd.to_numeric(

  df["assignment_score"], errors="coerce"

)

df.loc[

  (df["assignment_score"] < 0) |

  (df["assignment_score"] > 100),

  "assignment_score"

] = np.nan



# 5. Replace invalid quiz_score values

df["quiz_score"] = pd.to_numeric(

  df["quiz_score"], errors="coerce"

)

df.loc[

  (df["quiz_score"] < 0) |

  (df["quiz_score"] > 100),

  "quiz_score"

] = np.nan



# 6. Replace invalid study_hours values

df["study_hours"] = pd.to_numeric(

  df["study_hours"], errors="coerce"

)

df.loc[df["study_hours"] < 0, "study_hours"] = np.nan



# 7. Replace invalid feedback_rating values

df["feedback_rating"] = pd.to_numeric(

  df["feedback_rating"], errors="coerce"

)

df.loc[

  (df["feedback_rating"] < 1) |

  (df["feedback_rating"] > 5),

  "feedback_rating"

] = np.nan



# 8. Fill missing values

df["assignment_score"].fillna(

  df["assignment_score"].mean(),

  inplace=True

)



df["quiz_score"].fillna(

  df["quiz_score"].mean(),

  inplace=True

)



df["study_hours"].fillna(

  df["study_hours"].median(),

  inplace=True

)



df["feedback_rating"].fillna(

  df["feedback_rating"].median(),

  inplace=True

)



# 9. Print shape of cleaned dataframe

print("Cleaned Dataset Shape:")

print(df.shape)



# 10. Print missing values after cleaning

print("\nMissing Values After Cleaning:")

print(df.isnull().sum())



# 11. Save cleaned dataset

df.to_csv(

  "cleaned_ai_learning_lab.csv",

  index=False

)



print("\nCleaned dataset saved as 'cleaned_ai_learning_lab.csv'")
