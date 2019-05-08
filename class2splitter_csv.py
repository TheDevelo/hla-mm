# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 10:29:19 2017
name: class2splitter_csv.py
@author: changliu & Robert Fuchs
This script reads in output from HLAmatchmaker to quantify the number of mismatched epitopes in the graft-versus-host (GVH) and host-versus-graft (HVG) directions respectively.
input files: class2 analysis result from Hmm, tab 4 and tab 5 exported as class2rec.csv and class2don.csv respective.
output: class2output.csv
"""

from __future__ import division
import sys
import os
import re

don=open('class2don.csv','r')
rec=open('class2rec.csv','r')
out=open('class2output.csv','w')

DDRab=[]
DDRot=[]
DDWab=[]
DDWot=[]
DDQab=[]
DDQot=[]
DDQAab=[]
DDQAot=[]
DDPab=[]
DDPot=[]
DonEp=[]
for line in don:
    if line.split(',')[3].startswith('DRB1'):
        data=line.upper().split(',')
        DonEp.append(data[16:])
        DDRab.append(data[16:41]+data[76:101])
        DDRot.append(data[41:76]+data[101:136])
        DDWab.append(data[136:161]+data[196:221])
        DDWot.append(data[161:196]+data[221:256])
        DDQab.append(data[256:286]+data[315:345])
        DDQot.append(data[286:315]+data[345:374])
        DDQAab.append(data[374:394]+data[414:434])
        DDQAot.append(data[394:414]+data[434:454])
        DDPab.append(data[454:469]+data[484:499])
        DDPot.append(data[469:484]+data[499:514])
        
RDRab=[]
RDRot=[]
RDWab=[]
RDWot=[]
RDQab=[]
RDQot=[]
RDQAab=[]
RDQAot=[]
RDPab=[]
RDPot=[]
RecEp=[]
for line in rec: 
    if line.split(',')[4].startswith('DRB1'): 
        data=line.upper().split(',')
        RecEp.append(data[17:])
        RDRab.append(data[17:42]+data[77:102])
        RDRot.append(data[42:77]+data[102:137])
        RDWab.append(data[137:162]+data[197:222])
        RDWot.append(data[162:197]+data[222:257])
        RDQab.append(data[257:287]+data[316:346])
        RDQot.append(data[287:316]+data[346:375])
        RDQAab.append(data[375:395]+data[415:435])
        RDQAot.append(data[395:415]+data[435:455])
        RDPab.append(data[455:470]+data[485:500])
        RDPot.append(data[470:485]+data[500:515])

# Write column titles
out.write("Patient Row,GVH Total,GVH DRab,GVH DRot,GVH DWab,GVH DWot,GVH DQab,GVH DQot,GVH DQAab,GVH DQAot,GVH DPab,GVH DPot,HVG Total,HVG DRab,HVG DRot,HVG DWab,HVG DWot,HVG DQab,HVG DQot,HVG DQAab,HVG DQAot,HVG DPab,HVG DPot\n")
# Output data as a CSV file
for i in range(len(RecEp)):
    out.write(str(i+1))
    for REpType in [RecEp,RDRab,RDRot,RDWab,RDWot,RDQab,RDQot,RDQAab,RDQAot,RDPab,RDPot]:
        case=REpType[i]
        reccount=0
        for ep in case:
            if ep.strip() not in map(str.strip, DonEp[i]):
                reccount=reccount+1        
        out.write(','+str(reccount))
    for DEpType in [DonEp,DDRab,DDRot,DDWab,DDWot,DDQab,DDQot,DDQAab,DDQAot,DDPab,DDPot]:
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
