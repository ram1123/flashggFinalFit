#!/bin/bash
#
#########################################################################################
# Abraham Tishelman-Charny                                                              #
# 11 March 2020                                                                         #
#                                                                                       #
# The purpose of this script is to run all fggfinalfit steps for the HHWWgg analysis    #
#                                                                                       #
# Example usage:                                                                        #
# . HHWWggFinalFitScript.sh backgroundftest                                             #
# . HHWWggFinalFitScript.sh signal                                                      #
#########################################################################################

step=$1
year=$2

cmsenv
#-- Background
if [ $step == "backgroundftest" ]; then
    cd Background
    python RunBackgroundScripts.py --inputConfig HHWWgg_Synch_Background_Config.py
    # python RunBackgroundScripts.py --inputConfig HHWWgg_SMqqqq${year}_Config.py
    # python RunBackgroundScripts.py --inputConfig HHWWgg_SM${year}_Config.py
    # python RunBackgroundScripts.py --inputConfig HHWWgg_v2-7_Config.py
    cd ..
fi

##-- Not yet configured
# if [ $step == "backgroundplots" ]; then
#     cd Background
#     python RunBackgroundScripts.py bkgPlotsOnly --inputConfig config_HHWWgg_v2-3_2017.py
#     # python RunBackgroundScripts.py bkgPlotsOnly --inputConfig config_HHWWgg_v2-3_2017_2Cats.py
#     cd ..
# fi

#-- Signal
if [ $step == "signal" ]; then
    cd Signal
    python RunSignalScripts.py --inputConfig HHWWgg_Synch_Signal_Config.py # signal models
    # python RunSignalScripts.py --inputConfig HHWWgg_SMqqqq${year}_Config.py # signal models
    # python RunSignalScripts.py --inputConfig HHWWgg_SM${year}_Config.py # signal models
    # python RunSignalScripts.py --inputConfig HHWWgg_v2-7_Config.py # signal models
    cd ..
fi

#-- Datacards
if [ $step == "datacard" ]; then
    python RunCombineScripts.py datacard --inputConfig HHWWgg_Synch_Combine_Config.py # Make datacard
    # python RunCombineScripts.py datacard --inputConfig HHWWgg_SMqqqq${year}_Config.py # Make datacard
    # python RunCombineScripts.py datacard --inputConfig HHWWgg_SM${year}_Config.py # Make datacard
    # python RunCombineScripts.py datacard --inputConfig HHWWgg_v2-7_Config.py # Make datacard
fi

#-- Combine
if [ $step == "combine" ]; then
    python RunCombineScripts.py combine --inputConfig HHWWgg_Synch_Combine_Config.py # Make datacard
    # python RunCombineScripts.py combine --inputConfig HHWWgg_SMqqqq${year}_Config.py
    # python RunCombineScripts.py combine --inputConfig HHWWgg_SM${year}_Config.py
    # python RunCombineScripts.py combine --inputConfig HHWWgg_SMRun2_Config.py
    # python RunCombineScripts.py combine --inputConfig HHWWgg_v2-7_Config.py
    # bash RenameCombineFiles.sh
fi

#-- Plots
if [ $step == "plot" ]; then
    tagLabel="2TotCatsbothcombined"
    # SecondTagLabel="2TotCatsbothcombined"
    campaignOne="HHWWgg_v2-6"
    FinalState="qqqq"
    YEAR="2016"
    CHANNEL="ww"
    website="/eos/user/r/rasharma/www/doubleHiggs/HHWWgg/fggfinalfit_FixName/2016_WW"
    # bash RenameCombineFiles.sh $website $CHANNEL $YEAR
    cd Plots/FinalResults/
    # campaignOne="HHWWgg_v2-3"
    # campaignTwo="HHWWgg_v2-6"
    # SecondTagLabel="2TotCatsCOMBINEDWithoutSyst"
    # tagLabel="2TotCatsTag0WithSyst"
    # SecondTagLabel="2TotCatsTag0WithoutSyst"
    # HHWWgg_v2-6_2017_X1000_2TotCatsCOMBINEDWithSyst_HHWWgg_qqlnu.root

    ## qqqq Radion
    # python plot_limits.py -a  --HHWWggCatLabel $tagLabel --website ${website}  --systematics  --campaignOne $campaignOne  --yboost 1 --ymin 0.1 --ymax 1 --unit fb --FinalState ${FinalState} --resultType HH  --ymin 1e1 --ymax 1e6 --campaign HHWWgg_dummy # ratio of all points
    # python plot_limits.py -a  --HHWWggCatLabel $tagLabel --website ${website}  --systematics  --campaignOne $campaignOne  --yboost 1 --ymin 0.1 --ymax 1 --unit fb --FinalState ${FinalState} --resultType WWgg  --ymin 0.1 --ymax 1e2 --campaign HHWWgg_dummy # ratio of all points

    ## qqqq Radion: Grid
    # python plot_limits.py --channel $CHANNEL -a -g --GridLabels $tagLabel  --resultType HH --unit fb --ymin 0.1 --ymax 1 --yboost 1 --FinalState ${FinalState}  --website ${website} --year $YEAR

    # qqqq EFT
    ## python plot_limits.py --EFT --HHWWggCatLabel $tagLabel --systematics --campaign $campaignOne --resultType WWgg --unit pb --ymin 0.001 --ymax 1e2 --yboost -0.32  --FinalState ${FinalState} --website ${website} # EFT
    if [[ $CHANNEL == "zz" ]]; then
        echo "Inside ZZ channel"
        python plot_limits.py --channel $CHANNEL --EFT --HHWWggCatLabel $tagLabel --systematics --campaign $campaignOne --resultType HH --unit pb --ymin 0.1 --ymax 1e5 --yboost -0.32  --FinalState ${FinalState} --year $YEAR --website ${website} # EFT
    fi
    if [[ $CHANNEL == "ww" ]]; then
        echo "Inside WW channel"
        python plot_limits.py --channel $CHANNEL --EFT --HHWWggCatLabel $tagLabel --systematics --campaign $campaignOne --resultType HH --unit pb --ymin 0.001 --ymax 1e4 --yboost -0.32  --FinalState ${FinalState} --year $YEAR --website ${website} # EFT
    fi
    ## python plot_limits.py --EFT --HHWWggCatLabel $tagLabel --systematics --campaign $campaignOne --resultType HH --unit pb --ymin 10.0 --ymax 1e4 --yboost -0.32  --FinalState ${FinalState} --website ${website} # EFT

    cd ../../
fi
