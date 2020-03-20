def evaluation_metrics(list_of_models, X, y):
    table = [['Model Name','Accuracy','Sensitivity','Specificity', 'AUC ROC']]
    for name, model in list_of_models:
        y_pred = model.predict(X)
        y_proba = model.predict_proba(X)
        
        TN, FP, FN, TP = confusion_matrix(y, y_pred).ravel()
        accuracy = (TP + TN) / (TP + TN + FP + FN)
        sensitivity = TP / (TP + FN)
        specificity = TN / (TN + FP)
        
        false_positive_rate, true_positive_rate, thresholds = roc_curve(y, y_proba[:,1])
        auc_roc = auc(false_positive_rate, true_positive_rate)
        
        table.append([name, accuracy, sensitivity, specificity, auc_roc])
    return table