import pandas as pd

def MAE_weighted(model_pred, test_data, binary_class = 'Yes'):
    
    """The function return Mean Absolute error weighted by the 
    number of claims.
    
    Parameters
    ----------
    model_pred : model prediction
    test data : dataset with the test data
    binary_class : default Yes for binary calssification
    
    Returns
    -------
    Mean Absolute Error weighted 
    
    """

    test_data['predicted_label'] = model_pred

    #list of unique pantents
    publn_nr_list = test_data['publn_nr'].unique()

    #store the sume of the difference btewen the true labels and predicted labels
    sum_abs_pred_true = 0

    for pat in publn_nr_list:
        pat_db = test_data[test_data['publn_nr'] == pat]
        
        
        #for multiclass set to No
        if binary_class != 'Yes':

            #merge use claim - label 2 - to process - label 1
            pat_db['label'] = pat_db.label.replace(to_replace=[2], value=[1])
            pat_db['predicted_label'] = pat_db.predicted_label.replace(to_replace=[2], value=[1])

        #creates data frame with two rows with total num of claims 0 and 1s in the other.
        true_labels = pat_db.groupby(by='label').count().reset_index()
        pred_labels = pat_db.groupby(by='predicted_label').count().reset_index()

        #keeps only two columns and two rows of the labels and publication numbers
        true_labels = true_labels[['label' , 'publn_nr']]
        pred_labels = pred_labels[['predicted_label' , 'publn_nr']]
        
        true_labels.rename(columns = {'publn_nr':'nr_claims_x_type'}, inplace = True)
        pred_labels.rename(columns = {'publn_nr':'nr_claims_x_type'}, inplace = True)
        
        
        #for true labels, it calculate the percentage of a patent being process
        num_claims_true_labels = 0
        process_true = 0
        percentage_process_true_label = 0

        for i in range(true_labels.shape[0]):
            
            #store the total number of claims in a patent
            num_claims_true_labels += true_labels['nr_claims_x_type'].loc[i]
            
            #only if the claim is labelled 0 
            if i == 0:
                
                #store the number of claims labelled 0 - process
                process_true = true_labels['nr_claims_x_type'].loc[i]    

        #calculates the percentage of patent that is process - true labels
        percentage_process_true_label = process_true / num_claims_true_labels

        #for predicted labels it calculate the percentage of a patent being process
        num_claims_pred_labels = 0
        process_pred = 0
        percentage_process_pred_label = 0

        for j in range(pred_labels.shape[0]):
            
            num_claims_pred_labels += pred_labels['nr_claims_x_type'].loc[j]
            
            #only if the claim is labelled 0 
            if j == 0:
                
                #store the number of claims labelled 0 - process
                process_pred = pred_labels['nr_claims_x_type'].loc[j]
        
        #calculates the percentage of patent that is process - pred labels
        percentage_process_pred_label = process_pred / num_claims_pred_labels   

        
        sum_abs_pred_true += abs((percentage_process_pred_label - percentage_process_true_label)/num_claims_pred_labels)

    WMAE = sum_abs_pred_true/ len(publn_nr_list)


    return 'MAE-weighted is {}'.format(WMAE)


