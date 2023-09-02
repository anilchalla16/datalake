import datetime
import logging
import time
import urllib.request
import pandas as pd
current_date = datetime.datetime.now()
current_date = current_date.strftime("%m_%d_%Y")
file_name = r'D:\datalake\logfiles\ftostatus_'+str(current_date) +'.txt'
print(file_name)
logging.basicConfig(format='%(asctime)s -%(levelname)s - %(message)s',
                    level=logging.INFO, datefmt='%d-%b-%y %H:%M:%S', filename=file_name,
                    filemode='w')
logging.info('Start time of the script')
print(f"Program started : {datetime.datetime.now()}")
try:
    data_info = []
    with open(r"D:\datalake\ingestion\fto_status\files\sourcefiles\fto_numbers.txt", "r") as ftono:
        for no in ftono:
            url = "https://www.paddyprocurement.ap.gov.in/CSPPS/do?requestType=misreportsrh&actionVal=ftodtls&season=RMS-22&flag=RP&randomid=0.4798611554642792&ftono=" + str(no)
            with urllib.request.urlopen(url) as i:
                html = i.read()
            data = pd.read_html(html, skiprows=0)[3]
            FTONO = data.loc[3][1]
            PPC = data.loc[2][1]
            NAME = data.loc[8][1]
            STATUS = data.loc[6][1]
            AMOUNT = data.loc[5][1]
            Bank_Name = data.loc[9][1]
            data = [FTONO, PPC, NAME, STATUS, AMOUNT, Bank_Name]
            data_info.append(data)
            time.sleep(1)
    print("Date extracted from webpage")
    df = pd.DataFrame(data_info, columns=["FTONO", "PPC", "NAME", "STATUS", "AMOUNT", "Bank_Name"])
    print("Data loaded successfully")
    logging.info('Data filter from html ')
    #fto_status = df[df["STATUS"] == "Paid"]
    logging.info('FTO_NO status paid')
    print("FTO STATUS : Paid")

    df.to_excel(r"D:\datalake\ingestion\FTO_STATUS\files\targetfiles\fto_status_paid.xlsx")
    print("Fto status paid file saved")
    logging.info('saved the  file to excel')
    print(f"Program ended  :{datetime.datetime.now()}")
except Exception as e:
    print(f"Something went wrong: {e}")
    logging.error("Something went worng")
