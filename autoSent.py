import pyautogui as pg
import webbrowser as web
# import time
import pandas as pd
import pywhatkit


data = pd.read_csv("leads.csv")
data_dict = data.to_dict('list')
leads = data_dict['LeadNumber']
messages = data_dict['Message']
combo = zip(leads,messages)
first = True

for lead,message in combo:
    try:
        pywhatkit.sendwhatmsg_instantly("+" + str(lead), message, 15, True, 3)
        print("Message sent to(indirectly): ", lead)
    except:
        print("Message NOT able to sent to: ", lead)