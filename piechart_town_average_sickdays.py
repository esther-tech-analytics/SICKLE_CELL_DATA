# i am importing the libraries needed
import pandas as pd
import matplotlib.pyplot as plt 

#i am importing the excel file
df =pd.read_excel("sickle_cell_dataset_100_rows 2.xlsx")

#check if data load correctly
print(df.head())

# grouping the avg_sick_days by Town
avg_sick_days =df.groupby("Town")["Total Sick Days"].mean().round()
print(avg_sick_days)

#plotting the piechart
plt.figure(figsize=(7,7))

avg_sick_days.plot(
    kind="pie", 
    colors=["blue", "purple", "red"],
    autopct="%1.1f%%",
    startangle=90,
    )
#adding title for the pie chart

plt.title("Average Total Sick Days Per Town" , fontsize=16)
plt.ylabel("")
plt.tight_layout()
plt.savefig("Esther_pie_chart.png")
plt.show()




