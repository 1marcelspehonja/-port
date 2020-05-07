# Uvozimo potrebne knjižnice
library(rvest)
library(dplyr)
library(gsubfn)
library(readr)


igralci_1617 <- read_csv2("uvoz/igralci_1617.csv", na=":",locale=locale(encoding="Windows-1250"))
