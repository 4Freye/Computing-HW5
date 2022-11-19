#Compute the train and test roc_auc metric using roc_auc_score from sklearn
def roc_auc_metric(result):
    from sklearn.metrics import roc_auc_score
    return roc_auc_score(result['Actual'], result['Predicted_Proba_1'])
