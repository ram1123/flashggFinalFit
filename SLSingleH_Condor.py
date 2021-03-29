####################################################################################################
# 23 March 2021                                                                                    #
# Created by Badder Marzocchi and Tanvi Wamorkar                                                   #
# Edited by Abraham Tishelman-Charny                                                               #
#                                                                                                  #
# The purpose of this script is to create condor submission files.                                 #
####################################################################################################

#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
import itertools
from optparse import OptionParser
import operator
import os

if __name__ == '__main__':

	script = '''#!/bin/sh -e

WorkingDirectory="/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/"

TrainingLabel=$1;
procs=$2;
SHName=$3;
year=$4;
HHWWggSingleHiggsScale=$5;

echo "TrainingLabel: ${TrainingLabel}"
echo "procs: ${procs}"
echo "SHName: ${SHName}"
echo "year: ${year}"
echo "HHWWggSingleHiggsScale: ${HHWWggSingleHiggsScale}"

phpLoc="/eos/user/a/atishelm/www/HHWWgg/DNN/index.php" ##-- Location of php file for copying to new website directories 

cd ${WorkingDirectory}
eval `scramv1 ru -sh`
source ./setup.sh

Name="SingleHiggs_${SHName}_${year}_all_CategorizedTrees"
website="/eos/user/a/atishelm/www/HHWWgg/DNN/${TrainingLabel}/fggfinalfit/${year}/${procs}/"
mkdir -p ${website} 
cp ${phpLoc} /eos/user/a/atishelm/www/HHWWgg/DNN/${TrainingLabel}
cp ${phpLoc} /eos/user/a/atishelm/www/HHWWgg/DNN/${TrainingLabel}/fggfinalfit
cp ${phpLoc} /eos/user/a/atishelm/www/HHWWgg/DNN/${TrainingLabel}/fggfinalfit/${year}
cp ${phpLoc} ${website}

ext="SL_${TrainingLabel}"
UniqueExt=${ext}_${procs}_${year}
cat='HHWWggTag_SLDNN_0,HHWWggTag_SLDNN_1,HHWWggTag_SLDNN_2,HHWWggTag_SLDNN_3' #output cat name, it will be used in subsequence step
InputTreeCats='HHWWggTag_SL_0,HHWWggTag_SL_1,HHWWggTag_SL_2,HHWWggTag_SL_3' #input cat name in the tree
catNames=(${cat//,/ })
mass='125'

TreePath="/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/${year}/${TrainingLabel}/Single_H/"
InputWorkspace="/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/Workspaces_${TrainingLabel}/"
mkdir -p ${InputWorkspace}
doSelections="0"
Selections='(1.)' # Selections you want to applied.
# Replace="HHWWggTag_SLDNN_0"
Replace="HHWWggTag_SLDNN_3" 

############################################
#  Tree selectors#
#
############################################
# cp ./Signal/tools/replacementMapHHWWgg.py ./Signal/tools/replacementMap.py
# sed -i "s#REPLACEMET_CATWV#${Replace}#g" ./Signal/tools/replacementMap.py
cd ${WorkingDirectory}/Reweight
echo $Name $procs


##-- If there is a dash in the extension replace it because can't name C function with dash 
if [[ "${UniqueExt}" == *"-"* ]]; then
	UniqueFcnExt=${UniqueExt//[-]/_} ##--replace - with _ 
else
	UniqueFcnExt=${UniqueExt}
fi 

cp SingleHiggsSelections.C SingleHiggsSelections_Run_${UniqueFcnExt}.C
sed -i "s#NEW_Cat_NAME#${cat}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C 
sed -i "s#NAME#${Name}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C 
sed -i "s#CAT#${InputTreeCats}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C
sed -i "s#PROCS#${procs}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C
sed -i "s#YEAR#${year}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C
sed -i "s#2017#${year}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C
sed -i "s#INPUTPATH#${TreePath}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C
sed -i "s#UNIQUEPATH#${UniqueFcnExt}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C   
sed -i "s#SingleHiggsSelections_Run#SingleHiggsSelections_Run_${UniqueFcnExt}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C ##-- Pretty bad but should work 

# if [ "$ext" = "SL" ]
# then
sed -i "s#tagsDumper/trees/##g" SingleHiggsSelections_Run_${UniqueFcnExt}.C ##-- Assuming TDirectory structure 
# fi

if [ $doSelections -eq "1" ]
then
echo "Selection start"
sed -i "s#SELECTIONS#${Selections}#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C
else
echo "Do not apply any selections ,just copytree "
sed -i "s#SELECTIONS##g" SingleHiggsSelections_Run_${UniqueFcnExt}.C # No Selection 
fi
if [ $year -eq "2018" ]
then
sed -i "s#metUncUncertainty\\"#metUncUncertainty\\",\\"JetHEM\\"#g" SingleHiggsSelections_Run_${UniqueFcnExt}.C ##-- Note that double slash is needed for interpretation as single slash when going from string --> write(script)
fi

root -b -q SingleHiggsSelections_Run_${UniqueFcnExt}.C
outFile=${Name}_${year}_${UniqueFcnExt}.root
mv ${outFile}  ../Trees2WS/
rm SingleHiggsSelections_Run_${UniqueFcnExt}.C
cd ${WorkingDirectory}/Trees2WS/

#########################################
# start tree to workspace
########################################

if [ ! -d "$InputWorkspace/Signal/Input/${year}/" ]; then
  mkdir -p $InputWorkspace/Signal/Input/${year}
fi
# Signal tree to data ws
if [ $year -eq "2018" ]
then
echo " 2018, remove prefire"
cp HHWWgg_config_noprefire.py HHWWgg_config_run_${UniqueExt}.py
else
cp HHWWgg_config.py HHWWgg_config_run_${UniqueExt}.py
fi
sed -i "s#2017#${year}#g" HHWWgg_config_run_${UniqueExt}.py
sed -i "s#auto#${cat}#g" HHWWgg_config_run_${UniqueExt}.py
python trees2ws.py --inputConfig HHWWgg_config_run_${UniqueExt}.py --inputTreeFile ./${outFile}  --inputMass ${mass} --productionMode ${procs}  --year ${year} --doSystematics --UniqueName ${UniqueExt}
rm HHWWgg_config_run_${UniqueExt}.py
for catName in ${catNames[@]}
do
# /ws_ggh_SL_HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_ggh_2016/SingleHiggs_GluGluHToGG_2016_all_CategorizedTrees_2016_SL_HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_ggh_2016_ggh.root
cp ws_${procs}_${UniqueExt}/${UniqueExt}.root $InputWorkspace/Signal/Input/${year}/Shifted_M125_${procs}_${catName}.root
cp ws_${procs}_${UniqueExt}/${UniqueExt}.root $InputWorkspace/Signal/Input/${year}/output_M125_${procs}_${catName}.root
done
rm ${outFile}

#######################################
# Run ftest
######################################
echo "Run FTest"
cd ${WorkingDirectory}/Signal/

cp HHWWgg_single_higgs.py HHWWgg_config_Run_${UniqueExt}.py
sed -i "s#NODE#node_${node}#g" HHWWgg_config_Run_${UniqueExt}.py
sed -i "s#YEAR#${year}#g" HHWWgg_config_Run_${UniqueExt}.py
sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run_${UniqueExt}.py
sed -i "s#HHWWggTest#${ext}#g" HHWWgg_config_Run_${UniqueExt}.py
sed -i "s#CAT#${cat}#g" HHWWgg_config_Run_${UniqueExt}.py
sed -i "s#INPUTDIR#${InputWorkspace}/Signal/Input/${year}/#g" HHWWgg_config_Run_${UniqueExt}.py
python RunSignalScripts.py --inputConfig HHWWgg_config_Run_${UniqueExt}.py --mode fTest --modeOpts "doPlots"

#######################################
# Run photon sys
######################################
python RunSignalScripts.py --inputConfig HHWWgg_config_Run_${UniqueExt}.py --mode calcPhotonSyst

#######################################
#Run signal Fit
#######################################
python RunSignalScripts.py --inputConfig HHWWgg_config_Run_${UniqueExt}.py --mode signalFit --groupSignalFitJobsByCat
for catName in ${catNames[@]}
do
  echo "catName: ${catName}"
  mkdir -p outdir_${ext}_${procs}_${year}_single_Higgs/
  cp ${WorkingDirectory}/Signal/outdir_${ext}_${year}_single_Higgs/signalFit/output/CMS-HGG_sigfit_${ext}_${year}_single_Higgs_${procs}_${year}_${catName}.root outdir_${ext}_${procs}_${year}_single_Higgs/CMS-HGG_sigfit_${ext}_${procs}_${year}_single_Higgs_${catName}.root
  echo "COMMAND:"
  if [[ "$HHWWggSingleHiggsScale" == "1" ]]; then
    echo "Scaling Single Higgs by 2 - Should Only do this if evaluating on half of events"
    echo "python RunPlotter.py --procs all --years $year --cats $catName --ext ${ext}_${procs}_${year}_single_Higgs --HHWWggLabel ${ext}_${procs} --HHWWggSingleHiggsScale"
    python RunPlotter.py --procs all --years $year --cats $catName --ext ${ext}_${procs}_${year}_single_Higgs --HHWWggLabel ${ext}_${procs} --HHWWggSingleHiggsScale
  else
    echo "NOT Scaling Single Higgs by 2"
    echo "python RunPlotter.py --procs all --years $year --cats $catName --ext ${ext}_${procs}_${year}_single_Higgs --HHWWggLabel ${ext}_${procs}"
    python RunPlotter.py --procs all --years $year --cats $catName --ext ${ext}_${procs}_${year}_single_Higgs --HHWWggLabel ${ext}_${procs}   
  fi 

  echo "COPYING PLOTS:"
  echo "cp ${WorkingDirectory}/Signal/outdir_${ext}_${procs}_${year}_single_Higgs/Plots/*.png ${website}"
  echo "cp ${WorkingDirectory}/Signal/outdir_${ext}_${procs}_${year}_single_Higgs/Plots/*.pdf ${website}"
  cp ${WorkingDirectory}/Signal/outdir_${ext}_${procs}_${year}_single_Higgs/Plots/*.png ${website}
  cp ${WorkingDirectory}/Signal/outdir_${ext}_${procs}_${year}_single_Higgs/Plots/*.pdf ${website}
done

rm HHWWgg_config_Run_${UniqueExt}.py

########################################
#           DATACARD                   #
#                                      #
########################################
echo "Start generate datacard(no systematics)"
# cd ../Datacard
cd ${WorkingDirectory}/Datacard/
if [ ! -d "./SingleHiggs_${ext}_${year}" ]; then
  mkdir -p ./SingleHiggs_${ext}_${year}/
fi
# rm Datacard*.txt
# rm -rf yields_test/
#copy signal model
for catName in ${catNames[@]}
do
cp ${WorkingDirectory}/Signal/outdir_${ext}_${year}_single_Higgs/signalFit/output/CMS-HGG_sigfit_${ext}_${year}_single_Higgs_${procs}_${year}_${catName}.root ./SingleHiggs_${ext}_${year}/CMS-HGG_sigfit_packaged_${procs}_${catName}_${year}.root 
done
cd ${WorkingDirectory}

echo -e "DONE";

'''

# 	condor = '''executable              = run_script.sh
# output                  = {Condor_Extension}/output/job.$(ClusterId).$(ProcId).out
# error                   = {Condor_Extension}/error/job.$(ClusterId).$(ProcId).err
# log                     = {Condor_Extension}/log/job.$(ClusterId).log
# transfer_input_files    = run_script.sh
# # on_exit_remove          = (ExitBySignal == False) && (ExitCode == 0)
# # periodic_release        = (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > (60*60))
# +JobFlavour             = "microcentury"
# queue arguments from arguments.txt
# '''

	condor = '''executable              = run_script.sh
output                  = output/job.$(ClusterId).$(ProcId).out
error                   = error/job.$(ClusterId).$(ProcId).err
log                     = log/job.$(ClusterId).log
transfer_input_files    = run_script.sh
# on_exit_remove          = (ExitBySignal == False) && (ExitCode == 0)
# periodic_release        = (NumJobStarts < 3) && ((CurrentTime - EnteredCurrentStatus) > (60*60))
+JobFlavour             = "longlunch"
queue arguments from arguments.txt
'''

	if not os.path.isdir('error'): os.mkdir('error')
	if not os.path.isdir('output'): os.mkdir('output')
	if not os.path.isdir('log'): os.mkdir('log')				

	# condor = condor.replace("{Condor_Extension}", Condor_Extension)

	with open("condor_job.txt", "w") as cnd_out:
		cnd_out.write(condor)

	##-- Create condor submission file for each training, process, year combination 

	##-- All Trainings, processes, years 
	TrainingLabels = [
		# "HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM", 
		# "HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel", 
		"HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields"
		]

	SingleHiggs_Labels = [
		"tth", 
		# "wzh", 
		# "vbf", 
		# "ggh"
		]

	years = [
		# "2016", 
		"2017", 
		# "2018"
		]	

	# ##-- Shorter test 
	# TrainingLabels = ["HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM"]
	# SingleHiggs_Labels = ["ggh"]  
	# years = ["2018"]

	##-- Single Higgs info from process 
	SingleHiggsInfo = {
		"ggh" : "GluGluHToGG",
		"vbf" : "VBFHToGG",
		"wzh" : "VHToGG",
		"tth" : "ttHJetToGG"
	}

	arguments=[]

	for TrainingLabel in TrainingLabels:
		if("binary" in TrainingLabel):
			HHWWggSingleHiggsScale = "0"
		else:
			HHWWggSingleHiggsScale = "1"
		print("HHWWggSingleHiggsScale:",HHWWggSingleHiggsScale)
		for SingleHiggs_Label in SingleHiggs_Labels:
			for year in years:
				FullSingleHiggsName = SingleHiggsInfo[SingleHiggs_Label]

				##-- Get arguments for bash script 
				arguments.append("%s %s %s %s %s"%(TrainingLabel, SingleHiggs_Label, FullSingleHiggsName, year, str(HHWWggSingleHiggsScale))) 

				##-- Setup condor submission   
				# Condor_Extension = "Condor_%s_%s_%s"%(TrainingLabel, FullSingleHiggsName, year) ##-- For condor out, log, err directory 

				# if not os.path.isdir(Condor_Extension): os.mkdir(Condor_Extension)
				# if not os.path.isdir('%s/error'%(Condor_Extension)): os.mkdir('%s/error'%(Condor_Extension))
				# if not os.path.isdir('%s/output'%(Condor_Extension)): os.mkdir('%s/output'%(Condor_Extension))
				# if not os.path.isdir('%s/log'%(Condor_Extension)): os.mkdir('%s/log'%(Condor_Extension))

	with open("arguments.txt", "w") as args:
		args.write("\n".join(arguments))
	with open("run_script.sh", "w") as rs:
		rs.write(script)

	# COMMAND = "condor_submit condor_job.txt"

	# print("SUBMITTING condor job")
	# print("COMMAND: %s"%(COMMAND))
	# os.system(COMMAND)

	print("DONE")
