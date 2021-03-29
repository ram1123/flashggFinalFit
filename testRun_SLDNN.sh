#!/usr/bin/env bash
node="cHHH1"
procs='GluGluToHHTo2G2Qlnu'
year='2017'
doHHWWgg="True"
# cat='HHWWggTag_0'
cats='HHWWggTag_0,HHWWggTag_1,HHWWggTag_2,HHWWggTag_3'
#TreePath='/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2017/Signal/FL_NLO_2017_hadded/'
TreePath='/afs/cern.ch/work/a/atishelm/private/fggfinalfit_lite_HHWWgg/CMSSW_10_2_13/src/flashggFinalFit/DNNSignal/'
DataDirec='/afs/cern.ch/work/a/atishelm/private/fggfinalfit_lite_HHWWgg/CMSSW_10_2_13/src/flashggFinalFit/DNNData/'
DataTreeFile='/afs/cern.ch/work/a/atishelm/private/fggfinalfit_lite_HHWWgg/CMSSW_10_2_13/src/flashggFinalFit/DNNData/Data_2017.root'
doSelections="0"
Selections='(1)' # Seletions you want to applied.
# eval `scramv1 runtime -sh`
source ./setup.sh

#########################################
# start tree to workspace
########################################

# cd Trees2WS
# for cat in HHWWggTag_0 HHWWggTag_1 HHWWggTag_2 HHWWggTag_3
# do 
#   if [ ! -d "../Signal/Input/" ]; then
#     mkdir ../Signal/Input/
#   fi
#   if [ ! -d "../Background/Input/${procs}_${cat}_${year}" ]; then
#     mkdir -p ../Background/Input/${procs}_${cat}_${year}
#   fi
#   # python trees2ws.py --inputConfig HHWWgg_config.py --inputTreeFile ${TreePath}/${procs}_node_${node}_${year}.root --inputMass node_${node} --productionMode ${procs}  --year ${year}/
#   python trees2ws_data.py --inputConfig HHWWgg_config.py --inputTreeFile ${DataTreeFile}
#   # mv ${TreePath}/ws_${procs}/${procs}_node_${node}_${year}_${procs}.root ../Signal/Input/output_M125_${procs}_node_${node}_${cat}.root
#   mv ${DataDirec}/ws/Data_${year}.root ../Background/Input/${procs}_${cat}_${year}/allData.root
# done 
# cd .. 

# # # Signal tree to signal ws
# # # python trees2ws.py --inputConfig HHWWgg_config.py --inputTreeFile ${TreePath}/${procs}_node_${node}_${year}.root --inputMass node_${node} --productionMode ${procs}  --year ${year} --doSystematics

# # # data tree to data ws
# # # python trees2ws_data.py --inputConfig HHWWgg_config.py --inputTreeFile ./Data_13TeV_${cat}_${year}.root


# # # mv ws_${procs}/${procs}_node_${node}_${year}_${procs}.root ../Signal/Input/output_M125_${procs}_node_${node}_${cat}.root
# # # mv ws_${procs}/${procs}_node_${node}_${year}_${procs}.root ../Signal/Input/output_M125_${procs}_node_${node}_${cat}.root
# # # mv ws/Data_13TeV_${cat}_${year}.root ../Background/Input/${procs}_${cat}_${year}/allData.root
# # # rm ${procs}_node_${node}_${year}.root
# # # rm Data_13TeV_${cat}_${year}.root
# mv ${TreePath}/ws_${procs}/${procs}_node_${node}_${year}_${procs}.root ../Signal/Input/output_M125_${procs}_node_${node}_${cat}.root
# mv ${DataDirec}/ws/Data_${year}.root ../Background/Input/${procs}_${cat}_${year}/allData.root



# #########################################
# #shift dataset
# #########################################
# cd ../Signal/
# cd Signal 
# python ./scripts/shiftHiggsDatasets_test.py --inputDir ./Input/ --procs ${procs} --cats ${cats} --HHWWggLabel node_${node}

# #######################################
# # Run ftest
# ######################################
# cd Signal 
# # # echo "Run FTest"
# # cp HHWWgg_config_test.py HHWWgg_config_Run.py
# # sed -i "s#NODE#node_${node}#g" HHWWgg_config_Run.py
# # sed -i "s#YEAR#${year}#g" HHWWgg_config_Run.py
# # sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run.py
# # sed -i "s#CAT#${cats}#g" HHWWgg_config_Run.py
# # # sed -i "s#INPUTDIR#${path}/Signal/Input/#g" HHWWgg_config_Run.py
# # sed -i "s#INPUTDIR#./Input/#g" HHWWgg_config_Run.py
# # python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode fTest --modeOpts "doPlots"

# for cat in HHWWggTag_0 HHWWggTag_1 HHWWggTag_2 HHWWggTag_3
# do 
#   cp HHWWgg_config_test.py HHWWgg_config_Run.py
#   sed -i "s#NODE#node_${node}#g" HHWWgg_config_Run.py
#   sed -i "s#YEAR#${year}#g" HHWWgg_config_Run.py
#   sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run.py
#   sed -i "s#CAT#${cat}#g" HHWWgg_config_Run.py
#   # sed -i "s#INPUTDIR#${path}/Signal/Input/#g" HHWWgg_config_Run.py
#   sed -i "s#INPUTDIR#./Input/#g" HHWWgg_config_Run.py
#   python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode fTest --modeOpts "doPlots"  
# done 

# #######################################
# # Run photon sys
# ######################################
# cd Signal 
# python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode calcPhotonSyst


# #######################################
# #Run signal Fit
# #######################################
# cd Signal 
# python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode signalFit --groupSignalFitJobsByCat 
# cp outdir_HHWWggTest_${year}_node_${node}/signalFit/output/CMS-HGG_sigfit_HHWWggTest_${year}_node_${node}_${procs}_${year}_${cat}.root outdir_HHWWggTest_${year}_node_${node}/CMS-HGG_sigfit_HHWWggTest_${year}_node_${node}_${cat}.root
# python RunPlotter.py --procs all --years $year --cats $cat --ext HHWWggTest_${year}_node_${node}


# cd Signal 

# for cat in HHWWggTag_0 HHWWggTag_1 HHWWggTag_2 HHWWggTag_3
# do 
#   cp HHWWgg_config_test.py HHWWgg_config_Run.py
#   sed -i "s#NODE#node_${node}#g" HHWWgg_config_Run.py
#   sed -i "s#YEAR#${year}#g" HHWWgg_config_Run.py
#   sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run.py
#   sed -i "s#CAT#${cat}#g" HHWWgg_config_Run.py
#   # sed -i "s#INPUTDIR#${path}/Signal/Input/#g" HHWWgg_config_Run.py
#   sed -i "s#INPUTDIR#./Input/#g" HHWWgg_config_Run.py
#   python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode signalFit --groupSignalFitJobsByCat 
#   cp outdir_HHWWggTest_${year}_node_${node}/signalFit/output/CMS-HGG_sigfit_HHWWggTest_${year}_node_${node}_${procs}_${year}_${cat}.root outdir_HHWWggTest_${year}_node_${node}/CMS-HGG_sigfit_HHWWggTest_${year}_node_${node}_${cat}.root
#   python RunPlotter.py --procs all --years $year --cats $cat --ext HHWWggTest_${year}_node_${node}
  
# done 


# rm HHWWgg_config_Run.py

# ########################################
# #           BKG model                  #
# #                                      #
# ########################################

# cd Background 
# for cat in HHWWggTag_0 HHWWggTag_1 HHWWggTag_2 HHWWggTag_3
# do 
#   cp HHWWgg_cofig_test.py HHWWgg_config_Run.py
#   sed -i "s#CAT#${cat}#g" HHWWgg_config_Run.py
#   sed -i "s#YEAR#${year}#g" HHWWgg_config_Run.py
#   sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run.py  
#   # cmsenv 
#   # make clean 
#   # make 
#   python RunBackgroundScripts.py --inputConfig HHWWgg_config_Run.py --mode fTestParallel
# done 


# cd ../Background
# cp Trees2WS/HHWWgg_config_test.py Background/HHWWgg_config_Run.py
# cd Background
# cp HHWWgg_cofig_test.py HHWWgg_config_Run.py
# sed -i "s#CAT#${cat}#g" HHWWgg_config_Run.py
# sed -i "s#YEAR#${year}#g" HHWWgg_config_Run.py
# sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run.py
# # cmsenv
# # make clean
# # make

# python RunBackgroundScripts.py --inputConfig HHWWgg_config_Run.py --mode fTestParallel

# rm HHWWgg_cofig_Run.py

# ########################################
# #           DATACARD                   #
# #                                      #
# ########################################

cd Datacard 
for cat in HHWWggTag_0 HHWWggTag_1 HHWWggTag_2 HHWWggTag_3
do
  if [ ! -d "./${procs}_node_${node}/${procs}_node_${node}/" ]; then
    mkdir -p ./${procs}_node_${node}/${procs}_node_${node}
  fi   
  python RunYields.py --cats $cat --inputWSDirMap $year=../Signal/Input/ --procs ${procs} --doHHWWgg ${doHHWWgg} --HHWWggLabel node_${node} --batch local --sigModelWSDir ./Models --bkgModelWSDir ./Models --doSystematics --ext ${procs}_node_${node}
  python makeDatacard.py --years $year --prune True --ext ${procs}_node_${node} --pruneThreshold 0.00001 --doSystematics 
  python cleanDatacard.py --datacard Datacard.txt --factor 2 --removeDoubleSided 
  mv Datacard_cleaned.txt Datacard_cleaned_${cat}.txt 
done 

# echo "Start generate datacard"
# cd Datacard
# # cd ../Datacard
# if [ ! -d "./${procs}_node_${node}/${procs}_node_${node}/" ]; then
#   mkdir -p ./${procs}_node_${node}/${procs}_node_${node}
# fi
# rm Datacard*.txt
# rm -rf yields_*/
# #copy signal  and bkg model

# python RunYields.py --cats $cat --inputWSDirMap $year=../Signal/Input/ --procs ${procs} --doHHWWgg ${doHHWWgg} --HHWWggLabel node_${node} --batch local --sigModelWSDir ./Models --bkgModelWSDir ./Models --doSystematics --ext ${procs}_node_${node}
# python makeDatacard.py --years $year --prune True --ext ${procs}_node_${node} --pruneThreshold 0.00001 --doSystematics
# # python makeDatacard.py --years $year --prune True --ext ${procs}_node_${node} --pruneThreshold 0.00001 
# python cleanDatacard.py --datacard Datacard.txt --factor 2 --removeDoubleSided
# cp Datacard_cleaned.txt ./SingleHiggs_${procs}_node_${node}/HHWWgg_${procs}_node_${node}_${cat}_${year}_no_singleH.txt






# cp -rf SingleHiggs SingleHiggs_${procs}_node_${node}
# if [ ! -d "./SingleHiggs_${procs}_node_${node}/Models/" ]; then
  # mkdir -p ./SingleHiggs_${procs}_node_${node}/Models/
# fi
#   ####################
#   #
#   #   Add singleHiggs procs to RunYields.py 
#   ###################
#   python RunYields.py --cats ${cat} --inputWSDirMap 2017=${path}/Signal/Input --procs ${procs},tth,vbf,wzh,ggh --doSystematics --doHHWWgg True --HHWWggLabel node_${node} --batch local --ext SingleHiggs  --bkgModelWSDir ./Models --sigModelWSDir ./Models
#   ####################
#   echo "python RunYields.py --cats HHWWggTag_2 --inputWSDirMap 2017=/afs/cern.ch/user/c/chuw/chuw/HHWWgg/FinalFit/CMSSW_10_2_13/src/flashggFinalFit/Signal/Input --procs tth,GluGluToHHTo2G2l2nu,vbf,wzh --doSystematics --doHHWWgg True --HHWWggLabel node_cHHH1 --batch local --ext SingleHiggs  --bkgModelWSDir ./Models --sigModelWSDir ./Models"
#   python makeDatacard.py --years 2017 --prune True --ext SingleHiggs  --doSystematics --pruneThreshold 0.00001
#   python cleanDatacard.py --datacard Datacard.txt --factor 2 --removeDoubleSided
#   mv ./SingleHiggs_${procs}_node_${node}/*${cat}*.root SingleHiggs_${procs}_node_${node}/Models/
#   cp ${path}/Background/outdir_HHWWggTest_$year/CMS-HGG_multipdf_${cat}.root ./SingleHiggs_${procs}_node_${node}/Models/CMS-HGG_multipdf_${cat}_$year.root 
#   cp ${path}/Signal/outdir_HHWWggTest_${year}_node_${node}/signalFit/output/CMS-HGG_sigfit_HHWWggTest_${year}_node_${node}_${procs}_${year}_${cat}.root ./SingleHiggs_${procs}_node_${node}/Models/CMS-HGG_sigfit_packaged_${procs}_${cat}_${year}.root 
#   cp Datacard_cleaned.txt ./SingleHiggs_${procs}_node_${node}/HHWWgg_${procs}_node_${node}_${cat}_${year}.txt
  
#   python RunYields.py --cats $cat --inputWSDirMap $year=../Signal/Input/ --procs ${procs} --doHHWWgg ${doHHWWgg} --HHWWggLabel node_${node} --batch local --sigModelWSDir ./Models --bkgModelWSDir ./Models --doSystematics --ext ${procs}_node_${node}
#   python makeDatacard.py --years $year --prune True --ext ${procs}_node_${node} --pruneThreshold 0.00001 --doSystematics
#   python cleanDatacard.py --datacard Datacard.txt --factor 2 --removeDoubleSided
#   cp Datacard_cleaned.txt ./SingleHiggs_${procs}_node_${node}/HHWWgg_${procs}_node_${node}_${cat}_${year}_no_singleH.txt
# #
#   cd ./SingleHiggs_${procs}_node_${node}
#   echo "Combine results without singleH:"
#   combine HHWWgg_${procs}_node_${node}_${cat}_${year}_no_singleH.txt  -m 125 -M AsymptoticLimits --run=blind  --setParameterRanges  MH=120,130
#   echo "Combine results singleH:"
#   sed -i "23c process  0 2 3 4 5 1" ./HHWWgg_${procs}_node_${node}_${cat}_${year}.txt
#   combine HHWWgg_${procs}_node_${node}_${cat}_${year}.txt  -m 125 -M AsymptoticLimits --run=blind  --setParameterRanges  MH=120,130



