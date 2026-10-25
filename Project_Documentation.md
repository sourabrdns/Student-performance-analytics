# Project Documentation: Student Performance Analytics System

## 1. Project Title & Details
- **Project Name:** Student Performance Analytics System
- **Course / Program:** Python Data Analysis (EWB Courses)
- **Student Name:** [Enter Your Name Here]
- **Student ID:** [Enter Your ID Here]
- **Department:** [Enter Your Department Here]
- **Submission Date:** 26 October 2026

---

## 2. Objective
The primary objective of this project is to build an automated, Python-based student performance analytics system. The system reads student academic data, processes and analyzes it utilizing **NumPy** and **Pandas**, and generates actionable insights such as individual marks summaries, averages, letter grades, pass/fail statistics, subject-wise performance trends, and top-performing student rankings without relying on complex machine learning models.

---

## 3. Technologies Used
- **Python (v3.x):** Core programming language used for scripting logic, functions, and control flows.
- **Pandas:** Used for DataFrame creation, data ingestion (`pd.read_csv`), filtering, data manipulation, and table formatting.
- **NumPy:** Used for high-performance vectorized mathematical operations (calculating sums, means, maximums, and minimums across matrices).

---

## 4. Dataset Description
The project utilizes a custom CSV dataset located at `data/students.csv` containing 15 realistic student records. The dataset includes the following columns:
- `Student ID`: Unique numeric identifier for each student.
- `Name`: Full name of the student.
- `Department`: Academic discipline (Computer Science, IT, Electronics, Mechanical).
- `Maths`: Marks obtained in Mathematics (out of 100).
- `Physics`: Marks obtained in Physics (out of 100).
- `Chemistry`: Marks obtained in Chemistry (out of 100).
- `Attendance`: Percentage of classes attended (0–100%).

---

## 5. Implementation Step-by-Step
1. **Data Loading (Step 1 & 2):**  
   The program uses Pandas (`pd.read_csv`) to load records from `data/students.csv`, verify column headers, and check dataset integrity.
2. **Data Processing & Calculations (Step 3):**  
   - Subject marks are extracted into NumPy arrays to execute fast vectorized operations (`np.sum` and `np.mean`) for total and average marks.
   - Iterative loops evaluate each student's average score against grading thresholds to assign letter grades (`A` for $\ge 85$, `B` for $\ge 70$, `C` for $\ge 50$, `D` for $\ge 40$, `F` for $< 40$).
   - Conditional statements verify pass/fail criteria (requiring an average score $\ge 40$ and attendance $\ge 60\%$).
3. **Statistical Analysis (Step 4):**  
   - Subject-wise scores are grouped and analyzed via NumPy to determine the highest, lowest, and average score for Maths, Physics, and Chemistry.
   - Sorting algorithms isolate the top 3 performing students.
4. **Output Presentation (Step 5):**  
   - Formatted DataFrames and metrics are printed clearly to the console for the user to inspect without viewing code files.

---

## 6. Key Features Implemented
- **Automated Summary Generation:** Calculates total marks, average scores, grades, and pass/fail statuses for every student.
- **Class-Wide Metrics:** Computes overall class averages, total passed/failed counts, and pass percentages.
- **Subject-Wise Analysis:** Identifies peak performance, lowest scores, and subject averages.
- **Top Performers Ranking:** Dynamically sorts and displays the top 3 students.
- **Modular Architecture:** Separates calculation logic (`functions.py`) from execution flow (`main.py`).

---

## 7. Output / Results Summary
When running `python main.py`, the system outputs:
- A complete tabular summary of all 15 students showing IDs, names, departments, total marks, averages, grades, status, and attendance.
- Class performance metrics showing an overall average score of ~67.5% and an 80% class pass rate.
- Subject performance breakdown highlighting best and lowest performing subjects.
- A ranked list of the top 3 academic performers.

---

## 8. Final Outcome
The project was successfully designed, implemented, and tested locally. All requirements specified in the project guidelines—including Pandas dataframes, NumPy numerical calculations, modular functions, and robust directory structures—have been completely fulfilled.

---

## 9. Challenges & Learnings
- **Challenge:** Combining dual criteria (academic score threshold AND minimum attendance percentage) into the pass/fail determination function.
- **Solution:** Implemented structured `for` loops combined with explicit `if-else` conditional checking over pandas DataFrame rows.
- **Learning:** Gained strong practical experience in combining Pandas DataFrame manipulation with NumPy vectorized array calculations for clean, readable data-analytics scripts.

---

## 10. GitHub Repository Link
- **Repository URL:** `https://github.com/YOUR_USERNAME/student-performance-analytics`
