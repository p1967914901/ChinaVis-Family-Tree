import json
from sklearn.manifold import TSNE


class TSNEModel():
    def __init__(self, data):
        self.data = data
    
    def build(self):
        Tsne = TSNE(n_components=2)
        coordinates = Tsne.fit_transform(self.data)
        return coordinates

    # Tsne = TSNE(n_components=2)
    # outputAll = {}
    # a = [[CLOSO[i], MDSO[i], PO[i], APTO[i], ASO[i], STO[i]] for i in range(len(origin))]
    # # a = [[CLOSO[i], MDSO[i], PO[i], APTO[i], ASO[i]] for i in range(len(origin))]
    # # a = [[CLOSO[i], MDSO[i], PO[i], APTO[i]] for i in range(len(origin))]
    # # a = [[CLOSO[i], MDSO[i], PO[i]] for i in range(len(origin))]
    # # a = [[CLOSO[i], MDSO[i]] for i in range(len(origin))]

    # coordinates = Tsne.fit_transform(a)
