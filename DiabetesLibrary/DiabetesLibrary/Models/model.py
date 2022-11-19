# Split the data between train and test. (you can use train_test_split from sklearn or any otherway)
def split(df):
    from sklearn.model_selection import train_test_split
    y = df.loc[:, ['diabetes_mellitus']]
    X = df.loc[:, df.columns != 'diabetes_mellitus']
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = split(df)


def train_model(X, y):
    from sklearn.linear_model import LogisticRegression
    X= X.loc[:,['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']]
    regressor = LogisticRegression()
    regressor.fit(X, y)
    return regressor
regressor = train_model(X_train,y_train)

#Predict the targets for both the train and test sets and add the prediction as a new column (use
#predict_proba from the model to get the predicted probabilities) name the new column something like predictions.
def predict(X,y,regressor):
    X = X.loc[:,['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure', 'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']]
    y_pred = regressor.predict(X)
    y_pred_proba = regressor.predict_proba(X)
    results = pd.DataFrame({'Actual': y['diabetes_mellitus'], 'Predicted': y_pred, "Predicted_Proba_0": y_pred_proba[:,0],"Predicted_Proba_1": y_pred_proba[:,1]})
    return results
results_train = predict(X_train, y_train, regressor)
results_test = predict(X_test, y_test, regressor)