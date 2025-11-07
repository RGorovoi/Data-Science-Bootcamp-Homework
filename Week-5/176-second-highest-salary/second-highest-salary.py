import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    salary = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)

    if len(salary) < 2:
        second_highest_salary = None
    else:
        second_highest_salary = salary.iloc[1]

    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})

    return result_df
