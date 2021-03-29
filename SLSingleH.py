# The purpose of this module is to produce single higgs signal model fits 

import os 

os.system("`scramv1 runtime -sh`")
os.system("source ./setup.sh")

WorkingDirectory = "/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/"
procs = ['ggh', 'vbf', 'wzh', 'tth'] 
fileNames = [
             'SingleHiggs_GluGluHToGG_2017_all_CategorizedTrees', 
             'SingleHiggs_VBFHToGG_2017_all_CategorizedTrees', 
             'SingleHiggs_VHToGG_2017_all_CategorizedTrees',
             'SingleHiggs_ttHJetToGG_2017_all_CategorizedTrees'
             ]
years = ["2016"]

website="/eos/user/a/atishelm/www/HHWWgg/DNN/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/fggfinalfit/"
doSelections = 0
Selections = '(1.)' # Selections you want to applied.

for year in years:
    print"year:",year 
    for proc_i, proc in enumerate(procs):
        print"proc:",proc
        Name = fileNames[proc_i]
        outDirec = "%s/%s/%s/"%(website, year, proc)
        os.system("mkdir -p %s"%(outDirec))
        os.system("cp %s/../index.php %s"%(outDirec, outDirec))
        ext = "SL"
        cats = ["HHWWggTag_SLDNN_%s"%(i) for i in range(0,4)] # output cat name, it will be used in subsequence step
        InputTreeCats = ["HHWWggTag_SL_%s"%(i) for i in range(0,4)] #input cat name in the tree   
        mass = "125"     
        TreePath = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/%s/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/Single_H/"%(year)
        InputWorkspace = "/afs/cern.ch/work/a/atishelm/private/fggFinalFit_ForLimits/CMSSW_10_2_13/src/flashggFinalFit/Workspaces/"

        ############################################
        #  Tree selectors#
        #
        ############################################
        os.chdir("%s/Reweight"%(WorkingDirectory))
        print"On:",Name,",",proc

    # cd ${WorkingDirectory}/Reweight
    # echo $Name $procs
    cp SingleHiggsSelections.C SingleHiggsSelections_Run.C
    sed -i "s#NEW_Cat_NAME#${cat}#g" SingleHiggsSelections_Run.C 
    sed -i "s#NAME#${Name}#g" SingleHiggsSelections_Run.C 
    sed -i "s#CAT#${InputTreeCats}#g" SingleHiggsSelections_Run.C
    sed -i "s#PROCS#${procs}#g" SingleHiggsSelections_Run.C
    sed -i "s#YEAR#${year}#g" SingleHiggsSelections_Run.C
    sed -i "s#2017#${year}#g" SingleHiggsSelections_Run.C
    sed -i "s#INPUTPATH#${TreePath}#g" SingleHiggsSelections_Run.C
  if [ "$ext" = "SL" ]
  then
    sed -i "s#tagsDumper/trees/##g" SingleHiggsSelections_Run.C
  fi
    if [ $doSelections -eq "1" ]
    then
      echo "Selection start"
      sed -i "s#SELECTIONS#${Selections}#g" SingleHiggsSelections_Run.C
    else
      echo "Do not apply any selections ,just copytree "
      sed -i "s#SELECTIONS##g" SingleHiggsSelections_Run.C # No Selection 
    fi
  if [ $year -eq "2018" ]
  then
  sed -i "s#metUncUncertainty\"#metUncUncertainty\",\"JetHEM\"#g" SingleHiggsSelections_Run.C
  fi
    root -b -q SingleHiggsSelections_Run.C
    mv ${Name}_${year}.root  ../Trees2WS/
    cd ${WorkingDirectory}/Trees2WS/
    # cd ../Trees2WS/

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
cp HHWWgg_config_noprefire.py HHWWgg_config_run.py
else
cp HHWWgg_config.py HHWWgg_config_run.py
fi
sed -i "s#2017#${year}#g" HHWWgg_config_run.py
sed -i "s#auto#${cat}#g" HHWWgg_config_run.py
rm -rf ws*
python trees2ws.py --inputConfig HHWWgg_config_run.py --inputTreeFile ./${Name}_${year}.root --inputMass ${mass} --productionMode ${procs}  --year ${year} --doSystematics
rm HHWWgg_config_run.py
for catName in ${catNames[@]}
do
cp ws_${procs}/${Name}_${year}_${procs}.root $InputWorkspace/Signal/Input/${year}/Shifted_M125_${procs}_${catName}.root
cp ws_${procs}/${Name}_${year}_${procs}.root $InputWorkspace/Signal/Input/${year}/output_M125_${procs}_${catName}.root
done
rm ${Name}_${year}.root


#######################################
# Run ftest
######################################
echo "Run FTest"
# # # cd ../Signal/
cd ${WorkingDirectory}/Signal/

cp HHWWgg_single_higgs.py HHWWgg_config_Run.py
sed -i "s#NODE#node_${node}#g" HHWWgg_config_Run.py
sed -i "s#YEAR#${year}#g" HHWWgg_config_Run.py
sed -i "s#PROCS#${procs}#g" HHWWgg_config_Run.py
sed -i "s#HHWWggTest#${ext}#g" HHWWgg_config_Run.py
sed -i "s#CAT#${cat}#g" HHWWgg_config_Run.py
sed -i "s#INPUTDIR#${InputWorkspace}/Signal/Input/${year}/#g" HHWWgg_config_Run.py
python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode fTest --modeOpts "doPlots"

#######################################
# Run photon sys
######################################
python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode calcPhotonSyst

#######################################
#Run signal Fit
#######################################
python RunSignalScripts.py --inputConfig HHWWgg_config_Run.py --mode signalFit --groupSignalFitJobsByCat
for catName in ${catNames[@]}
do
  echo "catName: ${catName}"
  mkdir outdir_${ext}_${procs}_${year}_single_Higgs/
  cp ${WorkingDirectory}/Signal/outdir_${ext}_${year}_single_Higgs/signalFit/output/CMS-HGG_sigfit_${ext}_${year}_single_Higgs_${procs}_${year}_${catName}.root outdir_${ext}_${procs}_${year}_single_Higgs/CMS-HGG_sigfit_${ext}_${procs}_${year}_single_Higgs_${catName}.root
  echo "COMMAND:"
  echo "python RunPlotter.py --procs all --years $year --cats $catName --ext ${ext}_${procs}_${year}_single_Higgs --HHWWggLabel ${ext}_${procs}"
  python RunPlotter.py --procs all --years $year --cats $catName --ext ${ext}_${procs}_${year}_single_Higgs --HHWWggLabel ${ext}_${procs}
  echo "COPYING PLOTS:"
  echo "cp ${WorkingDirectory}/Signal/outdir_SL_${procs}_${year}_single_Higgs/Plots/*.png ${website}"
  echo "cp ${WorkingDirectory}/Signal/outdir_SL_${procs}_${year}_single_Higgs/Plots/*.pdf ${website}"
  cp ${WorkingDirectory}/Signal/outdir_SL_${procs}_${year}_single_Higgs/Plots/*.png ${website}
  cp ${WorkingDirectory}/Signal/outdir_SL_${procs}_${year}_single_Higgs/Plots/*.pdf ${website}
done



rm HHWWgg_config_Run.py


########################################
#           DATACARD                   #
#                                      #
########################################
echo "Start generate datacard(no systeamtics)"
# cd ../Datacard
cd ${WorkingDirectory}/Datacard/
if [ ! -d "./SingleHiggs_${ext}_${year}" ]; then
  mkdir -p ./SingleHiggs_${ext}_${year}/
fi
rm Datacard*.txt
rm -rf yields_test/
#copy signal modl
for catName in ${catNames[@]}
do
cp ${WorkingDirectory}/Signal/outdir_${ext}_${year}_single_Higgs/signalFit/output/CMS-HGG_sigfit_${ext}_${year}_single_Higgs_${procs}_${year}_${catName}.root ./SingleHiggs_${ext}_${year}/CMS-HGG_sigfit_packaged_${procs}_${catName}_${year}.root 
done
cd ${WorkingDirectory}
done
done

