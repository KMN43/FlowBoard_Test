import urllib3
import pandas as pd
from requests_kerberos import OPTIONAL, HTTPKerberosAuth
from retryer import requests_retry_session
import io


pd.options.display.float_format = "{:,.0f}".format
urllib3.disable_warnings()


fc = "MAD4"


def pull_rodeo_csv(url):
    resp = requests_retry_session().get(url,
                                    auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),
                                    verify=False,
                                    allow_redirects=True,
                                    timeout=30)

    if resp.status_code == 200:

        csv_data = resp.content

        if csv_data is not None:
            
            rawData = pd.read_csv(io.StringIO(csv_data.decode('utf-8')))
            df = rawData.dropna(axis=0, thresh=4)
            df = df.groupby(['Process Path', 'Work Pool']).agg({'Quantity': 'sum'}).reset_index()
            

        else:
            print("No Data")
    
    else:
        print(resp.raise_for_status())

    return df

if __name__ == "__main__":

    pull_rodeo_csv()