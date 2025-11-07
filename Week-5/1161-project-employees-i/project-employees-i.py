import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(project,employee,on='employee_id',how='inner')
    average_df = merged_df.groupby('project_id')['experience_years'].mean().reset_index()
    average_df['experience_years'] = average_df['experience_years'].round(2)

    average_df.rename(columns={'experience_years': 'average_years'},inplace=True)
    
    return average_df[['project_id', 'average_years']]
