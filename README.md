
## Automated Patent Classification by Type of Innovation for Clean Energy Storage Technologies

<br/>
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/de/thumb/7/7f/Birkbeck_College_Logo.svg/640px-Birkbeck_College_Logo.svg.png" height="80" width="280">
</p>

To complete the project, I followed the steps below - the full detailed process is described in the [Report](https://github.com/rcasaluce/final_project/blob/master/Y_Report/Report.pdf):

1. [A_Data_Collection](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection)
2. [B_Data_Pre_Processing](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing)
3. [C_Feature_Extraction](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction)
4. [D_Spot-Check](https://github.com/rcasaluce/final_project/tree/master/D_Spot-Check)
5. [E_Models](https://github.com/rcasaluce/final_project/tree/master/E_Models)
6. [F_Extra_Experiments_Abstracts](https://github.com/rcasaluce/final_project/tree/master/F_Extra_Experiments_Abstracts)
7. [Labelled_Data](https://github.com/rcasaluce/final_project/tree/master/Labelled_data)
8. [Unlabelled_Data](https://github.com/rcasaluce/final_project/tree/master/Unlabelled_data)
9. [Z_Best_Models_Saved](https://github.com/rcasaluce/final_project/tree/master/Z_Best_models_saved)

-------------------------
#### I built a web app using Django after the submission of the final report, and the web application can be found here: [https://patents-classification.herokuapp.com/](https://patents-classification.herokuapp.com/)

#### GitHub repository [here](https://github.com/rcasaluce/Django_app-patents_classification)

-------------------------
### [A_Data_Collection](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection)

This folder includes all the scripts to collect and parse the data. 

It is divided into two main folders, one for each patent office, [USPTO](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/USPTO) and [EPO](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/EPO).

[EPO](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/EPO):

[Sample_Bulk_Full_Text_EPO](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/EPO/Sample_Bulk_full_text_EPO) folder: this is where the 36 text files downloaded from Google Cloud are stored. I left inside just a sample of them (link to Google Cloud bucket to download full-text EPO patents: https://console.cloud.google.com/storage/browser/epo-public/).

[PATSTAT_EPO_Patents](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/EPO/PATSTAT_EPO_patents) folder: in this folder is stored the PATSTAT dataset with information about the patents that I collected from the EPO office (link to download the whole PATSTAT dataset: https://www.epo.org/searching-for-patents/business/patstat.html).

[EPO_Parser.ipynb](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/EPO/EPO_parser.ipynb) script: with it, I parsed the patents from each of the 36 text files and saved an xlsx file for each of them in the folder [Data_Parsed](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/EPO/Data_parsed).

[USPTO](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/USPTO):

[PATSTAT_USPTO_Patents](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/USPTO/PATSTAT_USPTO_patents) folder: in this folder is stored the PATSTAT dataset with information about the patents that I collected from the USPTO office.

[Webscraper_USPTO.ipynb](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/USPTO/Webscraper_USPTO.ipynb) script: with this script, the USPTO patents were web-scraped and parsed. The xlsx files with the patents parsed were saved in the folder Data_Collected. 

-------------------------

### [B_Data_Pre_Processing](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing)

This folder includes the scripts - [pre_process_claims.ipynb](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/pre_process_claims.ipynb) and [pre_process_abstracts.ipynb](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/pre_process_abstracts.ipynb) that I used to pre-process the labelled dataset, which I then saved as pickle files in the folder [Pickle_Files](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/Pickle_Files) to use them during the other phases of the project.

There is also another folder where I saved my most used functions, called [My_Functions](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/My_functions):

[A_Merge_Datasets.py](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/My_functions/A_merge_datasets.py): script that merges the datasets for the four energy technologies, either for the labelled or unlabelled datasets.
[B_Pre_Processing_Data.py](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/My_functions/B_pre_processing_data.py): script that pre-processes the text file.
[C_Metrics_Binary.py](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/My_functions/C_metrics_binary.py) and [D_Metrics_Multiclass.py](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/My_functions/D_metrics_multiclass.py): scripts to create a dataset of the metrics after evaluating the models.
[E_MAEweighted_Function.py](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/My_functions/E_MAEweighted_funct.py): script to calculate the Mean Absolute Error weighted.

-------------------------

### [C_Feature_Extraction](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction)

This folder includes the trained Word2Vec models (I had to delete those files from the repository because each of those models is around 5GB, and I also had to delete the file in the folder [Data_for_w2v](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction/Data_for_w2v) where I saved the text files prior to training the word embedding models because they were too large).

[Word2Vec](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction/Word2Vec) folder: This folder includes the scripts that I used to collect and parse the USPTO and EPO patents.

[Download_USPTO_Pat.ipynb](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction/Word2Vec/download_USPTO_pat.ipynb): This script downloads the zip files, extracts their XML files, parses each one of them, and saves them one by one as xlsx files – in the folder [USPTO](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v/USPTO) inside the folder [Data_for_w2v](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v) - with abstracts and claims from the USPTO office.

[Tokenizer_USPTO_Text_File.ipynb](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction/Word2Vec/tokenizer_USPTO_text_file.ipynb): This script takes the files saved in [USPTO](https://github.com/rcasaluce/code_final_project/tree/master/C_Feature_extraction/Data_for_w2v/USPTO), parses and pre-processes them, and creates for each of them a text file where in each line is saved either an abstract or a claim.

[Tokenizer_EPO_Text_File.ipynb](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction/Word2Vec/tokenizer_EPO_text_file.ipynb): This script parses and pre-processes again the 36 text files saved in [Sample_Bulk_Full_Text_EPO](https://github.com/rcasaluce/final_project/tree/master/A_Data_Collection/EPO/Sample_Bulk_full_text_EPO) folder and saves them in [Data_for_w2v](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction/Data_for_w2v)

 as text files in the same way as I did for the USPTO claims and abstracts.

[Train_w2v_Gensim.ipynb](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction/Word2Vec/Train_w2v_gensim.ipynb): This script is just an example of how I used the gensim library to train a word embedding model – Skip-gram with 300 dimensions, 5 for negative sampling, and 5 as window size. 

-------------------------

### [D_Spot-Check](https://github.com/rcasaluce/final_project/tree/master/D_Spot-Check)

This is the folder where I saved the scripts of my test harness to spot-check the best two models for each of the three classification models. 

Two folders are included inside it, one for the abstract and the other for the claims.

[Abstracts](https://github.com/rcasaluce/final_project/tree/master/D_Spot-Check/Abstracts) folder:

[Spot_Check_Binary_Classification_Abstracts.ipynb](https://github.com/rcasaluce/final_project/tree/master/D_Spot-Check/Abstracts/Spot_check_Binary_Classification_abstracts.ipynb): This script is to run the test harness for the binary classification model of the abstracts. It loads the pickle files saved in the folder [Pickle_Files](https://github.com/rcasaluce/final_project/tree/master/B_Data_pre_processing/Pickle_Files) and the Word2Vec model saved in the folder [C_Feature_Extraction](https://github.com/rcasaluce/final_project/tree/master/C_Feature_extraction).

[Claims](https://github.com/rcasaluce/final_project/tree/master/D_Spot-Check/Claims) folder:

[Spot_Check_Binary_Classification.ipynb](https://github.com/rcasaluce/final_project/tree/master/D_Spot-Check/Claims/Spot_check_Binary_Classification.ipynb) and [Spot_Check_Multiclass_Classification.ipynb](https://github.com/rcasaluce/final_project/tree/master/D_Spot-Check/Claims/Spot_check_Mulitclass_Classification.ipynb): These two scripts are for the test harness for both binary and multiclass classification models of claims. 

-------------------------

### [E_Models](https://github.com/rcasaluce/final_project/tree/master/E_Models)

Two folders are included inside it, one for the abstract and the other for the claims.

[Claims](https://github.com/rcasaluce/final_project/tree/master/E_Models/Claims) folder:

[Best_Two_Models_Binary_Classification_Claims.ipynb](https://github.com/rcasaluce/final_project/tree/master/E_Models/Claims/Best_two_models_Binary_Classification_claims.ipynb) and [Best_Two_Models_Multiclass_Classification_Claims.ipynb](https://github.com/rcasaluce/final_project/tree/master/E_Models/Claims/Best_two_models_Multiclass_Classification_claims.ipynb): scripts to run the best two models selected after the previous step – Spot-check.

[Abstracts](https://github.com/rcasaluce/final_project/tree/master/E_Models/Abstracts) folder:

[Best_Two_Models_Binary_Classification_Abstracts.ipynb](https://github.com/rcasaluce/final_project/tree/master/E_Models/Abstracts/Best_two_models_Binary_Classification_abstracts.ipynb): script to run the best model for the binary classification of abstracts.

[Pickle_Files](https://github.com/rcasaluce/final_project/tree/master/E_Models/Abstracts/Pickle_Files) folder: I saved the pickle files from the script  [Best_Two_Models_Binary_Classification_Abstracts.ipynb](https://github.com/rcasaluce/final_project/tree/master/E_Models/Abstracts/Best_two_models_Binary_Classification_abstracts.ipynb), such as the features and the targets data for both training and testing data, the best binary model trained and the TF-IDF fit/transformed for the best model. All these files are used for the experiments to increase the performance of the binary model for the abstracts - [F_Extra_Experiments_Abstracts](https://github.com/rcasaluce/final_project/tree/master/F_Extra_Experiments_Abstracts).

-------------------------

### [F_Extra_Experiments_Abstracts](https://github.com/rcasaluce/final_project/tree/master/F_Extra_Experiments_Abstracts)

This folder includes the three extra experiments for the abstracts.

[Data_Augmentation.ipynb](https://github.com/rcasaluce/final_project/tree/master/F_Extra_Experiments_Abstracts/Data_Augmentation.ipynb): This is the script that I used to create the text files to be augmented and after that I used them to run the binary classification models again with different algorithms and to choose the best one. The data augmented is saved in a folder called [Data_for_Augmentation](https://github.com/rcasaluce/final_project/tree/master/F_Extra_Experiments_Abstracts/Data_for_augmentation). 

[Pseudo_Labels_Abstracts.ipynb](https://github.com/rcasaluce/final_project/tree/master/F_Extra_Experiments_Abstracts/Pseudo_labels_Abstracts.ipynb): This script runs the pseudo labelling experiment that used the unlabelled data stored in the folder [Unlabelled_Data](https://github.com/rcasaluce/final_project/tree/master/Unlabelled_data) and with the predicted model saved in E_Models/Abstracts/Pickle_Files, it assigns labels to the unlabelled data. 

[Keyword_Search_Labeling_Abstracts.ipynb](https://github.com/rcasaluce/final_project/tree/master/F_Extra_Experiments_Abstracts/Keyword_search_labeling_Abstracts.ipynb): script that labels the unlabelled data using the keyword search method. 

-------------------------

The folders below are for the data manually labelled and for the data that I collected for the four energy technologies:
-------------------------
### [Labelled_Data](https://github.com/rcasaluce/final_project/tree/master/Labelled_data)
This is the part of the data collected that has been manually labelled.

### [Unlabelled_Data](https://github.com/rcasaluce/final_project/tree/master/Unlabelled_data)
This is the actual data collected from both patent offices for the four energy storage technologies.


