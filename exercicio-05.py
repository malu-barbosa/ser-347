import numpy as np
import matplotlib.pyplot as plt

# dados de desmatamento do programa PRODES http://www.obt.inpe.br/OBT/assuntos/programas/amazonia/prodes
ano = np.arange(2004,2020)
desmatamento = [27772,19014,14286,11651,12911,7464,7000,6418,4571,5891,5012,6207,7893,6947,7536,9762]

plt.figure( figsize=(15, 11))
plt.subplot(1, 2, 1)

plt.bar(ano, desmatamento, color="darkred", align='center', width=0.8, ec = "k", alpha = .8)

plt.xlabel("Ano", fontsize = 14)
plt.ylabel("Taxa de desmatamento (Km²)", fontsize = 14)

plt.title("Desmatamento na Amazônia Legal Brasileira (2004-2019)",fontsize = 12)
plt.xticks([2004,2006,2008,2010,2012,2014,2016,2018],
              ["2004","2006","2008","2010","2012",
               "2014","2016","2018"])

plt.subplot(1, 2, 2)
plt.pie(desmatamento,
        labels = ano,
        colors = ["blue", "darkblue", "green", "red", "darkred", "seagreen", "royalblue", "orange","grey", "black", "darkgreen", "cyan","magenta","yellow","purple","pink"],
        labeldistance = 1.05,
        explode = [0, 0, 0, 0, 0, 0, 0, 0,.1,.2,.3,0,0,0,0,0],
        wedgeprops = {"ec": "k"},
        textprops = {"fontsize": 12},
        )
plt.axis("equal")
plt.title("Desmatamento na Amazônia Legal Brasileira (2004-2019)")

plt.show()