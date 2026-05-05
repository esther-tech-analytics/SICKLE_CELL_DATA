# i am importing the packages and lib use to read the excel file and draw my chart

import pandas as pd
import matplotlib.pyplot as plt

# this line of code reads my excel file
df= pd.read_excel("sickle_cell_dataset_100_rows 2.xlsx")
print(df.head())

# i am calculating the average pain crises for each town
avg_pain_crises = df.groupby ("Town")["Pain_Crises_Per_Year"].mean()
print(avg_pain_crises)

# i will be drawing my average pain crises usign barcharts for each town
avg_pain_crises.plot(kind="bar", color=["purple", "orange","grey"])

plt.title("Average Pain Crises Per Town",fontsize=14)
plt.xlabel("Town",fontsize=12)
plt.ylabel("Average Pain Per Year",fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Average_Pain_Crises_Per_town.png")
plt.show()