import numpy as np
import matplotlib.pyplot as plt
import matplotlib

faixa_etaria = np.arange(4,105,5)

num_mulheres = [ 6779171, 7345231, 8441348, 8432004, 8614963, 8643419, 8026854, 7121915, 6688796, 6141338, 5305407, 4373877,
3468085, 2616745, 2074264, 1472930, 998349, 508724, 211594, 66806, 16989]

plt.figure( figsize=(15, 8))

plt.bar(faixa_etaria, num_mulheres, color="royalblue", align='center', width=4.0, ec = "k", alpha = .8)
plt.xlabel("Faixa etária", fontsize = 14)
plt.ylabel("População feminina", fontsize = 14)

plt.title("Distribuição por faixa etária da população feminina no Brasil-(2010)")

plt.yticks([ 100000, 1000000,  2000000,  3000000,  4000000, 5000000, 6000000, 7000000, 8000000, 9000000 ],
           [ "100 mil", "1 mi", "2 mi", "3 mi", "4 mi", "5 mi", "6 mi", "7 mi", "8 mi", "9 mi" ] )

plt.xticks([4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79,84,89,94,99,104],
           ["0-4","5-9","10-14","15-19","20-24","25-29","30-34","35-39","40-44",
             "45-49","50-54","55-59","60-64","65-69","70-74","75-79","80-84","85-89",
             "90-94","95-99", ">100"])

plt.show()
