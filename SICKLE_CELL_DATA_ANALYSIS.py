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
#plt.savefig("Average_sick_days_per_town.png")
#plt.show()



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
#plt.savefig("Average_Pain_Crises_Per_town.png")
#plt.show()



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
#plt.savefig("Hemoglobin_level_by_sickle_cell_type.png")
#plt.show()
 
 # Answer to the question Do children with HbSS have lower typical hemoglobin than HbSC?

print("\nDo children with HbSS have lower typical hemoglobin than HbSC?")
print(f"HbSS median: {median_hemoglobin['HbSS']} g/dL")
print(f"HbSC median: {median_hemoglobin['HbSC']} g/dL")
print("YES - HbSS has lower hemoglobin")


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
#plt.savefig("Onose_pie_chart.png")
#plt.show()


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
#plt.savefig("Esther_pie_chart.png")
#plt.show()

#i am doing the scattered plot chart
#Do older children have more pain crises than younger children
#note: there are no calculation
#plotting the piechart

plt.figure(figsize=(6,4))
plt.scatter(
    df["Age"],
    df["Pain_Crises_Per_Year"],
    color="coral",
    edgecolor= "black",
    alpha = 0.6
    )

#naming the chart
plt.title("Crises category" , fontsize=16)
plt.xlabel("by age group", fontsize=12)
plt.ylabel("pain crises")
plt.tight_layout()
#plt.savefig("age_correlation_chart.png")
#plt.show()

#How has the number of diagnosis changed over the year
#line graph
Diagnosis_Per_Year =df.groupby("Diagnosis_Year")["Child_ID"].count()
print(Diagnosis_Per_Year)

#creating canvas
plt.figure(figsize=(6,4))
plt.plot (Diagnosis_Per_Year.index,
          Diagnosis_Per_Year.values,
          color ="steelblue",
          marker="o",
          linewidth= 2,
          markersize= 7)
#naming the chart
plt.title("Diagnosis Trend" , fontsize=16)
plt.xlabel("Years", fontsize=12)
plt.ylabel("child ID")
plt.tight_layout()
#plt.savefig("Diagnosis_Trend_plt.png")
#plt.show()

#another method for line graph
Diagnosis_Per_Year = df.groupby ('Diagnosis_Year')["Child_ID"].count()
Diagnosis_Per_Year.plot (
    kind="line", color="red",
    marker="p",
    linewidth= 2,
    markersize= 7)

#naming the chart
plt.title("Diagnosis Trend" , fontsize=16)
plt.xlabel("Years", fontsize=12)
plt.ylabel("child ID")
plt.tight_layout()
plt.savefig("Diagnosis_Trend_plt.png")
plt.show()













