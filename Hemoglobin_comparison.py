# i am importing the packages and lib use to read the excel

import pandas as pd
import matplotlib.pyplot as plt
 
# this line of code reads my excel file
df = pd.read_excel("sickle_cell_dataset_100_rows 2.xlsx")
print(df.head())

# i am going to calculate the MEDIAN hemoglobin level for each sickle cell type

median_hemoglobin = df.groupby("Sickle_Cell_Type")["Hemoglobin_Level_g_dL"].median()
print(median_hemoglobin)
 
# i will be drawing the median hemoglobin using barchart for different sickle cell types
median_hemoglobin.plot(kind="bar", color=["yellow", "lightgreen"])

plt.title("Median Hemoglobin Level by Sickle Cell Type", fontsize=14)
plt.xlabel("Sickle Cell Type", fontsize=12)
plt.ylabel("Median Hemoglobin Level (g/dL)", fontsize=12)
plt.axhline(y=11.0, color="green", linestyle="--", label="Normal Level (11.0)")
plt.legend()
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("Hemoglobin_level_by_sickle_cell_type.png")
plt.show()
 
 # Answer to the question Do children with HbSS have lower typical hemoglobin than HbSC?

print("\nDo children with HbSS have lower typical hemoglobin than HbSC?")
print(f"HbSS median: {median_hemoglobin['HbSS']} g/dL")
print(f"HbSC median: {median_hemoglobin['HbSC']} g/dL")
print("YES - HbSS has lower hemoglobin")