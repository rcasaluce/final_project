## Automated Patent Classification by type of Innovation for Clean Energy Storage Technologies

<br/>
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/de/thumb/7/7f/Birkbeck_College_Logo.svg/640px-Birkbeck_College_Logo.svg.png" height="80" width="280">
</p>

To complete the project, I follow the steps below - the full detailed process is described in the [Report](https://github.com/rcasaluce/code_final_project/blob/master/Y_Report/Report.pdf):

1. [A_Data_Collection](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection)
2. [B_Data_pre_processing](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing)
3. [C_Feature_extraction](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction)
4. [D_Spot-Check](https://github.com/rcasaluce/code_final_project/tree/master/D_Spot-Check)
5. [E_Models](https://github.com/rcasaluce/code_final_project/tree/master/E_Models)
6. [F_Extra_Experiments_Abstracts](https://github.com/rcasaluce/code_final_project/tree/master/F_Extra_Experiments_Abstracts)
7. [Labelled_data](https://github.com/rcasaluce/code_final_project/tree/master/Labelled_data)
8. [Unlabelled_data](https://github.com/rcasaluce/code_final_project/tree/master/Unlabelled_data)
9. [Z_Best_models_saved](https://github.com/rcasaluce/code_final_project/tree/master/Z_Best_models_saved)

-------------------------
#### I have built a web app using Django after the submission the final report and the web application can be found here [https://patents-classification.herokuapp.com/](https://patents-classification.herokuapp.com/)

#### Github repository [here](https://github.com/rcasaluce/Django_app-patents_classification)

-------------------------
### [A_Data_Collection](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection)


This folder includes all the scripts to collect and parse the data. 

It is divided in two main folders, a folder of each patent office, [USPTO](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/USPTO) and [EPO](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collectionn/EPO).


[EPO](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/EPO):

[Sample_Bulk_full_text_EPO](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/EPO/Sample_Bulk_full_text_EPO) folder: this is where thery are stored the 36 text files downloaded from Google Cloud – I left inside just a sample of them (link to Google Cloud bucket to download full-text EPO patents https://console.cloud.google.com/storage/browser/epo-public/).

[PATSTAT_EPO_patents](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/EPO/PATSTAT_EPO_patents) folder: in this folder is stored the PASTAT dataset with information of the patents that I collected from the EPO office (link to download the whole PATSTAT dataset https://www.epo.org/searching-for-patents/business/patstat.html).

[EPO_parser.ipynb](https://github.com/Birkbeck/msc-data-science-project-2019-20-files-rcasaluce/edit/master/A_Data_Collection/EPO/EPO_parser.ipynb) script: with it, I parsed the patents from each of the 36 text files and saved a xlsx file for each of them in the folder [Data_parsed](https://github.com/Birkbeck/msc-data-science-project-2019-20-files-rcasaluce/edit/master/A_Data_Collection/EPO/Data_parsed).

[EPO_parser.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/EPO/EPO_parser.ipynb) script: with it, the EPO patents were parsed from each of the 36 text files and saved a xlsx file for each of them in the folder [Data_parsed](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/EPO/Data_parsed).



[USPTO](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/USPTO):

[PATSTAT_USPTO_patents](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/USPTO/PATSTAT_USPTO_patents) folder: in this folder is stored PASTAT dataset with information of the patents that I collected from the USPTO office.

[Webscraper_USPTO.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/USPTO/Webscraper_USPTO.ipynb) script: with this script the USPTO patents were web scrapped and parsed. The xlsx files with the patents parsed were saved them in the folder Data collected. 

-------------------------

### [B_Data_pre_processing](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing)

This folder includes the scripts - [pre_process_claims.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/pre_process_claims.ipynb) and [pre_process_abstracts.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/pre_process_abstracts.ipynb) that I used to pre-process the labelled dataset which then I saved as pickle files in the folder [Pickle_Files](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/Pickle_Files) to used them during the other phases of the project.

There is also another folder where I saved my most used functions, called [My_functions](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/My_functions):

[A_merge_datasets.py](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/My_functions/A_merge_datasets.py): script that merges the datasets for the four energy technologies either for the labelled or unlabelled dasets.
[B_pre_processing_data.py](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/My_functions/B_pre_processing_data.py): script that pre-process the text file.
[C_metrics_binary.py](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/My_functions/C_metrics_binary.py) and [D_metrics_multiclass.py](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/My_functions/D_metrics_multiclass.py): scripts to create a dataset of the metrics after evaluating the models.
[E_MAEweighted_funct.py](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/My_functions/E_MAEweighted_funct.py): script to calculate the Mean Absolute Error weighted.

-------------------------

### [C_Feature_extraction](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction)

This folder includes the trained Word2Vec models (I had to delete those files from the repository because each of those models is around 5GB and also I had to delete the file in the folder [Data_for_w2v](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v) where I saved the text files prior to train the word embedding models because too large).

[Word2Vec](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Word2Vec) folder: This folder includes the scripts that I used to collect and parse the USPO and EPO patents.

[download_USPTO_pat.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Word2Vec/download_USPTO_pat.ipynb): This script downloads the zip files, extracts their XML files, parses each one of them and save them one by one as a xlsx files – in the folder [USPTO](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v/USPTO) inside the folder [Data_for_w2v](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v) - with abstracts and claims from the USPTO office.

[tokenizer_USPTO_text_file.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Word2Vec/tokenizer_USPTO_text_file.ipynb): This script takes the files saved in [USPTO](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v/USPTO), parses and pre-processes them, creates for each of them a text file where in each line is saved either an abstract or a claim.

[tokenizer_EPO_text_file.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Word2Vec/tokenizer_EPO_text_file.ipynb): This script parses and pre-processes again the 36 text files saved in [Sample_Bulk_full_text_EPO](https://github.com/rcasaluce/code_final_project/tree/master/A_Data_Collection/EPO/Sample_Bulk_full_text_EPO) folder and save in [Data_for_w2v](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v) as text files in the same way as I did for the USPTO claims and abstracts.

[Train_w2v_gensim.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Word2Vec/Train_w2v_gensim.ipynb): Thsi script is just an example of how I used gensim library to train a word embedding model – Skip-gram with 300 of max dimension, 5 for negative sampling, 5 as window size. 

-------------------------

### [D_Spot-Check](https://github.com/rcasaluce/code_final_project/tree/master/D_Spot-Check)

This is the folder where I saved the scripts of my test harness to spot-check the best two models for each of the three classification models. 

Two folders are included inside it, one for the abstract and the other for the claims.

[Abstracts](https://github.com/rcasaluce/code_final_project/tree/master/D_Spot-Check/Abstracts) folder:

[Spot_check_Binary_Classification_abstracts.ipynb]https://github.com/rcasaluce/code_final_project/tree/master/D_Spot-Check/Abstracts/Spot_check_Binary_Classification_abstracts.ipynb): This script is to run the test harness for the binary classification model of the abstracts. It loads the pickle files saved in the folder [Pickle_Files](https://github.com/rcasaluce/code_final_project/tree/master/B_Data_pre_processing/Pickle_Files) and the Word2Vec model saved in the folder [C_Feature_extraction](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction).

[Claims](https://github.com/rcasaluce/code_final_project/tree/master/D_Spot-Check/Claims) folder: folder:

[Spot_check_Binary_Classification.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/D_Spot-Check/Claims/Spot_check_Binary_Classification.ipynb) and [Spot_check_Mulitclass_Classification.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/D_Spot-Check/Claims/Spot_check_Mulitclass_Classification.ipynb): These two scripts are for the test harness for both binary and multiclass classification models of claims. 

-------------------------

### [E_Models](https://github.com/rcasaluce/code_final_project/tree/master/E_Models)

Two folders are included inside it, one for the abstract and the other for the claims.

[Claims](https://github.com/rcasaluce/code_final_project/tree/master/E_Models/Claims) folder:

[Best_two_models_Binary_Classification_claims.ipynb]https://github.com/rcasaluce/code_final_project/tree/master/E_Models/Claims/Best_two_models_Binary_Classification_claims.ipynb) and [Best_two_models_Multiclass_Classification_claims.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/E_Models/Claims/Best_two_models_Multiclass_Classification_claims.ipynb): scripts to run the best two models selected after the previous step – Spot-check.

[Abstracts](https://github.com/rcasaluce/code_final_project/tree/master/E_Models/Abstracts) folder:

[Best_two_models_Binary_Classification_abstracts.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/E_Models/Abstracts/Best_two_models_Binary_Classification_abstracts.ipynb): scripts to run the best model for the binary classification of abstracts.

[Pickle_Files](https://github.com/rcasaluce/code_final_project/tree/master/E_Models/Abstracts/Pickle_Files) folder: I saved the pickle files from the script  [Best_two_models_Binary_Classification_abstracts.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/E_Models/Abstracts/Best_two_models_Binary_Classification_abstracts.ipynb), such as the features and the targets data for both training and testing data, the best binary model trained and the TF-IDF fit/transformed for the best model. All these files are used for the experiments to increase the performance of the binary model for the abstracts - [F_Extra_Experiments_Abstracts](https://github.com/rcasaluce/code_final_project/tree/master/F_Extra_Experiments_Abstracts).

-------------------------

### [F_Extra_Experiments_Abstracts](https://github.com/rcasaluce/code_final_project/tree/master/F_Extra_Experiments_Abstracts)

This folder includes the three extra experiments for the abstracts.

[Data_Augmentation.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/F_Extra_Experiments_Abstracts/Data_Augmentation.ipynb): This is the script that I used tocreate the text files to be augmented and after that I used them to run again the binary classification models with different algorithms and to choose the best one. The data augmented is save in a folder called [Data_for_augmentation]https://github.com/rcasaluce/code_final_project/tree/master/F_Extra_Experiments_Abstracts/Data_for_augmentation). 

[Pseudo_labels_Abstracts.ipynb](https://github.com/rcasaluce/code_final_project/tree/master/F_Extra_Experiments_Abstracts/Pseudo_labels_Abstracts.ipynb): This script runs the pseudo labelling experiment that used the unlabelled data stored in the folder [Unlabelled_data](https://github.com/rcasaluce/code_final_project/tree/master/Unlabelled_data) and with the predicted model saved in E_Models/Abstracts/Pickle_Files, it assigns  to the unlabelled data. 

[Keyword_search_labeling_Abstracts.ipynb](hhttps://github.com/rcasaluce/code_final_project/tree/master/F_Extra_Experiments_Abstracts/Keyword_search_labeling_Abstracts.ipynb): script that labels the unlabelled data using keyword search method. 



-------------------------

The folders below are for the data manually labelled and for the data that I collected for the four energy technologies:
-------------------------
### [Labelled_data](https://github.com/rcasaluce/code_final_project/tree/master/Labelled_data)
This is the part of the data collected that has been manually labelled.

### [Unlabelled_data](https://github.com/rcasaluce/code_final_project/tree/master/Unlabelled_data)
This is the actual data collected from both patent offices for the four energy storage technologie.

-------------------------

### [Z_Best_models_saved](https://github.com/rcasaluce/code_final_project/tree/master/Z_Best_models_saved)
In this folder I saved the best models for the claims, binary and multiclass models and the best model for the abstract trained with the data labelled by suing the keyword search.
