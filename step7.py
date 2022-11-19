#1 Load the data
from  DiabetesLibrary.DiabetesLibrary.Data import process
from  DiabetesLibrary.DiabetesLibrary.Models import model
from DiabetesLibrary.DiabetesLibrary.Models import evaluate



#2 

#a. Load the data.
data = process.read_data()


#c. Remove those rows that contain NaN values in the columns: age, gender, ethnicity.

data = process.remove_nan(data)


#d. Fill NaN with the mean value of the column in the columns: height, weight.

data = process.fill_nan(data)

#f. Create a binary variable for gender M/F.

data = process.binary_gender(data)

#e. Generate dummies for ethnicity column (One hot encoding).

data = process.generate_dummies(data)



#b. Split the data between train and test. (you can use train_test_split from sklearn or any other way)

X_train, X_test, y_train, y_test = model.split(data)

#g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the
#train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’,‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target thecolumn: ‘diabetes_mellitus’

regressortrain = model.train_model(X_train, y_train)


#h. Predict the targets for both the train and test sets and add the prediction as a new column (use predict_proba from the model to get the predicted probabilities) name the new column something like predictions.

resulttrain = model.predict(X_train, y_train, regressortrain)
resulttest = model.predict(X_test, y_test, regressortrain)


#i. Compute the train and test roc_auc metric using roc_auc_score from sklearn.

trainscore = evaluate.roc_auc_metric(resulttrain)
testscore = evaluate.roc_auc_metric(resulttest)

print(trainscore)
print(testscore)