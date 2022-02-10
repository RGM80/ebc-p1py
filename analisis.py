
import pandas as pd
excelData = pd.read_excel("C:/Users/upuan/Documents/ebc-python/ebc-p1py/sample-xls-file-for-testing.xls")
dataFrame = pd.DataFrame(excelData)
print(dataFrame.head())



