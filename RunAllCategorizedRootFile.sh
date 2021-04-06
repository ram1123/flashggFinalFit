# @Author: Ram Krishna Sharma
# @Date:   2021-04-05 15:07:12
# @Last Modified by:   ramkrishna
# @Last Modified time: 2021-04-05 15:30:37


# FH: WW Without QCD

#
#   Data
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/   --opt Data --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithoutQCD.txt --f Data --syst 0
#
#   Signal
python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/   --opt Signal --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithoutQCD.txt --f GluGluToHHTo2G2Z --syst 0 --node GluGluToHHTo2G2Z_cHHH1
python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/   --opt Signal --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithoutQCD.txt --f GluGluToHHTo2G4Q --syst 0 --node GluGluToHHTo2G2W_cHHH1
#
#   Single Higgs
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithoutQCD.txt --f VHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithoutQCD.txt --f VBFHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithoutQCD.txt --f GluGluHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithoutQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithoutQCD.txt --f ttHJet --syst 0

# FH: WW With QCD

#
#   Data
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/   --opt Data --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithQCD.txt --f Data --syst 0
#
#   Signal
python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/   --opt Signal --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithQCD.txt --f GluGluToHHTo2G2Z --syst 0 --node GluGluToHHTo2G2Z_cHHH1
python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/   --opt Signal --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithQCD.txt --f GluGluToHHTo2G4Q --syst 0 --node GluGluToHHTo2G2W_cHHH1
#
#   Single Higgs
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithQCD.txt --f VHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithQCD.txt --f VBFHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithQCD.txt --f GluGluHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWgg_WithQCD.txt --f ttHJet --syst 0


# FH: WWZZ With QCD

#
#   Data
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/   --opt Data --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWZZgg_WithQCD.txt --f Data --syst 0
#
#   Signal
python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/   --opt Signal --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWZZgg_WithQCD.txt --f GluGluToHHTo2G2Z --syst 0 --node GluGluToHHTo2G2Z_cHHH1
python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/   --opt Signal --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWZZgg_WithQCD.txt --f GluGluToHHTo2G4Q --syst 0 --node GluGluToHHTo2G2W_cHHH1
#
#   Single Higgs
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWZZgg_WithQCD.txt --f VHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWZZgg_WithQCD.txt --f VBFHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWZZgg_WithQCD.txt --f GluGluHToGG --syst 0
# python CategorizeTrees.py --iD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/   --opt SingleHiggs --year 2017 --oD /eos/user/r/rasharma/post_doc_ihep/double-higgs/ntuples/January_2021_Production/DNN/samples_w_DNN/HHWWyyDNN_binary_April2_WWZZgg_WithQCD_BalanceYields/CategorizeRootFile/ --nBoundaries BinBoundaries_April2_WWZZgg_WithQCD.txt --f ttHJet --syst 0
#
