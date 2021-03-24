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

#!/usr/bin/env bash

TrainingLabel=$1
node=$2
year=$3
HHWWggSingleHiggsScale=$4

singleHiggs="tth,wzh,vbf,ggh"
WorkingDirectory="/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/"
phpLoc="/eos/user/a/atishelm/www/HHWWgg/DNN/index.php" ##-- Location of php file for copying to new website directories 

cd ${WorkingDirectory}
eval `scramv1 ru -sh`
source ./setup.sh

echo "==================="
echo "Start ${year} ${node}"
ext="SL_${TrainingLabel}"
procs='GluGluToHHTo2G2Qlnu'
website="/eos/user/a/atishelm/www/HHWWgg/DNN/${TrainingLabel}/fggfinalfit/"
mkdir -p ${website}/${year}/${node}
mkdir -p ${website}/${year}/Background
cp ${phpLoc} ${website}/${year}/
cp ${phpLoc} ${website}/${year}/Background/
cp ${phpLoc} ${website}/${year}/${node}/

UniqueExt=${ext}_${procs}_${year}

InputTreeCats='HHWWggTag_SL_0,HHWWggTag_SL_1,HHWWggTag_SL_2,HHWWggTag_SL_3' #input cat name in the Signal tree
InputDataTreeCats='HHWWggTag_SL_0,HHWWggTag_SL_1,HHWWggTag_SL_2,HHWWggTag_SL_3' #input cat name in the Data tree

cat='HHWWggTag_SLDNN_0,HHWWggTag_SLDNN_1,HHWWggTag_SLDNN_2,HHWWggTag_SLDNN_3' #Final cat name 

SignalTreeFile="/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/${year}/${TrainingLabel}/Signal_${node}_${year}_all_CategorizedTrees.root"
DataTreeFile="/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/${year}/${TrainingLabel}/Data_${year}_CategorizedTrees.root"
InputWorkspace="/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/Workspaces_${TrainingLabel}/"

Replace='HHWWggTag_SLDNN_0'
doSelections="0"
Selections='(1.)' # Selections you want to applied.
catNames=(${cat//,/ })

# ############################################
# #  Tree selectors#
# #
# ############################################

# ##-- If there is a dash in the extension replace it because can't name C function with dash 
# if [[ "${UniqueExt}" == *"-"* ]]; then
# 	UniqueFcnExt=${UniqueExt//[-]/_} ##--replace - with _ 
# else
# 	UniqueFcnExt=${UniqueExt}
# fi 

# cd ${WorkingDirectory}/Reweight/
# cp Selections.C Selections_Run_${UniqueFcnExt}.C
# cp DataSelections.C DataSelections_Run_${UniqueFcnExt}.C
# sed -i "s#NODE#${node}#g" Selections_Run_${UniqueFcnExt}.C 
# sed -i "s#NEW_Cat_NAME#${cat}#g" Selections_Run_${UniqueFcnExt}.C 
# sed -i "s#CAT#${InputTreeCats}#g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#PROCS#${procs}#g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#YEAR#${year}#g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#2017#${year}#g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#INPUTFILE#${SignalTreeFile}#g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#UNIQUEFCN#${UniqueFcnExt}#g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#Selections_Run#Selections_Run_${UniqueFcnExt}#g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#UNIQUEFCN#${UniqueFcnExt}#g" DataSelections_Run_${UniqueFcnExt}.C
# sed -i "s#DataSelections_Run#DataSelections_Run_${UniqueFcnExt}#g" DataSelections_Run_${UniqueFcnExt}.C

# sed -i "s#tagsDumper/trees/##g" Selections_Run_${UniqueFcnExt}.C
# sed -i "s#tagsDumper/trees/##g" DataSelections_Run_${UniqueFcnExt}.C

# if [ $year -eq "2018" ]
# then
#   sed -i "s#metUncUncertainty\\"#metUncUncertainty\\",\\"JetHEM\\"#g" Selections_Run_${UniqueFcnExt}.C
# fi
# ##########Data selection #####
#   sed -i "s#CAT#${InputDataTreeCats}#g" DataSelections_Run_${UniqueFcnExt}.C
#   sed -i "s#NEW_Cat_NAME#${cat}#g" DataSelections_Run_${UniqueFcnExt}.C 
#   sed -i "s#YEAR#${year}#g" DataSelections_Run_${UniqueFcnExt}.C
#   sed -i "s#INPUTFILE#${DataTreeFile}#g" DataSelections_Run_${UniqueFcnExt}.C


# if [ $doSelections -eq "1" ]
# then
#   echo "Selection start"
#   sed -i "s#SELECTIONS#${Selections}#g" Selections_Run_${UniqueFcnExt}.C
#   ##########Data selection #####
#   sed -i "s#SELECTIONS#${Selections}#g" DataSelections_Run_${UniqueFcnExt}.C

# else
#   echo "Do not apply any selections ,just copytree "
#   sed -i "s#SELECTIONS##g" Selections_Run_${UniqueFcnExt}.C # No Selection 
#   sed -i "s#SELECTIONS##g" DataSelections_Run_${UniqueFcnExt}.C #No Selection
# fi

# root -b -q  Selections_Run_${UniqueFcnExt}.C
# root -b -q DataSelections_Run_${UniqueFcnExt}.C
# rm Selections_Run_${UniqueFcnExt}.C
# rm DataSelections_Run_${UniqueFcnExt}.C

# SigOutFile=${procs}_node_${node}_${year}_${UniqueFcnExt}.root
# DataOutFile=Data_13TeV_${year}_${UniqueFcnExt}.root

# mv ${SigOutFile}  ../Trees2WS/
# mv ${DataOutFile} ../Trees2WS/

# cd ${WorkingDirectory}/Trees2WS/
# #########################################
# # start tree to workspace
# ########################################

# if [ ! -d "${InputWorkspace}/Signal/Input/${year}/" ]; then
#   mkdir -p ${InputWorkspace}/Signal/Input/${year}/
# fi
# # Signal tree to signal ws

# if [ $year -eq "2018" ] 
# then
#   echo "2018, remove prefire"
#   cp HHWWgg_config_noprefire.py HHWWgg_config_run_${UniqueExt}.py
# else
#   cp HHWWgg_config.py HHWWgg_config_run_${UniqueExt}.py
# fi
# sed -i "s#2017#${year}#g" HHWWgg_config_run_${UniqueExt}.py
# sed -i "s#auto#${cat}#g" HHWWgg_config_run_${UniqueExt}.py
# python trees2ws.py --inputConfig HHWWgg_config_run_${UniqueExt}.py --inputTreeFile ./${SigOutFile} --inputMass node_${node} --productionMode ${procs}  --year ${year} --doSystematics --UniqueName ${UniqueExt}
# # data tree to data ws
# python trees2ws_data.py --inputConfig HHWWgg_config_run_${UniqueExt}.py --inputTreeFile ./${DataOutFile} --UniqueName ${UniqueExt}
# rm HHWWgg_config_run_${UniqueExt}.py
# for catName in ${catNames[@]}
# do
#   if [ ! -d "${InputWorkspace}/Background/Input/${procs}_${year}" ]; then
#     mkdir -p ${InputWorkspace}/Background/Input/${procs}_${year}
#   fi
#   cp ws_${procs}_${UniqueExt}/${UniqueExt}.root ${InputWorkspace}/Signal/Input/${year}/Shifted_M125_${procs}_node_${node}_${catName}.root
#   cp ${InputWorkspace}/Signal/Input/${year}/Shifted_M125_${procs}_node_${node}_${catName}.root ${InputWorkspace}/Signal/Input/${year}/output_M125_${procs}_node_${node}_${catName}.root
#   cp ws_Data_${UniqueExt}/Data_${UniqueExt}.root ${InputWorkspace}/Background/Input/${procs}_${year}/allData.root
# done
# rm ${SigOutFile}
# rm ${DataOutFile}

# cd ${WorkingDirectory}/Signal/
# cp ./tools/replacementMapHHWWgg.py ./tools/replacementMap.py
# sed -i "s#REPLACEMET_CATWV#${Replace}#g" ./tools/replacementMap.py

# #######################################
# # Run ftest
# ######################################
# echo "Run FTest"
# cp HHWWgg_config_test.py HHWWgg_config_Run_${UniqueExt}.py
# sed -i "s#NODE#node_${node}#g" HHWWgg_config_Run_${UniqueExt}.py
# sed -i "s#YEAR#${year}#g" HHWWgg_config_Run_${UniqueExt}.py
# sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run_${UniqueExt}.py
# sed -i "s#CAT#${cat}#g" HHWWgg_config_Run_${UniqueExt}.py
# sed -i "s#HHWWggTest#${ext}#g" HHWWgg_config_Run_${UniqueExt}.py
# sed -i "s#INPUTDIR#${InputWorkspace}/Signal/Input/${year}/#g" HHWWgg_config_Run_${UniqueExt}.py
# python RunSignalScripts.py --inputConfig HHWWgg_config_Run_${UniqueExt}.py --mode fTest --modeOpts "--doPlots"

# #######################################
# # Run photon sys
# ######################################
# python RunSignalScripts.py --inputConfig HHWWgg_config_Run_${UniqueExt}.py --mode calcPhotonSyst

# #######################################
# #Run signal Fit
# #######################################
# python RunSignalScripts.py --inputConfig HHWWgg_config_Run_${UniqueExt}.py --mode signalFit --groupSignalFitJobsByCat
# for catName in ${catNames[@]}
# do
# 	cp outdir_${ext}_${year}_node_${node}/signalFit/output/CMS-HGG_sigfit_${ext}_${year}_node_${node}_${procs}_${year}_${catName}.root outdir_${ext}_${year}_node_${node}/CMS-HGG_sigfit_${ext}_${year}_node_${node}_${catName}.root
# 	python RunPlotter.py --procs all --years $year --cats $catName --ext ${ext}_${year}_node_${node} --HHWWggLabel $ext
# 	echo "COPYING PLOTS"
# 	echo "cp ${WorkingDirectory}/Signal/outdir_${ext}_${year}_node_${node}/Plots/* ${website}/${year}/${node}"
# 	cp ${WorkingDirectory}/Signal/outdir_${ext}_${year}_node_${node}/Plots/* ${website}/${year}/${node}
# done

# rm HHWWgg_config_Run_${UniqueExt}.py
# ########################################
# #           BKG model                  #
# #                                      #
# ########################################
# cd ${WorkingDirectory}/Background/
# cp HHWWgg_config_test.py HHWWgg_cofig_Run_${UniqueExt}.py
# sed -i "s#CAT#${cat}#g" HHWWgg_cofig_Run_${UniqueExt}.py
# sed -i "s#YEAR#${year}#g" HHWWgg_cofig_Run_${UniqueExt}.py
# sed -i "s#HHWWggTest#${ext}#g" HHWWgg_cofig_Run_${UniqueExt}.py
# sed -i "s#PROCS#${procs}#g" HHWWgg_cofig_Run_${UniqueExt}.py
# sed -i "s#INPUT#${InputWorkspace}#g" HHWWgg_cofig_Run_${UniqueExt}.py
# # make clean
# make

# python RunBackgroundScripts.py --inputConfig HHWWgg_cofig_Run_${UniqueExt}.py --mode fTestParallel
# echo "COPYING PLOTS"
# echo "cp outdir_${ext}_${year}/bkgfTest-Data/multipdf_HHWWggTag_*.png ${website}/${year}/Background/"
# echo "cp outdir_${ext}_${year}/bkgfTest-Data/multipdf_HHWWggTag_*.pdf ${website}/${year}/Background/"
# cp outdir_${ext}_${year}/bkgfTest-Data/multipdf_HHWWggTag_*.png ${website}/${year}/Background/
# cp outdir_${ext}_${year}/bkgfTest-Data/multipdf_HHWWggTag_*.pdf ${website}/${year}/Background/

# rm HHWWgg_cofig_Run_${UniqueExt}.py


########################################
#           DATACARD                   #
#                                      #
########################################
echo "Start generate datacard"
cd ${WorkingDirectory}/Datacard/
DatacardName="Datacard_${UniqueExt}"
rm ${DatacardName}*.txt
# rm Datacard*.txt
rm -rf yields_SingleHiggs_${UniqueExt}/
# cp systematics_${year}.py systematics_${UniqueExt}.py
# cp systematics_${year}.py systematics.py

# copy signal  and bkg model

outDirectory=SingleHiggs_${procs}_node_${node}_${ext}_${year}/
PrevStepDirec="SingleHiggs_${ext}_${year}/"

rm -rf ${outDirectory}
cp -rf SingleHiggs_${ext}_${year}/ ${outDirectory}
if [ ! -d "${outDirectory}/Models/" ]; then
  mkdir -p ./${outDirectory}/Models/
fi
####################
#
#   Add singleHiggs procs to RunYields.py 
###################

echo "python RunYields.py --cats ${cat} --inputWSDirMap ${year}=${InputWorkspace}/Signal/Input/${year} --procs ${procs},${singleHiggs} --doSystematics True --doHHWWgg True --HHWWggLabel node_${node} --batch local --ext SingleHiggs  --bkgModelWSDir ./Models --sigModelWSDir ./Models "
python RunYields.py --cats ${cat} --inputWSDirMap ${year}=${InputWorkspace}/Signal/Input/${year} --procs ${procs},${singleHiggs} --doSystematics True --doHHWWgg True --HHWWggLabel node_${node} --batch local --ext SingleHiggs_${UniqueExt}  --bkgModelWSDir ./Models --sigModelWSDir ./Models 
echo "python makeDatacard.py --years ${year} --prune True --ext SingleHiggs  --doSystematics True --pruneThreshold 0.000001 --output ${DatacardName}"
python makeDatacard.py --years ${year} --prune True --ext SingleHiggs_${UniqueExt}  --doSystematics True --pruneThreshold 0.000001 --output ${DatacardName}
echo "python cleanDatacard.py --datacard ${DatacardName}.txt --factor 2 --removeDoubleSided"
python cleanDatacard.py --datacard ${DatacardName}.txt --factor 2 --removeDoubleSided
cp ./${PrevStepDirec}*.root ${outDirectory}/Models/
for catName in ${catNames[@]}
do
	cp ${WorkingDirectory}/Background/outdir_${ext}_$year/CMS-HGG_multipdf_${catName}.root ./${outDirectory}/Models/CMS-HGG_multipdf_${catName}_$year.root
	cp ${WorkingDirectory}/Signal/outdir_${ext}_${year}_node_${node}/signalFit/output/CMS-HGG_sigfit_${ext}_${year}_node_${node}_${procs}_${year}_${catName}.root ./${outDirectory}/Models/CMS-HGG_sigfit_packaged_${procs}_${catName}_${year}.root
done
cp ${DatacardName}_cleaned.txt ./${outDirectory}/HHWWgg_${procs}_node_${node}_${ext}_${year}.txt

python RunYields.py --cats $cat --inputWSDirMap $year=${InputWorkspace}/Signal/Input/${year}/ --procs ${procs} --doHHWWgg True --HHWWggLabel node_${node} --batch local --sigModelWSDir ./Models --bkgModelWSDir ./Models --doSystematics True --ext ${procs}_node_${node}_${UniqueExt} 
python makeDatacard.py --years $year --prune True --ext ${procs}_node_${node}_${UniqueExt} --pruneThreshold 0.00001 --doSystematics --output ${DatacardName}
python cleanDatacard.py --datacard ${DatacardName}.txt --factor 2 --removeDoubleSided
cp ${DatacardName}_cleaned.txt ./${outDirectory}/HHWWgg_${procs}_node_${node}_${ext}_${year}_no_singleH.txt
datacards=`ls ./${outDirectory}/*.txt`
for datacard in $datacards
do
	echo "xs_HH         rateParam * GluGluToHHTo2G2Qlnu_*_hwwhgg_node_${node} 31.049" >>$datacard
	echo "br_HH_WWgg    rateParam * GluGluToHHTo2G2Qlnu_*_hwwhgg_node_${node} 0.000970198" >>$datacard
	echo "br_WW_qqlnu   rateParam * GluGluToHHTo2G2Qlnu_*_hwwhgg_node_${node} 0.441" >>$datacard

	echo "nuisance edit  freeze xs_HH" >> $datacard
	echo "nuisance edit  freeze br_WW_qqlnu" >>  $datacard
	echo "nuisance edit  freeze br_HH_WWgg" >> $datacard
done

if [[ "$HHWWggSingleHiggsScale" == "1" ]]; then
  ##-- Add factor of 2 to single higgs only if using half of original events to model 
  echo "ADDING FACTOR OF TWO TO SINGLE HIGGS PROCESSES ---- Should only be done if using half of original events to model"
  echo "FactorOfTwo   rateParam * *_${year}_hgg 2 " >> ${outDirectory}/HHWWgg_${procs}_node_${node}_${ext}_${year}.txt 
  echo "nuisance edit  freeze FactorOfTwo" >> ${outDirectory}/HHWWgg_${procs}_node_${node}_${ext}_${year}.txt
fi 

cd ./${outDirectory}
echo " "
echo " "
echo "Combine results without singleH:"
echo " "
echo " "
combine HHWWgg_${procs}_node_${node}_${ext}_${year}_no_singleH.txt  -m 125.38 -M AsymptoticLimits --run='blind' --freezeParameters MH --setParameters MH=125.38 --cminDefaultMinimizerStrategy 0  --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
 
mv higgsCombineTest.AsymptoticLimits.mH125.38.root ${WorkingDirectory}/CombineOutput/HHWWgg_${procs}_node_${node}_${ext}_${year}_no_singleH.root

echo " "
echo " "
echo "Combine results with singleH:"
echo " "
echo " "

combine HHWWgg_${procs}_node_${node}_${ext}_${year}.txt  -m 125.38 -M AsymptoticLimits --run='blind' --freezeParameters MH --setParameters MH=125.38 --cminDefaultMinimizerStrategy 0  --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
cd ${WorkingDirectory}

mv higgsCombineTest.AsymptoticLimits.mH125.38.root ${WorkingDirectory}/CombineOutput/HHWWgg_${procs}_node_${node}_${ext}_${year}.root

echo -e "DONE";

'''

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

	##-- Trainings, SingleHiggs, years, nodes 
	TrainingLabels = [
		# "HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM", 
		# "HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel", 
		"HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields"
		]

	SingleHiggs_Labels = [
		"tth", 
		"wzh", 
		"vbf", 
		"ggh"
		]

	years = [
		# "2016", 
		"2017", 
		# "2018"
		]	

	nodes = ["cHHH1"]

	arguments=[]

	for TrainingLabel in TrainingLabels:
		if("binary" in TrainingLabel):
			HHWWggSingleHiggsScale = "0"
		else:
			HHWWggSingleHiggsScale = "1"
		print("HHWWggSingleHiggsScale:",HHWWggSingleHiggsScale)

		for node in nodes:
			for year in years:
				##-- Get arguments for bash script 
				arguments.append("%s %s %s %s"%(TrainingLabel, node, year, str(HHWWggSingleHiggsScale))) 

	with open("arguments.txt", "w") as args:
		args.write("\n".join(arguments))
	with open("run_script.sh", "w") as rs:
		rs.write(script)

	# COMMAND = "condor_submit condor_job.txt"

	# print("SUBMITTING condor job")
	# print("COMMAND: %s"%(COMMAND))
	# os.system(COMMAND)

	print("DONE")
