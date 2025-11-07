import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner', suffixes=('_emp', '_dept'))

    merged_df['salary_rank'] = merged_df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    high_earners_df = merged_df[merged_df['salary_rank'] <= 3]
    
    result_df = high_earners_df.rename(
        columns={'name_dept': 'Department','name_emp': 'Employee','salary': 'Salary'})
    
    return result_df[['Department', 'Employee', 'Salary']]
