import json
import sys
import os
import pickle
import numpy as np



ent2search = {}
mnt2pos = {}
subtotal = 0
total = 0
acc_degree = []
acc_prom = []
acc_string_prom = []


with open("./data/aida_test_complete_le_titov.json", "r") as f:
    dataset = json.load(f)
    for data in dataset:
        sentence = data["sentence"]
        for mnt in data["mentions"]:
            mnt_surface = mnt['mention-surface']
            pos = mnt['positives']
            ent = mnt["entity"]
            WDdegree = mnt['positives-WDdegree']
            FBprom = mnt['positives-FBprom']
            pos_names = mnt['positives-name']
            ent_name = mnt['entity-name']
            if len(pos) == 0:
                continue 
            total += 1
            cand2name = []
            cand_name = []
            cand2degree = []
            cand_degree = []
            cand2prom = []
            cand_prom = []
            if ent in pos:
                subtotal += 1
                ## DEGREE BASELINE
                for p, d in zip(pos, WDdegree):
                    if p != 'Unknown' and d != 'Unknown':
                        cand2degree.append(d)
                        cand_degree.append(p)
                if len(cand_degree) > 0 and ent in cand_degree:
                    cand2degree = -np.array(cand2degree)
                    acc_degree.append(np.argsort(cand2degree)[0] == cand_degree.index(ent))
                ## PROMINENCE BASELINE
                for p, d in zip(pos, FBprom):
                    if p != 'Unknown' and d != 'Unknown':
                        cand2prom.append(d)
                        cand_prom.append(p)
                if len(cand_prom) > 0 and ent in cand_prom:
                    cand2prom = np.array(cand2prom)
                    acc_prom.append(np.argsort(cand2prom)[0] == cand_prom.index(ent))
                ## STRING MATCHING BASELINE
                for p, d, n in zip(pos, FBprom, pos_names):
                    if p != 'Unknown' and d != 'Unknown' and n == mnt_surface:
                        cand2name.append(d)
                        cand_name.append(p)
                if len(cand_name) > 0 and ent in cand_name:
                    cand2name = np.array(cand2name)
                    acc_string_prom.append(np.argsort(cand2name)[0] == cand_name.index(ent))

#print("Size of E+ {} and Total {}".format(subtotal, total))
print("[Our Implementation] DEGREE - Precision in E+ {} and in Total {}".format(sum(acc_degree) / subtotal, sum(acc_degree) / total ))
print("[Our Implementation] PROMINENCE - Precision in E+ {} and in Total {}".format(sum(acc_prom) / subtotal, sum(acc_prom) / total ))
print("[Our Implementation] STRING MATCHING - Precision in E+ {} and in Total {}".format(sum(acc_string_prom) / subtotal, sum(acc_string_prom) / total ))
print("[Le Phong and Titov Implementation] STRING MATCHING - Precision in E+ {} and in Total {}".format(str(0.291), str(0.150)))
print("[Le Phong and Titov Implementation] τMIL-ND - Precision in E+ {} and in Total {}".format(str(0.732), str(0.389)))
