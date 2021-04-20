# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Date:   2021-04-20
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-04-20
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
  # if not os.path.isdir('error'): os.mkdir('error')
  if not os.path.isdir('output'): os.mkdir('output')
  if not os.path.isdir('log'): os.mkdir('log')

  # Prepare condor jobs
  condor = '''executable              = run_script_Signal.sh
output                  = output/strips.$(ClusterId).$(ProcId).out
error                   = output/strips.$(ClusterId).$(ProcId).out
log                     = log/strips.$(ClusterId).log
transfer_input_files    = run_script_Signal.sh,BinBoundaries_20Apr.txt
# on_exit_remove          = (ExitBySignal == False) && (ExitCode == 0)
# periodic_release        = (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > (60*60))

+JobFlavour             = "workday"
# +AccountingGroup      = "group_u_CMS.CAF.ALCA"
queue arguments from arguments_Signal.txt
'''

  with open("condor_job_Signal.txt", "w") as cnd_out:
     cnd_out.write(condor)

  outputDir = os.getcwd()


  script = '''#!/bin/sh -e

LOCAL=${1};
CHANNEL=${2};
INDIR=${3};
OPTION=${4};
WHICHSIGNAL=${5};
YEAR=${6};
OUTDIR=${7};
BinBoundaryTextFile=${8};
FINDSTRING=${9};
IFSYST=${10};
WHICHNODE=${11};

echo "LOCAL: ${LOCAL}"
echo "CHANNEL: ${CHANNEL}"
echo "INDIR: ${INDIR}"
echo "OPTION: ${OPTION}"
echo "WHICHSIGNAL: ${WHICHSIGNAL}"
echo "YEAR: ${YEAR}"
echo "OUTDIR: ${OUTDIR}"
echo "BinBoundaryTextFile: ${BinBoundaryTextFile}"
echo "FINDSTRING: ${FINDSTRING}"
echo "IFSYST: ${IFSYST}"
echo "WHICHNODE: ${WHICHNODE}"

eval `scramv1 ru -sh`

if [[ ${OPTION} -eq  "Signal" ]]; then
  python ${LOCAL}/CategorizeTrees_v2.py --ch ${CHANNEL} --iD ${INDIR} --opt ${OPTION} --year ${YEAR} --oD ${OUTDIR} --nBoundaries  ${BinBoundaryTextFile} --f ${FINDSTRING} --syst ${IFSYST} --WhichSig ${WHICHSIGNAL} --node ${WHICHNODE}
fi

if [[ ${OPTION} -eq  "SingleHiggs" ]]; then
  python ${LOCAL}/CategorizeTrees_v2.py --ch ${CHANNEL} --iD ${INDIR} --opt ${OPTION} --year ${YEAR} --oD ${OUTDIR} --nBoundaries  ${BinBoundaryTextFile} --f ${FINDSTRING} --syst ${IFSYST}
fi

if [[ ${OPTION} -eq  "Data" ]]; then
  python ${LOCAL}/CategorizeTrees_v2.py --ch ${CHANNEL} --iD ${INDIR} --opt ${OPTION} --year ${YEAR} --oD ${OUTDIR} --nBoundaries  ${BinBoundaryTextFile} --f ${FINDSTRING} --syst 0
fi

echo -e "DONE";
'''

  arguments=[]



  inDirStarts = [
     ##-- Binary
   #   "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production",
   "/eos/user/l/lipe/DNN_Evaluation_sample/2017/"
  ]


  # years = ["2016", "2017", "2018"]
  years = ["2017"]

  channel = "FH"
  indir = "/eos/user/l/lipe/DNN_Evaluation_sample/2017/"
  option = "Signal"
  whichsignal = "ZZ"
  year = 2017
  outdir = "/eos/user/l/lipe/DNN_Evaluation_sample/2017/CategorizeRootFileCondor/"
  binboundarytextfile = "BinBoundaries_20Apr.txt"
  findstring = "GluGluToHHTo2G2Z"
  ifSyst = 1
  whichNode = "cHHH1"

  arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, option, "WW", year, outdir, binboundarytextfile, "GluGluToHHTo2G2Z", ifSyst, whichNode))
  arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, option, "ZZ", year, outdir, binboundarytextfile, "GluGluToHHTo2G4Q", ifSyst, whichNode))

  # # SingleHiggs = [ "VHToGG", "VBFHToGG", "GluGluHToGG", "ttHJet" ]
  SingleHiggs = [ "ttHJet" ]

  for singleHiggsSample in SingleHiggs:
   arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, "SingleHiggs", "ZZ", year, outdir, binboundarytextfile, singleHiggsSample, ifSyst, whichNode))

  # Data
  # arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, "Data", "ZZ", year, outdir, binboundarytextfile, "Data", ifSyst, whichNode))

  with open("arguments_Signal.txt", "w") as args:
     args.write("\n".join(arguments))

  with open("run_script_Signal.sh", "w") as rs:
     rs.write(script)
