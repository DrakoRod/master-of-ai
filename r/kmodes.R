data = read.csv("../data/sample2.csv")

sprintf("Cols: %s", ncol(data))
sprintf("Rows: %s", nrow(data))

numRowsSample = nrow(data)
nKs = 3

print("::::::::::::::")
print("Ks randmon selected::")
for (i in 1:nKs) {
  randmon_num = sample(1:numRowsSample, 1, replace = FALSE)
}
print(randmon_num)

print("::::::::::::::")

# Create Ks data frame from original csv data frame
ks = data[0,]

# Iterating using a for loop

for (i in 1:nrow(data)) {
   x = list()
   print(i)
  row_data <- data[i,]
}

