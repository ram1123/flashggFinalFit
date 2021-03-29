#########################################################################################
# Abraham Tishelman-Charny                                                              #
# 24 March 2021                                                                         #
#                                                                                       #
# The purpose of this script is to compute combine limits for various SL DNN trainings, # 
# years and nodes.                                                                      # 
#########################################################################################

import os 
import pandas as pd 

arguments = pd.read_csv("arguments.txt", sep=" ", header=None)

for i, row in enumerate(arguments.values.tolist()):
    if(i > 1): break 
    row = [str(e) for e in row]
    arg_str = " ".join(row)
    print("arg_str:",arg_str)
    COMMAND = "sh run_script.sh %s"%(arg_str)
    print("COMMAND:",COMMAND)

    os.system(COMMAND)

