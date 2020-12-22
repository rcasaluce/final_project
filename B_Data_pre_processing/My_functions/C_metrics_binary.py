from sklearn import metrics
import pandas as pd

def calc_binary_class_metrics(targets, model, name_model, data_type):


    """The function return the evaluation metrics for a binary
    classification.
    
    Parameters
    ----------
    targets : target variable
    model : model fit and trained that needs to be evaluated
    name_model : string name of the learning algorithm
    data_type : string name of the type of data used to eveluate the model - test or validation
    
    Returns
    -------
    a dataset with all the metrics stored in one row 
    
    """
    # Metrics
    precision = metrics.precision_score(targets, model)
    recall = metrics.recall_score(targets, model)
    f1_score = metrics.f1_score(targets, model)
    balanced_accuracy = metrics.balanced_accuracy_score(targets, model)
    accuracy = metrics.accuracy_score(targets, model)

    #to calculate AUC for multiclass
    auc = metrics.roc_auc_score(targets, model)

    #calculate specificity
    m_c = metrics.confusion_matrix(targets, model)
    tn = m_c[0, 0]
    tp = m_c[1, 1]
    fn = m_c[1, 0]
    fp =m_c[0, 1]
    #https://scikit-learn.org/stable/modules/model_evaluation.html
    specificity = tn / (tn + fp)

    #creates the dictionar to be saved in the results_score data frame
    scores = {
         'Model': [name_model],
        'Data' : [data_type],
         'Precision': [precision],
         'Recall': [recall],
        'Specificity' : [specificity],
        'F1-score' : [f1_score],
        'Accuracy': [accuracy],
        'Bal Accuracy' : [balanced_accuracy],
        'AUC' : [auc]
    }

    scores = pd.DataFrame(scores)
    
    return scores
