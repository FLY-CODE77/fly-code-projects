import pandas as pd
def monthly_sub(df):
    '''
    sub last month - this month car sales value
    return top 5 increasement and decreasement sales months 
    and values 
    '''

    df = df.sort_values(by='date')
    new_df = df[1:]
    new_df['before'] = df['value'][:-1].values
    new_df['sub'] = -(new_df['before'] - new_df['value'])
    
    good_day = new_df['sub'].sort_values(ascending=False)[:5]
    bad_day = new_df['sub'].sort_values()[:5]
    day_df = pd.concat([good_day, bad_day], 0)
    return day_df
    print('function activated')