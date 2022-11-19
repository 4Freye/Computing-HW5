# Read_csv()

Return the dataframe 'sample_diabetes_mellitus_data - sample_diabetes_mellitus_data.csv'

# remove_nan(df)

Remove those rows that contain NaN values in the columns: age, gender, ethnicity
The input is the dataframe from sample_diabetes, and return same dataframe without Nans

# fill_nan(df)

Fill NaN with the mean value of the column in the columns: height, weight.
The input is the dataframe from sample_diabetes, and return same dataframe with mean value replacing the Nans.

# binary_gender(df)

Creates a binary variable for gender M/F.
The input is the dataframe from sample_diabetes and return same dataframe with one binary column "female" replacing the "Gender" column that is drop.

# generate_dummies(df)

Generate dummies for ethnicity column (One hot encoding)
The input is the dataframe from sample_diabetes and return same dataframe with dummy varaibles for each type of ethnicity.

# split(df)

Split the data between train and test. It use train_test_split from sklearn.
The input is the dataframe from sample_diabetes and the output are four dataframes: X_train, X_test, y_train, y_test

# train_model(X, y)

Train a model (LogisticRegression from sklearn) in the train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’,
‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target the column: ‘diabetes_mellitus’
The input is dataframe X and y to train and it return the regressor object.

# predict(X,y,regressor)

Predict the targets and predict the probability of each target.
The input is the dataframe X and y and the regressor. It return a dataframe with a column "Actual" with the real value, a "Predicted" column with the predicted value from the model, 
a "Predicted_Proba_0" column with the probability of being 0 and "Predicted_Proba_1" column with the probability of being 1.

# roc_auc_metric(result)

Compute the train and test roc_auc metric using roc_auc_score from sklearn.
The input is the "result" dataframe from the predict() function and return the roc_auc_score comparing the "Actual" with "Predicted_Proba_1". 
It can be used from the train or test results.