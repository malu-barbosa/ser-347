import numpy as np
import matplotlib.pyplot as plt
import matplotlib


num_homens = [ 7016987, 7624144, 8725413, 8558868, 8630229, 8460995, 7717658, 6766664, 6320568, 5692014,
            4834995, 3902344, 3041035, 2224065, 1667372, 1090517, 668623, 310759, 114964, 31529, 7247]

faixa_etaria = np.arange(4,105,5)

plt.figure(figsize=(15, 8))

plt.barh(faixa_etaria, num_homens, 4.0, color="darkblue", align='center', ec = "k")

plt.ylabel("Faixa etária", fontsize = 14)
plt.xlabel("População masculina", fontsize = 14)

plt.title("Distribuição por faixa etária da população masculina no Brasil-(2010)")

plt.xticks([ 100000, 1000000,  2000000,  3000000,  4000000, 5000000, 6000000, 7000000, 8000000, 9000000 ],
           [ "100 mil", "1 mi", "2 mi", "3 mi", "4 mi", "5 mi", "6 mi", "7 mi", "8 mi", "9 mi" ] )

plt.yticks([4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,89,94,99,104],
           ["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
             "45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89",
             "90-94","95-99", ">100"])

plt.show()