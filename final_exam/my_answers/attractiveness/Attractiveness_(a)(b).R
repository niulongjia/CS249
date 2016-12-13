not.installed <- function(pkg) !is.element(pkg, installed.packages()[,1])
if (not.installed("e1071")) install.packages("e1071", repos = "http://cran.r-project.org")
if (not.installed("zoo")) install.packages("zoo", repos = "http://cran.r-project.org")
if (not.installed("mice")) install.packages("mice", repos = "http://cran.r-project.org")

library(zoo)
library(e1071)
library(mice)

training.set = read.csv( file("attractiveness_train.csv"), header = TRUE )
test.set = read.csv( file("attractiveness_test.csv"), header = TRUE )

# training.set = na.aggregate(training.set) # fill in NA with mean value of the column
# test.set = na.aggregate(test.set) # fill in NA with mean value of the column
training.set=mice(training.set)
training.set=complete(training.set)
test.set=mice(test.set)
test.set=complete(test.set)
#training.set[,"male"] = as.numeric(training.set[,"male"])

svmModel = svm(   factor(male) ~ . ,data=training.set,kernal = "radial" )
svmPred = predict( svmModel, test.set  )
#svmPred = round(predict( svmModel, test.set  ))
#svmPred=as.logical(svmPred)

write.table(svmPred, file = "attractiveness_predictions.csv", append =FALSE, quote = FALSE, sep = ",",
            eol = "\n", na = "", dec = ".", row.names = FALSE,
            col.names = "male", qmethod = c("escape", "double"),
            fileEncoding = "")