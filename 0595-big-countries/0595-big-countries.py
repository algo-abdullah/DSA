import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    # df  = pd.DataFrame
    # print(df.head) 
    # return df.area
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    return df[['name', 'population', 'area']]
    # if pd.DataFrame.population ==25000000 and pd.DataFrame.area ==    3000000 :

        # return DataFrame.name,DataFrame.population,DataFrame.area    