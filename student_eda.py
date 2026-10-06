import pandas as pd
import matplotlib.pyplot as plt

# Create student dataset
data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Gender": [
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Female"
    ],
    "StudyHours": [4, 3, 5, 2, 6, 4, 7, 3, 5, 2, 6, 5],
    "Attendance(%)": [90, 82, 95, 78, 92, 85, 96, 80, 88, 79, 91, 89],
    "Marks": [82, 70, 88, None, 91, 68, 95, 72, None, 65, 84, 84]
}

# Create DataFrame
df = pd.DataFrame(data)

# Make one row an exact duplicate
df.loc[11] = df.loc[10]

# Save dataset
df.to_csv("student_performance.csv", index=False)

# Load CSV
df = pd.read_csv("student_performance.csv")

# Initial inspection
print("Shape:", df.shape)

print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicate row
df = df.drop_duplicates()

# Fill missing Marks with median
median_marks = df["Marks"].median()
df["Marks"] = df["Marks"].fillna(median_marks)

print("\nAfter cleaning:", df.shape)

# -----------------------------
# Histogram of Marks
# -----------------------------

plt.hist(df["Marks"], bins=6, edgecolor="black")

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Marks Distribution")

plt.savefig("marks_histogram.png")
plt.close()

# -----------------------------
# Boxplot of Marks
# -----------------------------

plt.boxplot(df["Marks"])

plt.ylabel("Marks")
plt.title("Marks Boxplot")

plt.savefig("marks_boxplot.png")
plt.close()

# -----------------------------
# Scatter Plot
# -----------------------------

plt.scatter(df["StudyHours"], df["Marks"])

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.savefig("studyhours_vs_marks.png")
plt.close()

# -----------------------------
# Correlation Matrix
# -----------------------------

correlation = df[
    ["StudyHours", "Attendance(%)", "Marks"]
].corr()

print("\nCorrelation Matrix:")
print(correlation)

# ---------

gender_summary = df.groupby("Gender")[
    ["Marks", "Attendance(%)"]
].mean()

print("\nAverage Marks and Attendance by Gender:")
print(gender_summary)

print("\nSaved:")
print("marks_histogram.png")
print("marks_boxplot.png")
print("studyhours_vs_marks.png")