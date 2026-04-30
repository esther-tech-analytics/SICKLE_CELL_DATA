# i am importing the packages and lib use to read the excel file and draw my chart

import pandas as pd
import matplotlib.pyplot as plt

# this line of code reads my excel file
df = pd.read_excel("sickle_cell_dataset_100_rows 2.xlsx")
print(df.head())

# i am going to calculate the average sick days for each town
avg_sick_days = df.groupby("Town")["Total Sick Days"].mean().round()
print(avg_sick_days)

# i will be drawing my average sick days using barchart for each of the towns
avg_sick_days.plot(kind="bar",color=["steelblue","coral","mediumseagreen"],edgecolor="black")


plt.title("Average Sick Days Per Town", fontsize=14)
plt.xlabel("Town", fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Average_sick_days_per_town.png")
plt.show()
