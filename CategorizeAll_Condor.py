#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
import itertools
from optparse import OptionParser
import operator
import os

##-- Example Usage:
# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ -r 120. -R 130. --nStep 4 --MultiClass --outDir /eos/user/a/atishelm/www/HHWWgg/DNN/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Categorization/
# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ -r 115. -R 135. --nStep 1 --MultiClass --outDir /eos/user/a/atishelm/www/HHWWgg/DNN/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Categorization/

# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_MultiClass_EvenSingleH_2Hgg_withKinWeight_HggClassScale_4_BkgClassScale_1_BalanceYields/ -r 120. -R 130. --nStep 4 --MultiClass --outDir /eos/user/a/atishelm/www/HHWWgg/DNN/HHWWyyDNN_MultiClass_EvenSingleH_2Hgg_withKinWeight_HggClassScale_4_BkgClassScale_1_BalanceYields/Categorization/
# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_MultiClass_EvenSingleH_2Hgg_withKinWeight_HggClassScale_4_BkgClassScale_1_BalanceYields/ -r 115. -R 135. --nStep 1 --MultiClass --outDir /eos/user/a/atishelm/www/HHWWgg/DNN/HHWWyyDNN_MultiClass_EvenSingleH_2Hgg_withKinWeight_HggClassScale_4_BkgClassScale_1_BalanceYields/Categorization/

# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ -r 120. -R 130. --nStep 4 --MultiClass --outDir /eos/user/a/atishelm/www/HHWWgg/DNN/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Categorization/
# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ -r 115. -R 135. --nStep 1 --MultiClass --outDir /eos/user/a/atishelm/www/HHWWgg/DNN/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Categorization/

# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ -r 115. -R 135. --nStep 1 --MultiClass
# python optimizeCategories_Condor.py -d /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ -r 120. -R 130. --nStep 4 --MultiClass

if __name__ == '__main__':

#   parser = OptionParser()
#   parser.add_option( "-d", "--inDir",   dest="inDir",    default="",   type="string", help="inDir" )
#   parser.add_option( "-o", "--outDir",   dest="outDir",    default="",   type="string", help="outDir" )
#   parser.add_option( "-r", "--massMin", dest='massMin',  default=120., type="float",  help="massMin")
#   parser.add_option( "-R", "--massMax", dest='massMax',  default=130., type="float",  help="massMax")
#   parser.add_option( "-n", "--nStep",   dest='nStep',    default=1,    type="int",      help="nStep")
#   parser.add_option('--MultiClass', dest='MultiClass', action="store_true", help = "Run multiclassifier categorization -- includes VH and ttH in B computation")
#   (options, args) = parser.parse_args()  

#   inDir = options.inDir
#   outDir = options.outDir 
#   massMin = options.massMin
#   massMax = options.massMax
#   nStep = options.nStep
#   MultiClass = options.MultiClass

#   print "inDir:  ",inDir
#   print "MultiClass:",MultiClass
#   print "massMin:",massMin
#   print "massMax:",massMax
#   print "nStep:",nStep
  
  local = os.getcwd()
  if not os.path.isdir('error'): os.mkdir('error') 
  if not os.path.isdir('output'): os.mkdir('output') 
  if not os.path.isdir('log'): os.mkdir('log') 
   
  # Prepare condor jobs
  condor = '''executable              = run_script.sh
output                  = output/strips.$(ClusterId).$(ProcId).out
error                   = error/strips.$(ClusterId).$(ProcId).err
log                     = log/strips.$(ClusterId).log
transfer_input_files    = run_script.sh
# on_exit_remove          = (ExitBySignal == False) && (ExitCode == 0)
# periodic_release        = (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > (60*60))
    
+JobFlavour             = "longlunch"
# +AccountingGroup        = "group_u_CMS.CAF.ALCA"
queue arguments from arguments.txt
'''

  with open("condor_job.txt", "w") as cnd_out:
     cnd_out.write(condor)

  outputDir = os.getcwd()


  script = '''#!/bin/sh -e

TRAININGLABEL=$1; 
INDIR=$2; 
VAR=$3;
LOCAL=$4;
YEAR=$5;

eval `scramv1 ru -sh`
python ${LOCAL}/CategorizeAll.py --TrainingLabel ${TRAININGLABEL} --inDir ${INDIR} --var ${VAR} --year ${YEAR} --local ${LOCAL}

echo -e "DONE";  
'''

  arguments=[]

  TrainingLabels = [
      ##-- Binary 
      # "HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM",
      "HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel",
      ##-- MultiClassifier 
      "HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields",
      "HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields",
      "HHWWyyDNN_MultiClass_EvenSingleH_2Hgg_withKinWeight_HggClassScale_4_BkgClassScale_1_BalanceYields"   
  ]

  inDirStarts = [
     ##-- Binary
   #   "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production",
     "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production",
     ##-- MultiClassifier 
     "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier",
     "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier",
     "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier"   
  ]

  vars = [
     ##-- Binary
   #   "evalDNN",
     "evalDNN",
     ##-- MultiClassifier
     "evalDNN_HH",
     "evalDNN_HH",
     "evalDNN_HH"
  ]

  years = ["2016", "2017", "2018"]

  for iTrain, TrainingLabel in enumerate(TrainingLabels):
    inDirStart = inDirStarts[iTrain]
    var = vars[iTrain]     
    for year in years:
      inDir = "%s/%s/"%(inDirStart, TrainingLabel)
      arguments.append("{} {} {} {} {}".format(TrainingLabel, inDir, var, local, year))

  with open("arguments.txt", "w") as args:
     args.write("\n".join(arguments)) 

  with open("run_script.sh", "w") as rs:
     rs.write(script) 
