import pandas as pd
import glob, os
 
os.chdir("C:\Users\ajax77\Documents\ASSIST\Training Data\Session01")
results = pd.DataFrame([])
 
for counter, file in enumerate(glob.glob("armIMU*")):
    namedf = pd.read_csv(file, skiprows=0, usecols=[1,2,3])
    results = results.append(namedf)
 
results.to_csv('C:\Users\ajax77\Documents\ASSIST\Training Data\combinedfile.csv')