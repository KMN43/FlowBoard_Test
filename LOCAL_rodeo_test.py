import urllib3
import pandas as pd
from requests_kerberos import OPTIONAL, HTTPKerberosAuth
from retryer import requests_retry_session
from formatter import pandas_format
from openpyxl import load_workbook

pd.options.display.float_format = "{:,.0f}".format
urllib3.disable_warnings()


fc = "MAD4"

url1 = f"https://rodeo-dub.amazon.com/{fc}/ExSD?yAxis=WORK_POOL&zAxis=PROCESS_PATH" \
      f"&shipmentTypes=CUSTOMER_SHIPMENTS&exSDRange.quickRange=PLUS_MINUS_1_DAY&" \
      f"exSDRange.dailyStart=00%3A00&exSDRange.dailyEnd=00%3A00&giftOption=ALL&fulfillmentServiceClass=ALL&" \
      f"fracs=ALL&isEulerExSDMiss=ALL&isEulerPromiseMiss=ALL&isEulerUpgraded=ALL&" \
      f"isReactiveTransfer=ALL&workPool=PredictedCharge&workPool=PlannedShipment&" \
      f"_workPool=on&workPool=ReadyToPick&workPool=ReadyToPickHardCapped&" \
      f"workPool=ReadyToPickUnconstrained&workPool=PickingNotYetPicked&workPool=PickingNotYetPickedPrioritized" \
      f"&workPool=PickingNotYetPickedNotPrioritized&workPool=PickingNotYetPickedHardCapped&workPool=CrossdockNotYetPicked&" \
      f"_workPool=on&workPool=PickingPicked&workPool=PickingPickedInProgress&workPool=PickingPickedInTransit&" \
      f"workPool=PickingPickedRouting&workPool=PickingPickedAtDestination&workPool=Inducted&workPool=RebinBuffered" \
      f"&workPool=Sorted&workPool=GiftWrap&workPool=Packing&workPool=Scanned&workPool=ProblemSolving&workPool=ProcessPartial&" \
      f"workPool=SoftwareException&workPool=Crossdock&workPool=PreSort&workPool=TransshipSorted&workPool=Palletized&_workPool=on&" \
      f"workPool=ManifestPending&workPool=ManifestPendingVerification&workPool=Manifested&workPool=Loaded&workPool=TransshipManifested&" \
      f"_workPool=on&processPath=PPHOV&processPath=PPSingleMedium&processPath=PPNonCon&processPath=PPMultiWrap&processPath=PPMultiMedium&" \
      f"processPath=PPNonConTeamLift&processPath=PPMultiTBYB&processPath=&minPickPriority=MIN_PRIORITY&shipMethod=&shipOption=&sortCode=&fnSku="
      
      
      
def pull_rodeo(url):
    resp = requests_retry_session().get({url},
                                    auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),
                                    verify=False,
                                    allow_redirects=True,
                                    timeout=30)

    if resp.status_code == 200:
        data = pd.read_html(resp.text,flavor=None,header=0, index_col=0)

        if data is not None:
            df = pd.concat(data, sort=False)
            df = df.dropna(axis=0, thresh=4)

        else:
            print("No Data")
    
    else:
        print(resp.raise_for_status())

    return df