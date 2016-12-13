not.installed <- function(pkg) !is.element(pkg, installed.packages()[,1])
if (not.installed("caret")) install.packages("caret", repos="http://cran.us.r-project.org")
if (not.installed("pROC")) install.packages("pROC", repos="http://cran.us.r-project.org")
# if (not.installed("AppliedPredictiveModeling")) install.packages("AppliedPredictiveModeling")
# if (not.installed("doSNOW"))  install.packages("doSNOW", repos="http://cran.us.r-project.org")   # multicore computation in R in windows
# if (not.installed("doParallel"))  install.packages("doParallel", repos="http://cran.us.r-project.org")   # multicore computation in R in windows
# if (not.installed("kernlab"))  install.packages("kernlab", repos="http://cran.us.r-project.org")   # multicore computation in R in windows
# if (not.installed("e1071")) install.packages("e1071", repos = "http://cran.r-project.org")
# if (not.installed("C50")) install.packages("C50", repos = "http://cran.r-project.org")  
# if (not.installed("partykit")) install.packages("partykit", repos = "http://cran.r-project.org")  

# library(partykit)
# library(e1071)
# library(doSNOW)
# library(doParallel)
# library(AppliedPredictiveModeling)
# library(caret)
# library(kernlab)
# library(C50)
library(pROC)
library(caret)

load("grantData.RData")

ctrl <- trainControl(method = "LGOCV",
                     summaryFunction = twoClassSummary,
                     classProbs = TRUE,
                     index = list(TrainSet = pre2008),
                     savePredictions = TRUE)

c50Grid <- expand.grid(trials = c(1:9, (1:10)*10),
                       model = c("tree", "rules"),
                       winnow = c(TRUE, FALSE))
set.seed(476)
c50FactorFit <- train(training[,factorPredictors], training$Class,
                      method = "C5.0",
                      tuneGrid = c50Grid,
                      verbose = FALSE,
                      metric = "ROC",
                      trControl = ctrl)

test.set = read.csv( file("APM_prediction_input.csv"), header = TRUE, na.strings=c("","NA") ) 
test.set=subset(test.set, select=-c(Class)) 

C50Pred=predict(c50FactorFit,test.set,type="prob")

write.table(C50Pred, file = "predictions.csv", append =FALSE, quote = FALSE, sep = ",",
            eol = "\n", na = "", dec = ".", row.names = FALSE,
            col.names = FALSE, qmethod = c("escape", "double"),
            fileEncoding = "")
