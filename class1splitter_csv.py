# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:29:19 2017
name: class1splitter_csv.py
@author: changliu & Robert Fuchs
This script reads in output from HLAmatchmaker to quantify the number of mismatched epitopes in the graft-versus-host (GVH) and host-versus-graft (HVG) directions respectively.
input files: class1 analysis result from Hmm, tab 4 and tab 5 exported as class1rec.csv and class1don.csv respective.
output: class1output.csv
"""

from __future__ import division
import sys
import os
import re

don=open('class1don.csv','r')
rec=open('class1rec.csv','r')
out=open('class1output.csv','w')


DAab=[]
DAot=[]
DBab=[]
DBot=[]
DCab=[]
DCot=[]
DonEp=[]
for line in don:
    if line.split(',')[2].startswith('A'):
        line=line.upper()
        DonEp.append(line.split(',')[8:668])
        DAab.append(line.split(',')[8:68]+line.split(',')[118:178])
        DAot.append(line.split(',')[68:118]+line.split(',')[178:228])
        DBab.append(line.split(',')[228:288]+line.split(',')[338:398])
        DBot.append(line.split(',')[288:338]+line.split(',')[398:448])
        DCab.append(line.split(',')[448:508]+line.split(',')[558:618])
        DCot.append(line.split(',')[508:558]+line.split(',')[618:668])
        
RAab=[]
RAot=[]
RBab=[]
RBot=[]
RCab=[]
RCot=[]
RecEp=[]
for line in rec: 
    if line.split(',')[4].startswith('A'): 
        line=line.upper()
        RecEp.append(line.split(',')[10:670])
        RAab.append(line.split(',')[10:70]+line.split(',')[120:180])
        RAot.append(line.split(',')[70:120]+line.split(',')[180:230])
        RBab.append(line.split(',')[230:290]+line.split(',')[340:400])
        RBot.append(line.split(',')[290:340]+line.split(',')[400:450])
        RCab.append(line.split(',')[450:510]+line.split(',')[560:620])
        RCot.append(line.split(',')[510:560]+line.split(',')[620:670])

# Write column titles
out.write("Patient Row,GVH Total,GVH Aab,GVH Aot,GVH Bab,GVH Bot,GVH Cab,GVH Cot,HVG Total,HVG Aab,HVG Aot,HVG Bab,HVG Bot,HVG Cab,HVG Cot\n")
# Output data as a CSV file
for i in range(len(RecEp)):
    out.write(str(i+1))
    for REpType in [RecEp,RAab,RAot,RBab,RBot,RCab,RCot]:
        case=REpType[i]
        reccount=0
        for ep in case:
            if ep.strip() not in map(str.strip, DonEp[i]):
                reccount=reccount+1        
        out.write(','+str(reccount))
    for DEpType in [DonEp,DAab,DAot,DBab,DBot,DCab,DCot]:
        case=DEpType[i]
        doncount=0
        for ep in case:
            if ep.strip() not in map(str.strip, RecEp[i]):
                doncount=doncount+1
        out.write(','+str(doncount))
    out.write('\n')
        
don.close()
rec.close()
out.close()               
