# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Date:   2021-04-20
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-04-21
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

  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('-y', '--Year', dest='Year', help='Year to run', default="2016", type=int)
  parser.add_argument('-s', '--ExtraString', dest='ExtraString', help='Extra string to be added in the condor file name', default="", type=str)

  args = parser.parse_args()
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
  condor = '''executable              = run_script_%s.sh
output                  = output/strips.$(ClusterId).$(ProcId).out
error                   = output/strips.$(ClusterId).$(ProcId).out
log                     = log/strips.$(ClusterId).log
transfer_input_files    = run_script_%s.sh,BinBoundaries_20Apr.txt
# on_exit_remove          = (ExitBySignal == False) && (ExitCode == 0)
# periodic_release        = (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > (60*60))

+JobFlavour             = "workday"
# +AccountingGroup      = "group_u_CMS.CAF.ALCA"
queue arguments from arguments_%s.txt
'''

  with open("condor_job_%s.txt"%(args.ExtraString), "w") as cnd_out:
     cnd_out.write(condor%(args.ExtraString,args.ExtraString,args.ExtraString))

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
TEMPDIR="."

# In condor jobs don't send the output directly to EOS. Keep them in condor local.
# Once the job is done move it to EOS. Condor job could send files directly to EOS,
# but I think this may be slow. While write to local should be fast.

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

if [[ ${OPTION} ==  "Signal" ]]; then
  echo "Inside signal condition"
  echo "==============="
  date
  echo "==============="
  python ${LOCAL}/CategorizeTrees.py --ch ${CHANNEL} --iD ${INDIR} --opt ${OPTION} --year ${YEAR} --oD ${TEMPDIR} --nBoundaries  ${BinBoundaryTextFile} --f ${FINDSTRING} --syst ${IFSYST} --WhichSig ${WHICHSIGNAL} --node ${WHICHNODE}
  echo "==============="
  echo "List all files"
  ls
  echo "==============="
  echo "mv *${FINDSTRING}*.root ${OUTDIR}/"
  mv *${FINDSTRING}*.root ${OUTDIR}/
  echo "==============="
  date
fi

if [[ ${OPTION} ==  "SingleHiggs" ]]; then
  echo "Inside SingleHiggs condition"
  echo "==============="
  date
  echo "==============="
  python ${LOCAL}/CategorizeTrees.py --ch ${CHANNEL} --iD ${INDIR} --opt ${OPTION} --year ${YEAR} --oD ${TEMPDIR} --nBoundaries  ${BinBoundaryTextFile} --f ${FINDSTRING} --syst ${IFSYST}
  echo "==============="
  echo "List all files"
  ls
  echo "==============="
  echo "mv *${FINDSTRING}*.root ${OUTDIR}/"
  mv *${FINDSTRING}*.root ${OUTDIR}/
  echo "==============="
  date
fi

if [[ ${OPTION} ==  "Data" ]]; then
  echo "Inside Data condition"
  echo "==============="
  date
  echo "==============="
  python ${LOCAL}/CategorizeTrees.py --ch ${CHANNEL} --iD ${INDIR} --opt ${OPTION} --year ${YEAR} --oD ${TEMPDIR} --nBoundaries  ${BinBoundaryTextFile} --f ${FINDSTRING} --syst 0
  echo "==============="
  echo "List all files"
  ls
  echo "==============="
  echo "mv *${FINDSTRING}*.root ${OUTDIR}/"
  mv *${FINDSTRING}*.root ${OUTDIR}/
  echo "==============="
  date
fi

echo -e "DONE";
'''

  arguments=[]



  inDirStarts = [
     ##-- Binary
   #   "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production",
   "/eos/user/l/lipe/DNN_Evaluation_sample/2016/"
   # "/eos/user/l/lipe/DNN_Evaluation_sample/2017/"
   # "/eos/user/l/lipe/DNN_Evaluation_sample/2018/"
  ]


  # years = ["2016", "2017", "2018"]
  years = ["2017"]

  channel = "FH"
  indir = "/eos/user/l/lipe/DNN_Evaluation_sample/2016/"
  option = "Signal"
  whichsignal = "ZZ"
  year = 2017
  # outdir = "/eos/user/l/lipe/DNN_Evaluation_sample/2017/CategorizeRootFileCondor_21Apr_v3/"
  outdir = "/eos/user/l/lipe/DNN_Evaluation_sample/2016/CategorizeRootFileCondor/"
  binboundarytextfile = "BinBoundaries_20Apr.txt"
  findstring = "GluGluToHHTo2G2Z"
  ifSyst = 1
  whichNode = "cHHH1"

  arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, option, "WW", year, outdir, binboundarytextfile, "GluGluToHHTo2G2Z", ifSyst, whichNode))
  arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, option, "ZZ", year, outdir, binboundarytextfile, "GluGluToHHTo2G4Q", ifSyst, whichNode))

  SingleHiggs = [ "VHToGG", "VBFHToGG", "GluGluHToGG", "ttHJet" ]
  # SingleHiggs = [ "ttHJet" ]

  for singleHiggsSample in SingleHiggs:
   arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, "SingleHiggs", "ZZ", year, outdir, binboundarytextfile, singleHiggsSample, ifSyst, whichNode))

  # # Data
  arguments.append("{} {} {} {} {} {} {} {} {} {} {}".format(local, channel, indir, "Data", "ZZ", year, outdir, binboundarytextfile, "Data", ifSyst, whichNode))

  with open("arguments_%s.txt"%(args.ExtraString), "w") as argFile:
     argFile.write("\n".join(arguments))

  with open("run_script_%s.sh"%(args.ExtraString), "w") as scriptFile:
     scriptFile.write(script)

