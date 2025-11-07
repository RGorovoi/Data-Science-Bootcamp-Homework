import pandas as pd

def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    total_players = activity['player_id'].nunique()
    
    if total_players == 0:
        return pd.DataFrame({'fraction': [0.00]})

    first_logins = activity.groupby('player_id')['event_date'].min().reset_index()
    first_logins.columns = ['player_id', 'first_login'] 
    first_logins['target_date'] = first_logins['first_login'] + pd.Timedelta(days=1)
    
    returning_count = pd.merge(first_logins,activity,left_on=['player_id', 'target_date'], right_on=['player_id', 'event_date'],how='inner')['player_id'].nunique() 
    
    fraction_value = round(returning_count / total_players, 2)
    
    return pd.DataFrame({'fraction': [fraction_value]})
