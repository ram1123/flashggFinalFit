##################################################################################################################################
# Abraham Tishelman-Charny                                                                                                       #
# 22 March 2021                                                                                                                  #
#                                                                                                                                #
# The purpose of this module is to run all tree categorization steps for a given DNN training. On data, signal and single higgs. # 
##################################################################################################################################

##-- All Trainings 
##-- Binary 
# HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM
# HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM_withKinWeight_weightSel

##-- MultiClassifier 
# HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields
# HHWWyyDNN_WithHggFactor2-200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields
# HHWWyyDNN_MultiClass_EvenSingleH_2Hgg_withKinWeight_HggClassScale_4_BkgClassScale_1_BalanceYields.txt

import os 
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument("--TrainingLabel", type = str, default = "", help = "Unique label of DNN Training")
parser.add_argument("--inDir", type = str, default = "", help = "Input directory with ntuples to categorize")
parser.add_argument("--var", type = str, default = "", help = "Variable to categorize on")
parser.add_argument("--year", type = str, default = "", help = "year")
parser.add_argument("--local", type = str, default = "", help = "Local directory")
args = parser.parse_args()

TrainingLabel = args.TrainingLabel 
inDir = args.inDir 
var = args.var 
year = args.year 
LOCAL = args.local

##-- Binary 
# TrainingLabel = "HHWWyyDNN_binary_noHgg_noNegWeights_BalanceYields_allBkgs_LOSignals_noPtOverM" ##-- String for a given DNN training - used for paths and labels 
# inDir = "/eos/user/b/bmarzocc/HHWWgg/January_2021_Production/%s/"%(TrainingLabel)       
# var = "evalDNN"

##-- Multiclass 
# TrainingLabel = "HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields" ##-- String for a given DNN training - used for paths and labels 
# inDir = "/eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/%s/"%(TrainingLabel)   
# var = "evalDNN_HH"

Single_Higgs_Procs_2016 = ["GluGluHToGG_M125_2016", "VBFHToGG_M125_2016", "VHToGG_M125_2016", "ttHJetToGG_M125_2016"]
Single_Higgs_Procs_2017 = ["GluGluHToGG_2017", "VBFHToGG_2017", "VHToGG_2017", "ttHJetToGG_2017"]
Single_Higgs_Procs_2018 = ["GluGluHToGG_M125_2018", "VBFHToGG_M125_2018", "VHToGG_M125_2018", "ttHJetToGG_2018"]

doSys = 1 ##-- Do systematics

if(doSys): syst = "1"
else: syst = "0"

# python CategorizeTrees.py --iD /eos/user/a/atishelm/ntuples/HHWWgg_DNN/MultiClassifier/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ --opt SingleHiggs --year 2016 --oD /eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/2016/HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields/ --nBoundaries HHWWyyDNN_200Epochs-3ClassMulticlass_EvenSingleH_2Hgg_withKinWeightCut10_BalanceYields.txt --f GluGluHToGG_M125_2016 --part all
# years = ["2016", "2017", "2018"]
# years = ["2017", "2018"]
# years = ["2016"]

##-- Data 
# for year in years:

print "On Data Year %s"%(year)
# Make output directory if it doesn't already exist 
outDir = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/%s/%s/"%(year, TrainingLabel)
direcExists = os.path.exists(outDir)
if(not direcExists):
    print "Creating directory %s"%(outDir)
    os.system("mkdir -p %s"%(outDir))
CatTxtFile = "%s/%s.txt"%(LOCAL, TrainingLabel)
COMMAND = "python %s/CategorizeTrees.py --iD %s --opt Data --year %s --oD %s --nBoundaries %s --f ata_%s --v %s "%(LOCAL, inDir, year, outDir, CatTxtFile, year, var)
print "Executing command: ",COMMAND
os.system(COMMAND)

##-- Signal 
# for year in years:

print "On Signal Year %s"%(year)
# Make output directory if it doesn't already exist 
outDir = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/%s/%s/"%(year, TrainingLabel)
direcExists = os.path.exists(outDir)
if(not direcExists):
    print "Creating directory %s"%(outDir)
    os.system("mkdir -p %s"%(outDir))
CatTxtFile = "%s/%s.txt"%(LOCAL, TrainingLabel)
COMMAND = "python %s/CategorizeTrees.py --iD %s --opt Signal --year %s --oD %s --nBoundaries %s --f cHHH1_%s --node cHHH1 --part all --v %s --syst %s"%(LOCAL, inDir, year, outDir, CatTxtFile, year, var, syst)
print "Executing command: ",COMMAND
os.system(COMMAND)    

##-- Single Higgs 
# for year in years:

print "On Single Higgs Year %s"%(year)
# Make output directory if it doesn't already exist 
outDir = "/eos/user/a/atishelm/ntuples/HHWWgg_flashgg/January_2021_Production/%s/%s/Single_H/"%(year, TrainingLabel)    
direcExists = os.path.exists(outDir)
if(not direcExists):
    print "Creating directory %s"%(outDir)
    os.system("mkdir -p %s"%(outDir))  

##-- For Each single higgs
exec("Single_Higgs_Labels = Single_Higgs_Procs_%s"%(year))
for SingleHiggsLabel in Single_Higgs_Labels:
    CatTxtFile = "%s/%s.txt"%(LOCAL, TrainingLabel)
    COMMAND = "python %s/CategorizeTrees.py --iD %s --opt SingleHiggs --year %s --oD %s --nBoundaries %s --f %s --part all --v %s --syst %s "%(LOCAL, inDir, year, outDir, CatTxtFile, SingleHiggsLabel, var, syst)
    print "Executing command: ",COMMAND
    os.system(COMMAND)          