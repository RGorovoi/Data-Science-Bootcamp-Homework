import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    cooperation = actor_director.groupby(['actor_id', 'director_id']).size()
    collaborators = cooperation[cooperation >= 3]
    result = collaborators.index.to_frame(index=False)
    return result
