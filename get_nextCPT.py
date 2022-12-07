import pandas as pd
import datetime as dt

def get_nextCPT (df):
    ExSD_list = ["02:30","03:00","03:30","06:45","10:45","14:30","18:45","19:15","19:45","23:00","23:30"]
    df['ExSD'] = pd.to_datetime(df['ExSD'])
    df['ExSD_str'] = df['ExSD'].dt.strftime('%H:%M')
    df = df[df['ExSD_str'].isin(ExSD_list)]
    now = dt.datetime.now()
    minT = df['ExSD'].min()
    
    PADtime = ((minT - now)- pd.Timedelta(minutes=20))
    PADtime = PADtime.total_seconds()/60
    nextCPT = df.loc[df['ExSD'] == minT]['ExSD_str'].min()
    
    return PADtime,nextCPT


if __name__ == "__main__":
    get_nextCPT()