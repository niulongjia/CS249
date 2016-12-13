not.installed <- function(pkg) !is.element(pkg, installed.packages()[,1])
if (not.installed("e1071")) install.packages("e1071", repos = "http://cran.r-project.org")
if (not.installed("zoo")) install.packages("zoo", repos = "http://cran.r-project.org")
if (not.installed("mice")) install.packages("mice", repos = "http://cran.r-project.org")

library(zoo)
library(e1071)
library(mice)

training.set = read.csv( file("attractiveness_train.csv"), header = TRUE )
test.set = read.csv( file("attractiveness_test.csv"), header = TRUE )

training.set=mice(training.set)
training.set=complete(training.set)
test.set=mice(test.set)
test.set=complete(test.set)

logistic_regression_L2 = function( formula, dataset, tol=1.0e-6, lambda = 0) 
{
  initial.model = model.frame( formula, dataset )
  X = model.matrix( formula, data = dataset )
  y = model.response( initial.model, "numeric" )  # y values should be 0 and 1
  w = matrix(0, nrow = dim(X)[2])
  #ybar = mean(y)
  #w0 = log(ybar / (1 - ybar))
  flag = 1
  while (flag)
  {
    # eta = matrix(w0, ncol = dim(X)[1]) + t(w) %*% t(X)
    etai = t(w) %*% t(X)
    mui = 1 / (1 + exp(-etai))
    s = mui * (1 - mui)
    zi = etai + (y - mui) / s
    S = diag(as.vector(s))
    # w_new = solve(t(X) %*% S %*% (X)) %*% t(X) %*% S %*% t(z)
    w_new = solve(t(X) %*% S %*% (X) + lambda * diag(1, nrow = dim(X)[2])) %*% 
                 (t(X) %*% t(y - mui) - lambda * w) + w
    # w_new = solve(t(X) %*% S %*% (X)) %*% (t(X) %*% t(y - mu)) + w
    flag = ifelse(sum((w - w_new)^2) > tol, 1, 0)
    w = w_new
  }
  return(w)
}

returnList = logistic_regression_L2( male ~ ., training.set, lambda = 1)
svmPred= returnList[1]+
        returnList[2]*test.set$age+
        returnList[3]*test.set$weight+
        returnList[4]*test.set$attractive+
        returnList[5]*test.set$intelligence+
        returnList[6]*test.set$trustworthy
svmPred = (svmPred>=0.5)

write.table(svmPred, file = "attractiveness_predictions.csv", append =FALSE, quote = FALSE, sep = ",",
            eol = "\n", na = "", dec = ".", row.names = FALSE,
            col.names = "male", qmethod = c("escape", "double"),
            fileEncoding = "")