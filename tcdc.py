#!/usr/bin/env python
# coding: utf-8

# In[30]:


#-*- coding: utf-8 -*-
import csv
import pandas as pd
import random
from datetime import datetime

rdf = pd.read_csv('노선.csv')
tdf = pd.read_csv('교통수단코드.csv')

day = '20181104'
f = 'C:/Data/20181229_인천시_교통카드데이터/1-1.거래내역/DI_TBTRDD010_' + day + '.csv'
df = pd.read_csv(f, index_col=None, header=0, encoding='utf-8', low_memory=False)
of = 'IC_ETick_' + day + '.txt'
df.sample(n=10).head()


# In[ ]:


with open(of, mode='w', newline='') as visum_file:
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
        No = no_dict.setdefault(row['카드번호'], seq_no)
        if No == seq_no:
            seq_no = seq_no + 1
        
        NumPass = row['이용객수']
#         노선ID => 노선번호, 지하철 => 교통수단코드 기준 교통수단명
        SurveyLineName = row['노선ID']
        if SurveyLineName == '~':
            trans_name = tdf.loc[tdf['교통수단코드'] == row['교통수단코드'], '교통수단명']
            if len(trans_name) > 0:
#                 print('길이:', len(trans_name), '수단명: ', trans_name)
                SurveyLineName = trans_name.values[0]
            else:
                SurveyLineName = row['교통수단코드']
        else:
            route_name = rdf.loc[rdf['노선ID'] == row['노선ID'], '노선명']
            if len(route_name) > 0:
                SurveyLineName = route_name.values[0]
        InputStopNo = row['승차정류장ID']
        dt = str(row['승차일시'])
        InputStopDepTime = datetime.strptime(dt[8:], '%H%M%S').strftime('%H:%M:%S')
        InputStopDepDay = 1
#         InputStopDepDay = datetime.strptime(dt[:8], '%Y%m%d').strftime('%Y-%m-%d')
        BoardStopNo = row['승차정류장ID']
        AlightStopNo = row['하차정류장ID']
        DestStopNo = row['하차정류장ID']
        OrigStopNo = row['승차정류장ID']
        PreTSysCode = ''
        NewLine = ''
        
        visum_writer.writerow([No, NumPass, SurveyLineName, InputStopNo, 
                              InputStopDepTime, InputStopDepDay, BoardStopNo, AlightStopNo, 
                              DestStopNo, OrigStopNo, PreTSysCode, NewLine])

