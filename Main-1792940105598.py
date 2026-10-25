import pandas as pd
import numpy as np
from functions import (
    calculate_student_totals_and_averages,
    determine_pass_fail,
    analyze_subject_performance,
    get_top_performers
)

def main():
    print("=" * 60)
    print("      STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 60)
    
    # Step 1: Read Dataset
    file_path = 'data/students.csv'
    try:
        df = pd.read_csv(file_path)
        print(f"\n[INFO] Dataset successfully loaded from {file_path}")
        print(f"[INFO] Total Records Loaded: {len(df)}\n")
    except FileNotFoundError:
        print(f"[ERROR] Could not find file at {file_path}. Ensure data/students.csv exists.")
        return

    # Step 2: Process Data
    df = calculate_student_totals_and_averages(df)
    df = determine_pass_fail(df)

    # Step 3: Display Processed Data Summary
    print("--- STUDENT MARKS AND GRADES SUMMARY ---")
    summary_cols = ['Student ID', 'Name', 'Department', 'Total Marks', 'Average Marks', 'Grade', 'Status', 'Attendance']
    print(df[summary_cols].to_string(index=False))

    # Step 4: Class Performance Metrics
    overall_class_avg = np.round(np.mean(df['Average Marks'].to_numpy()), 2)
    total_students = len(df)
    passed_students = len(df[df['Status'] == 'Pass'])
    failed_students = len(df[df['Status'] == 'Fail'])
    pass_percentage = np.round((passed_students / total_students) * 100, 2)

    print("\n" + "=" * 60)
    print("--- OVERALL CLASS PERFORMANCE STATS ---")
    print(f"Overall Class Average Score : {overall_class_avg}")
    print(f"Total Students             : {total_students}")
    print(f"Passed Students            : {passed_students}")
    print(f"Failed Students            : {failed_students}")
    print(f"Pass Percentage            : {pass_percentage}%")

    # Step 5: Subject-Wise Performance Analysis
    print("\n" + "=" * 60)
    print("--- SUBJECT-WISE PERFORMANCE ANALYSIS ---")
    subject_df = analyze_subject_performance(df)
    print(subject_df.to_string())

    best_subject = subject_df.loc['Average'].idxmax()
    print(f"\nBest Performing Subject (Highest Average): {best_subject} ({subject_df.loc['Average', best_subject]})")

    # Step 6: Top Performers
    print("\n" + "=" * 60)
    print("--- TOP 3 PERFORMERS ---")
    top_3 = get_top_performers(df, top_n=3)
    print(top_3[['Student ID', 'Name', 'Department', 'Average Marks', 'Grade']].to_string(index=False))

    print("\n" + "=" * 60)
    print("[INFO] Analysis successfully completed.")
    print("=" * 60)

if __name__ == '__main__':
    main()