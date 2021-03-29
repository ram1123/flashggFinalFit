#!/usr/bin/env bash
node=("cHHH1")
singleHiggs="tth,wzh,vbf,ggh"
echo "==================="

# TrainingLabel="HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM"
TrainingLabel="HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel"
HHWWggSingleHiggsScale="0"
phpLoc="/eos/user/a/atishelm/www/HHWWgg/DNN/index.php" ##-- Location of php file for copying to new website directories 

ext="SL_Run2combinedData_${TrainingLabel}"
procs='GluGluToHHTo2G2Qlnu'
cat='HHWWggTag_SLDNN_0,HHWWggTag_SLDNN_1,HHWWggTag_SLDNN_2,HHWWggTag_SLDNN_3' #Final cat name 
InputWorkspace="/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/Workspaces_${TrainingLabel}/"
hadd_workspaceDir="/afs/cern.ch/work/a/atishelm/private/flashgg-10_6_8/CMSSW_10_6_8/src/flashgg/"
catNames=(${cat//,/ })
WorkingDirectory="/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/"
SingleYearExt="SL_${TrainingLabel}"

########################################
#           hadd_workspace             #
#                                      #
########################################
cd $hadd_workspaceDir 
eval `scramv1 runtime -sh`
cd $InputWorkspace
cd Background/Input/
mkdir $ext
cd $ext
cp ../${procs}_2016/allData.root Data2016.root
cp ../${procs}_2017/allData.root Data2017.root
cp ../${procs}_2018/allData.root Data2018.root
hadd_workspaces allData.root Data201*

########################################
#           BKG model                  #
#                                      #
########################################
cd ${WorkingDirectory}
eval `scramv1 runtime -sh`
source ./setup.sh
cd ./Background
cp HHWWgg_config_test.py HHWWgg_config_Run.py
sed -i "s#CAT#${cat}#g" HHWWgg_config_Run.py
sed -i "s#PROCS_YEAR#${ext}#g" HHWWgg_config_Run.py
sed -i "s#HHWWggTest_YEAR#${ext}#g" HHWWgg_config_Run.py
sed -i "s#YEAR#combined#g" HHWWgg_config_Run.py
sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run.py
sed -i "s#INPUT#${InputWorkspace}#g" HHWWgg_config_Run.py
# make clean
make

python RunBackgroundScripts.py --inputConfig HHWWgg_config_Run.py --mode fTestParallel
rm HHWWgg_config_Run.py

########################################
#           DATACARD                   #
#                                      #
########################################
echo "Start generate datacard"
cd ../Datacard
rm Datacard*.txt
rm -rf yields_*/
rm -rf ./SL_run2_${ext}
cp systematics_merged.py systematics.py
#copy signal  and bkg model
if [ ! -d "./SL_run2_${ext}/Models/" ]; then
  mkdir -p ./SL_run2_${ext}/Models/
fi

####################
#
#   Add singleHiggs procs to RunYields.py 
###################
cd ${WorkingDirectory}/Datacard/
cp ${WorkingDirectory}/Background/outdir_${ext}/CMS-HGG_multipdf_*.root ./SL_run2_${ext}/Models/
cp -rf ./SingleHiggs_${procs}_node_${node}_${SingleYearExt}_2016/* SL_run2_${ext}/
cp -rf ./SingleHiggs_${procs}_node_${node}_${SingleYearExt}_2017/* SL_run2_${ext}/
cp -rf ./SingleHiggs_${procs}_node_${node}_${SingleYearExt}_2018/* SL_run2_${ext}/

python RunYields.py --cats ${cat} --inputWSDirMap 2016=${InputWorkspace}/Signal/Input/2016,2017=${InputWorkspace}/Signal/Input/2017,2018=${InputWorkspace}/Signal/Input/2018/ --procs ${procs},${singleHiggs} --doSystematics True --doHHWWgg True --HHWWggLabel node_${node} --batch local --ext SingleHiggs  --bkgModelWSDir ./Models --sigModelWSDir ./Models --mergeYears True --ignore-warnings True
python makeDatacard.py --years 2016,2017,2018 --prune True --ext SingleHiggs --pruneThreshold 0.00001 --doSystematics
python cleanDatacard.py --datacard Datacard.txt --factor 2 --removeDoubleSided
cp Datacard_cleaned.txt  SL_run2_${ext}/SL_run2_merged.txt
# cd SL_run2_${ext}/
cd ${WorkingDirectory}/Datacard/SL_run2_${ext}/
echo "xs_HH         rateParam * GluGluToHHTo2G2Qlnu_*_hwwhgg_node_${node} 31.049" >>SL_run2_merged.txt
echo "br_HH_WWgg    rateParam * GluGluToHHTo2G2Qlnu_*_hwwhgg_node_${node} 0.000970198" >>SL_run2_merged.txt
echo "br_WW_qqlnu   rateParam * GluGluToHHTo2G2Qlnu_*_hwwhgg_node_${node} 0.441" >> SL_run2_merged.txt
echo "nuisance edit  freeze xs_HH" >> SL_run2_merged.txt
echo "nuisance edit  freeze br_WW_qqlnu" >> SL_run2_merged.txt
echo "nuisance edit  freeze br_HH_WWgg" >> SL_run2_merged.txt 

if [[ "$HHWWggSingleHiggsScale" == "1" ]]; then

  ##-- Add factor of 2 to single higgs only if using half of original events to model 
  echo "ADDING FACTOR OF TWO TO SINGLE HIGGS PROCESSES ---- Should only be done if using half of original events to model"
  echo "FactorOfTwo   rateParam * ggh_*_hgg 2 " >> SL_run2_merged.txt
  echo "FactorOfTwo   rateParam * vbf_*_hgg 2 " >> SL_run2_merged.txt
  echo "FactorOfTwo   rateParam * wzh_*_hgg 2 " >> SL_run2_merged.txt
  echo "FactorOfTwo   rateParam * tth_*_hgg 2 " >> SL_run2_merged.txt
  echo "nuisance edit  freeze FactorOfTwo" >> SL_run2_merged.txt

fi 

combineCards.py HHWWgg_${procs}_node_${node}_${ext}_2016.txt HHWWgg_${procs}_node_${node}_${ext}_2017.txt HHWWgg_${procs}_node_${node}_${ext}_2018.txt > SL_run2_separate_year.txt
echo "Combine results with merged:"
combine SL_run2_merged.txt  -m 125.38 -M AsymptoticLimits --run='blind' --freezeParameters MH -t -1 --setParameters MH=125.38 --cminDefaultMinimizerStrategy 0  --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
echo "Combine results with separate data:"
combine SL_run2_separate_year.txt -m 125.38 -M AsymptoticLimits --run='blind' --freezeParameters MH -t -1 --setParameters MH=125.38 --cminDefaultMinimizerStrategy 0  --cminFallbackAlgo Minuit2,Migrad,0:0.1 --X-rt MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2
cd ${WorkingDirectory}
