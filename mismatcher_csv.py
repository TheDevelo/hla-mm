import sys
import os
import re

data=open('mismatchdata.csv','r')
out=open('mismatchoutput.csv','w')

out.write("Patient Row,Rec1A,Rec2A,Rec1B,Rec2B,Rec1C,Rec2C,Rec1DRB,Rec2DRB,Rec1DQB,Rec2DQB,Rec1DPB,Rec2DPB,")
out.write("Don1A,Don2A,Don1B,Don2B,Don1C,Don2C,Rec1DRB,Rec2DRB,Rec1DQB,Rec2DQB,Rec1DPB,Rec2DPB,")
out.write("A Allele GVH,B Allele GVH,C Allele GVH,DRB Allele GVH,DQB Allele GVH,DPB Allele GVH,")
out.write("A Antigen GVH,B Antigen GVH,C Antigen GVH,DRB Antigen GVH,DQB Antigen GVH,DPB Antigen GVH,")
out.write("A Allele HVG,B Allele HVG,C Allele HVG,DRB Allele HVG,DQB Allele HVG,DPB Allele HVG,")
out.write("A Antigen HVG,B Antigen HVG,C Antigen HVG,DRB Antigen HVG,DQB Antigen HVG,DPB Antigen HVG\n")

for line in data:
    row = line.split(',')
    out_row = []
    if row[1].startswith('A'):
        # Copy data into output row
        for i in range(25):
            out_row.append(row[i])
        # Create data arrays for easy matching
        recA=[out_row[1],out_row[2]]
        recB=[out_row[3],out_row[4]]
        recC=[out_row[5],out_row[6]]
        recDRB=[out_row[7],out_row[8]]
        recDQB=[out_row[9],out_row[10]]
        recDPB=[out_row[11],out_row[12]]
        donA=[out_row[13],out_row[14]]
        donB=[out_row[15],out_row[16]]
        donC=[out_row[17],out_row[18]]
        donDRB=[out_row[19],out_row[20]]
        donDQB=[out_row[21],out_row[22]]
        donDPB=[out_row[23],out_row[24]]

        for direct in range(2):
            for trunc in range(2):
                for group in range(6):
                    # Set data arrays to new alias to make code more general
                    if group == 0:
                        host = recA
                        trans = donA
                    if group == 1:
                        host = recB
                        trans = donB
                    if group == 2:
                        host = recC
                        trans = donC
                    if group == 3:
                        host = recDRB
                        trans = donDRB
                    if group == 4:
                        host = recDQB
                        trans = donDQB
                    if group == 5:
                        host = recDPB
                        trans = donDPB
                    # Swap host and trans if direction is HVG
                    if direct == 1:
                        swap = host
                        host = trans
                        trans = swap
                    # Truncate data if antigen matching
                    if trunc == 1:
                        host[0] = host[0][:-3]
                        host[1] = host[1][:-3]
                        trans[0] = trans[0][:-3]
                        trans[1] = trans[1][:-3]

                    # Get num of mismatches
                    mismatches = 0
                    for allele in host:
                        if allele not in trans:
                            mismatches += 1

                    # Write to out_row
                    out_row.append(str(mismatches))

        # Write out_row to file
        out.write(','.join(out_row)+"\n")


