import pandas as pd
import requests
from datetime import datetime
import numpy as np
import pytz
import sys, os
import math
from colorama import init, Fore, Back, Style
# https://pypi.org/project/colorama/

# # Using os.name
# current_os = os.name
# print("Current OS (os.name):", current_os)

# # Using sys.platform
# current_os_sys = sys.platform
# print("Current OS (sys.platform):", current_os_sys)

# Initialize colorama
init()

# Example usage
# print(Fore.RED + 'Red text')
# print(Back.GREEN + 'Green background')
# print(Style.RESET_ALL + 'Back to default')

list_news_convertion = ["Unemployment Claims"]

def colored_histogram_with_labels(data_wk):
    max_value = 5
    min_value = -5
    # print (min_value,0,max_value)

    label_line = ''
    wk_report = "%+2s |%-3s|%-3s|%-3s|%-3s|%-3s|%-3s|%-3s"%(("",'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'))
    print (wk_report)
    print(Style.RESET_ALL + ("---+---+---+---+---+---+---+---"))
    x = ("","","","","","","")
    for i in range(10, -1, -1):
        new_x = []
        idx = i-5
        new_x.append(idx)
        for min, max in data_wk:
            #print ("\t\t\t",dk - idx)
            if max - idx >= 0 and max > 0 and max - idx < max:
                new_x.append("X")
            elif min - idx <= 0 and min < 0 and min - idx > min:
                # print ("\t\t\t",dk - idx)
                new_x.append("X")    
            else: new_x.append(" ")
            
        x = tuple(new_x)
        #print (x)    
        if idx == 0: print(Style.RESET_ALL + ("%+2s +---+---+---+---+---+---+--- "%(i-5)))
        else:
            fnt_color = Style.RESET_ALL
            if idx > 0: fnt_color = Fore.GREEN
            elif idx < 0: fnt_color = Fore.RED
            print(fnt_color + ("%+2s . %-2s. %-2s. %-2s. %-2s. %-2s. %-2s. %-2s"%(x)))

def get_json_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data from the URL.")
        return None

# URL of the JSON data
url = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"

# Get JSON data
json_data = get_json_data(url)
today = datetime.now()

if json_data:
    # Convert JSON data to DataFrame
    df = pd.DataFrame(json_data)
    
    # Convert date column to datetime objects
    df['date'] = pd.to_datetime(df['date'])
    df['date_only'] = df['date'].dt.date
    df['time_only'] = df['date'].dt.time
    
    # Convert datetime to new timezone (UTC+7)
    new_timezone = pytz.timezone('Asia/Bangkok')  # Change to appropriate timezone
    df['date'] = df['date'].dt.tz_convert(new_timezone)
    # Filter data by country
    # filtered_df = df[df['country'].isin(['GBP', 'JPY', 'USD', 'EUR'])]
    filtered_df = df[df['country'].isin(['USD'])]
    
    # print (today.date())
    
    # 0     1                            2      3      4         5          6         7 
    # title country                      date   impact forecast  previous   date_only time_only
    # Display the filtered DataFrame
    # print(filtered_df)
    
    # Print DataFrame headers
    headers = df.columns
    # print("%-60s %-8s %-21s %-7s %-10s %-10s %-10s %-10s %-10s" % 
    # (headers[0].upper(), headers[1].upper(), headers[2].upper(), 
     # headers[3].upper(), headers[4].upper(), headers[5].upper(), 
     # "GOLD.VIEW", "CALCULATE", "PERCENT"))
    previous_date_only = None
    trend_suggest_weeks = []
    trend_suggest_today = []
    sum_wk_7day_crazy = []
    # Print DataFrame line by line
    for index, row in filtered_df.iterrows():
        forecast = row['forecast'].replace("%", "").replace("T", "").replace("B", "").replace("K", "").replace("M", "")
        previous = row['previous'].replace("%", "").replace("T", "").replace("B", "").replace("K", "").replace("M", "")
        gold_view = ""
        dxy_view  = "="
        if forecast == '':
            if previous != '':
                forecast = previous
            else:
                previous = '0'
                forecast = '0'
        trend_forecast = 0
        impact_level  = 1
        if row['impact'] == "Medium": 
            impact_level  =  2
        elif row['impact'] == "High": 
            impact_level  =  4
            
        percent = 0
        try:
            trend_forecast = (float(forecast) - float(previous))
            if float(previous)!= 0: percent = (float(forecast) - float(previous))*100/float(previous)
            if row['title'] in list_news_convertion: 
                trend_forecast = (float(previous) - float(forecast))
                if float(previous)!= 0: percent = (float(previous) - float(forecast))*100/float(previous)
            if trend_forecast > 0:
                if impact_level > 2: gold_view = "---" 
                else: gold_view = "-" 
                dxy_view  = ">"
            elif trend_forecast == 0 : 
                if impact_level > 2: gold_view = "???" 
                #  else: gold_view = "NORMAL"
            elif trend_forecast < 0: 
                if impact_level > 2: gold_view = "+++" 
                else: gold_view = "+"
                dxy_view  = "<"
            if impact_level >= 2 and percent != 0:
                trend_suggest_weeks.append(percent * impact_level)
                
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print("Fail @line: " + str(exc_tb.tb_lineno) + " w/ " + str(exc_obj) + " ... ")
        
        fnt_color = Style.RESET_ALL
        if row['date_only'] >= today.date():
            # USD      2024-02-27 20:30:00   High
            # -----------------------------------
            day_name = row['date_only'].strftime("%A")
            if row['date_only'] != previous_date_only: 
                print ("")
                #x_datetime = datetime.strptime(row['date_only'], "%Y-%m-%d %H:%M:%S")
                
                print ("------ %-10s %-5s ------"%(day_name, str(row['date'])[:10]))
                
                previous_date_only = row['date_only']
            else:
                if trend_suggest_weeks and row['date_only'] == today.date(): 
                    trend_suggest_today.append(trend_suggest_weeks[-1])
            if impact_level > 1:
                if "+" in gold_view:    
                    fnt_color = Fore.GREEN
                elif "-" in gold_view:
                    fnt_color = Fore.RED
                else:
                    fnt_color = Style.RESET_ALL
                    
                if row['impact'] == "High":
                    if fnt_color == Style.RESET_ALL: fnt_color = Fore.CYAN
                    fnt_color =  fnt_color + Style.BRIGHT
                sum_wk_7day_crazy.append((day_name, row['title'], row['impact'], percent * impact_level))
            print(fnt_color + ("%-5s %-1s %+7s %-1s %-7s %+5s %-3s" %(str(row['date'])[11:16], row['impact'][:1], row['forecast'],dxy_view, row['previous'], str(format(trend_forecast, '.2f')), gold_view)))
            previous_date_only = row['date_only']
    print ("")
    print (Style.RESET_ALL + "------------ SUMMARY --------------")
    # print (trend_suggest_today)
    # print (trend_suggest_weeks)
    
    total_today = sum(trend_suggest_today)
    # print (trend_suggest_today)
    # print (total_today)
    
    if (total_today > 0): 
        print (Fore.RED + ("PREDICT TODAY GOLD -> DOWN (%s)"%str(format(total_today, '.2f'))))
    elif (total_today < 0): 
        print (Fore.GREEN + ("PREDICT TODAY GOLD -> UP (%s)"%str(format(total_today, '.2f'))))
    else: 
        print (Style.RESET_ALL + ("PREDICT TODAY GOLD -> UNKNOW (%s)"%str(format(total_today, '.2f'))))
    
    total_wk = sum(trend_suggest_weeks)
    # print (total_wk)
    if (total_wk >  0): 
        print (Fore.RED +("PREDICT WEEKS GOLD -> DOWN (%s)"%str(format(total_wk, '.2f'))))
    elif (total_wk <  0): 
        print (Fore.GREEN + ("PREDICT WEEKS GOLD -> UP (%s)"%str(format(total_wk, '.2f'))))
    else: 
        print (Style.RESET_ALL + ("PREDICT WEEKS GOLD -> UNKNOW (%s)"%str(format(total_wk, '.2f'))))
    print (Style.RESET_ALL + "-----------------------------------")
    
    # print (trend_suggest_weeks)

    #print (sum_wk_7day_crazy)
    days_on_week = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    new_days_on_week = []
    for day in days_on_week:
        print (day)
        data_report = []
        min, max= 0,0
        for each_day_crazy in sum_wk_7day_crazy:
            dayname, title, impact, percentage = each_day_crazy
            if day == dayname:
                if percentage < 0: min = min + percentage
                if percentage > 0: max = max + percentage
                print ("  ", impact[:1], str(format(percentage, '.2f'))+"%", title)
                data_report.append(percentage)
                
        # if sum(data_report) > 1 and sum(data_report)
        if sum(data_report) != 0:
            # print (min, max)
            if abs(sum(data_report)) < 5:
                min = math.floor(min)
                max = math.ceil(max)
                #print (min, max)
            else:
                min = math.floor((min/abs(sum(data_report))) * 5)
                max = math.ceil((max/abs(sum(data_report))) * 5)
            #print (min, max)    

        # else:
        #     print(0,0)
        new_days_on_week.append((max*-1, min*-1))
       # print (day,new_days_on_week[-1])
        #print ("")
    
    colored_histogram_with_labels(new_days_on_week)  
        
