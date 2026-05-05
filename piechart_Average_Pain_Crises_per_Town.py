# i am importing the libraries needed
import pandas as pd
import matplotlib.pyplot as plt 

#i am importing the excel file
df =pd.read_excel("sickle_cell_dataset_100_rows 2.xlsx")

#check if data load correctly
print(df.head())

# i am calculating the average pain crises for each town
avg_pain_crises = df.groupby ("Town")["Pain_Crises_Per_Year"].mean()
print(avg_pain_crises)

#plotting the piechart
plt.figure(figsize=(15,7))

avg_pain_crises.plot(
    kind="pie", 
    colors=["Green", "coral", "yellow"],
    autopct="%1.1f%%",
    startangle=90,
    )
#adding title for the pie chart

plt.title("Average Pain Crises Per Town" , fontsize=16)
plt.ylabel("")
plt.tight_layout()
plt.savefig("Onose_pie_chart.png")
plt.show()




