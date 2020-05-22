import numpy as np

# definindo as séries temprais
s1 = np.array((168, 398, 451, 337, 186, 232, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 323, 106, 1055, 170))
s2 = np.array((168, 400, 451, 300, 186, 200, 262, 349, 189, 204, 220, 220, 207, 239, 259, 258, 242, 331, 251, 180, 106, 1055, 200))

#distância euclidiana pelo numpy
d2 = np.linalg.norm(s1 - s2)
print("Distância euclidiana =", d2)

a = s1,s2
print("Médias = ", np.mean(a, axis = 0))
print("Máximos =", np.maximum(s1, s2))
print("Mínimos =", np.minimum(s1, s2))