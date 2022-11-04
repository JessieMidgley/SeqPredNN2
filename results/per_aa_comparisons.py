import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_metrics(file):
    lst = []
    with open(file) as f:
        for line in f:
            if line.strip():                                # if the string is not only white space
                lst.append([x for x in line.split()])

    return lst


def per_aa_metrics(file):
    lst = get_metrics(file)
    names = []
    precision = []
    recall = []
    f1 = []
    for x in lst[1:21]:                                     # don't want first line (contains headings)
        names.append(x[0])
        precision.append(float(x[1]))
        recall.append(float(x[2]))
        f1.append(float(x[3]))

    return names, precision, recall, f1



# PER AA METRICS:

names, unb_precision, unb_recall, unb_f1 = per_aa_metrics('report_unbalanced.txt')
names, OS_precision, OS_recall, OS_f1 = per_aa_metrics('report_OS.txt')
names, US_precision, US_recall, US_f1 = per_aa_metrics('report_US.txt')
names, WL_precision, WL_recall, WL_f1 = per_aa_metrics('report_WL.txt')
names, T_precision, T_recall, T_f1 = per_aa_metrics('report_T.txt')
names, TPT_2_US_precision, TPT_2_US_recall, TPT_2_US_f1 = per_aa_metrics('report_TPT-2-US.txt')
names, TPT_2_OS_precision, TPT_2_OS_recall, TPT_2_OS_f1 = per_aa_metrics('report_TPT-2-OS.txt')

# names, T_US_precision, T_US_recall, T_US_f1 = per_aa_metrics('report_T-US.txt')
# names, T_OS_precision, T_OS_recall, T_OS_f1 = per_aa_metrics('report_T-OS.txt')
# names, TPT_1_US_precision, TPT_1_US_recall, TPT_1_US_f1 = per_aa_metrics('report_TPT-1-US.txt')
# names, TPT_1_OS_precision, TPT_1_OS_recall, TPT_1_OS_f1 = per_aa_metrics('report_TPT-1-OS.txt')



# MAKE PLOTS

df = pd.DataFrame(np.c_[unb_recall, US_recall, OS_recall, WL_recall, T_recall, TPT_2_US_recall, TPT_2_OS_recall],
                  index=names)

df = df.reindex(index = ['CYS', 'TRP', 'MET', 'HIS', 'TYR', 'GLN', 'PHE', 'ASN', 'PRO', 'ARG',
       'THR', 'LYS', 'ILE', 'SER', 'ASP', 'GLU', 'VAL', 'GLY', 'ALA', 'LEU'])
df = df.rename(index={'CYS': 'C', 'TRP':'W', 'MET':'M', 'HIS':'H', 'TYR':'Y', 'GLN':'Q', 'PHE':'F', 'ASN':'N', 'PRO':'P', 'ARG':'R',
       'THR':'T', 'LYS':'K', 'ILE':'I', 'SER':'S', 'ASP':'D', 'GLU':'E', 'VAL':'V', 'GLY':'G', 'ALA':'A', 'LEU':'L'})

df.plot.bar(width=0.8, figsize=(15,5), color=['#F2B701', '#E68310', '#CF1C90', '#80BA5A', '#008695', '#7F3C8D', '#f97b72'])

plt.xticks(rotation=0)
plt.legend(["Unbalanced", "US", "OS", "WL", "T", "TPT-2-US", "TPT-2-OS"])
plt.xlabel("Residue")
plt.ylabel("Recall")
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(0.1))

plt.show()

