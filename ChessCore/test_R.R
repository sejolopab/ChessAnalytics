# Title     : TODO
# Objective : TODO
# Created by: josegamboa
# Created on: 2019-06-20

library(pracma)
library(Smisc)
library(caret)

A <- matrix(data=c(10,-18,6,-11),nrow=2,ncol=2, byrow = TRUE)

v1 <- matrix(data=c(2,1),nrow=2,ncol=1, byrow = TRUE)
v2 <- matrix(data=c(3,2),nrow=2,ncol=1, byrow = TRUE)

gamma1 <- 1
gamma2 <- -2

identical(A %*% v1, gamma1 * v1)
identical(A %*% v2, gamma2 * v2)

eig(A) #vector de valores propios del paquete pracma
eigen(A) #funciones base de R