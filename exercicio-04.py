import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.DataFrame({'Age': ['0-4','5-9','10-14','15-19','20-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-94','95-99','>100'],
                     'Male':[7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014, 4834995, 3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247],
                     'Female': [-6779171, -7345231, -8441348, -8432004, -8614963, -8643419, -8026854, -7121915, -6688796, -6141338, -5305407, -4373877,-3468085, -2616745, -2074264, -1472930, -998349, -508724, -211594, -66806, -16989]})

plt.figure(figsize=(25, 10))
Age2 = ["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
             "45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89",
             "90-94","95-99", ">100"]
bar_plot = sns.barplot(x='Male', y='Age', data=df, order=Age2, color="royalblue")

bar_plot = sns.barplot(x='Female', y='Age', data=df, order=Age2,color = "red")

plt.xticks([0,-1000000,  -2000000,  -3000000,  -4000000, -5000000, -6000000, -7000000, -8000000, -9000000,
              1000000,  2000000,  3000000,  4000000, 5000000, 6000000, 7000000, 8000000, 9000000 ],
           ["0","1 mi", "2 mi", "3 mi", "4 mi", "5 mi", "6 mi", "7 mi", "8 mi", "9 mi",
             "1 mi", "2 mi", "3 mi", "4 mi", "5 mi", "6 mi", "7 mi", "8 mi", "9 mi"] )
plt.ylabel("Faixa etária", fontsize = 14)
plt.xlabel("População", fontsize = 14)

plt.title("Distribuição da população feminina e masculina no Brasil-(2010)")
plt.gca().invert_yaxis()


plt.show()