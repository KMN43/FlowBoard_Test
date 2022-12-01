import urllib3
import pandas as pd
from requests_kerberos import OPTIONAL, HTTPKerberosAuth
from retryer import requests_retry_session
from formatter import pandas_format
from openpyxl import load_workbook

pd.options.display.float_format = "{:,.0f}".format
urllib3.disable_warnings()


fc = "MAD4"

url = f"https://rodeo-dub.amazon.com/{fc}/ExSD?yAxis=WORK_POOL&zAxis=PROCESS_PATH&shipmentTypes=CUSTOMER_SHIPMENTS&exSDRange.quickRange=PLUS_MINUS_1_DAY&exSDRange.dailyStart=00%3A00&exSDRange.dailyEnd=00%3A00&giftOption=ALL&fulfillmentServiceClass=ALL&fracs=ALL&isEulerExSDMiss=ALL&isEulerPromiseMiss=ALL&isEulerUpgraded=ALL&isReactiveTransfer=ALL&workPool=PredictedCharge&workPool=PlannedShipment&_workPool=on&workPool=ReadyToPick&workPool=ReadyToPickHardCapped&workPool=ReadyToPickUnconstrained&workPool=PickingNotYetPicked&workPool=PickingNotYetPickedPrioritized&workPool=PickingNotYetPickedNotPrioritized&workPool=PickingNotYetPickedHardCapped&workPool=CrossdockNotYetPicked&_workPool=on&workPool=PickingPicked&workPool=PickingPickedInProgress&workPool=PickingPickedInTransit&workPool=PickingPickedRouting&workPool=PickingPickedAtDestination&workPool=Inducted&workPool=RebinBuffered&workPool=Sorted&workPool=GiftWrap&workPool=Packing&workPool=Scanned&workPool=ProblemSolving&workPool=ProcessPartial&workPool=SoftwareException&workPool=Crossdock&workPool=PreSort&workPool=TransshipSorted&workPool=Palletized&_workPool=on&workPool=ManifestPending&workPool=ManifestPendingVerification&workPool=Manifested&workPool=Loaded&workPool=TransshipManifested&_workPool=on&processPath=PPHOV&processPath=PPSingleMedium&processPath=PPNonCon&processPath=PPMultiWrap&processPath=PPMultiMedium&processPath=PPNonConTeamLift&processPath=PPMultiTBYB&processPath=&minPickPriority=MIN_PRIORITY&shipMethod=&shipOption=&sortCode=&fnSku="
resp = requests_retry_session().get(url,
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