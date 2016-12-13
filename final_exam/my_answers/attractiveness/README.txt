my_answers/attractiveness contains the following files:

- Attractiveness_(a)(b) (R script for (a)(b))
- Attractiveness_(c)(d) (R script for (c)(d))
- attractiveness_train.csv (training data)
- attractiveness_test.csv (test data)
- attractiveness_predictions.csv (predictions for the test data using L2-regularized logistic regression).
- README.txt

By dealing with missing values, mean-substitution may be fine in some cases, 
however such simple approaches usually introduce bias into the data, for instance, 
applying mean substitution leaves the mean unchanged (which is desirable) 
but decreases variance, which may be undesirable.

The mice package in R, helps imputing missing values with plausible data values. 
These plausible values are drawn from a distribution specifically designed for each
missing datapoint.