import numpy as np
import pandas as pd

def calculate_student_totals_and_averages(df):
    """
    Calculates total and average marks for each student using NumPy arrays.
    """
    marks_matrix = df[['Maths', 'Physics', 'Chemistry']].to_numpy()
    
    total_marks = np.sum(marks_matrix, axis=1)
    average_marks = np.mean(marks_matrix, axis=1)
    
    df['Total Marks'] = total_marks
    df['Average Marks'] = np.round(average_marks, 2)
    return df

def assign_grade(average):
    """
    Assigns grades based on predefined rules using conditional logic.
    """
    if average >= 85:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 50:
        return 'C'
    elif average >= 40:
        return 'D'
    else:
        return 'F'

def determine_pass_fail(df):
    """
    Determines Pass/Fail status. Pass requires average >= 40 and attendance >= 60%.
    """
    grades = []
    statuses = []
    
    for idx, row in df.iterrows():
        grade = assign_grade(row['Average Marks'])
        grades.append(grade)
        
        # Condition: Pass if average >= 40 and attendance >= 60%
        if row['Average Marks'] >= 40 and row['Attendance'] >= 60:
            statuses.append('Pass')
        else:
            statuses.append('Fail')
            
    df['Grade'] = grades
    df['Status'] = statuses
    return df

def analyze_subject_performance(df):
    """
    Generates subject-wise performance statistics using NumPy and Pandas.
    """
    subjects = ['Maths', 'Physics', 'Chemistry']
    subject_stats = {}
    
    for subject in subjects:
        scores = df[subject].to_numpy()
        subject_stats[subject] = {
            'Average': np.round(np.mean(scores), 2),
            'Highest': np.max(scores),
            'Lowest': np.min(scores)
        }
        
    return pd.DataFrame(subject_stats)

def get_top_performers(df, top_n=3):
    """
    Retrieves top N students sorted by average marks.
    """
    return df.sort_values(by='Average Marks', ascending=False).head(top_n)
