#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
import pandas as pd
import random
from datetime import datetime

f = 'C:/Data/20181229_인천시_교통카드데이터/1-1.거래내역/DI_TBTRDD010_20181101.csv'
df = pd.read_csv(f, index_col=None, header=0, encoding='utf-8', low_memory=False)

with open('IC_ETick.txt', mode='w', newline='') as visum_file:
    visum_writer = csv.writer(visum_file, delimiter=';', quoting=csv.QUOTE_NONE)
    
    visum_writer.writerow(['$VISION'])
    visum_writer.writerow(['* VisumInst'])
    visum_writer.writerow(['* 22.05.12, 18.27.29'])
    visum_writer.writerow(['*'])
    visum_writer.writerow(['*'])
    visum_writer.writerow(['* Tabelle: Versionsblock'])
    visum_writer.writerow(['$VERSION', 'VERSNR', 'FILETYPE', 'LANGUAGE', 'UNIT'])
    visum_writer.writerow(['4.00','Att','Eng','KM'])
    visum_writer.writerow(['*'])
    visum_writer.writerow(['*'])
    visum_writer.writerow(['* Table: PuT path legs'])
    visum_writer.writerow(['$SingleRowSurveyData:No', 'NumPass', 'SurveyLineName', 'InputStopNo', 'InputStopDepTime', 'InputStopDepDay', 'BoardStopNo', 'AlightStopNo', 'DestStopNo', 'OrigStopNo', 'PreTSysCode'])
# 번호	승객수	탑승노선	탑승정류장	탑승시간	탑승일자	하차정류장	환승정류장	최종하차정류장	최초출발정류장	
    visum_writer.writerow(['*'])
    visum_writer.writerow(['*'])
    
    seq_no = 1
    no_dict = {}
    
    for index, row in df.iterrows():
        no = no_dict.setdefault(row['카드번호'], seq_no)
        if no == seq_no:
            seq_no = seq_no + 1
        
        dt = str(row['승차일시'])
        InputStopDepTime = datetime.strptime(dt[8:], '%H%M%S').strftime('%H:%M:%S')
        InputStopDepDay = datetime.strptime(dt[:8], '%Y%m%d').strftime('%Y-%m-%d')
        
        visum_writer.writerow([no, row['이용객수'], row['노선ID'], row['승차정류장ID'], 
                              InputStopDepTime, InputStopDepDay, row['승차정류장ID'], row['하차정류장ID'], 
                              row['하차정류장ID'], row['승차정류장ID'], '', ''])

