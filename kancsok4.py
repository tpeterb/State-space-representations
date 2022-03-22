from Feladat import *

class kancsok(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel
        self.K1 = 5
        self.K2 = 3
        self.K3 = 2

    def celteszt(self, allapot):
        return allapot[0] == self.cel

    def rakovetkezo(self, allapot):
        lepesek = []
        k1, k2 = allapot
        k3 = 5 - (k1 + k2)

        if k1 > 0 and k2 < self.K2:
            m = min(k1, self.K2 - k2)
            lepesek.append((k1 - m, k2 + m))

        if k1 > 0 and k3 < self.K3:
            m = min(k1, self.K3 - k3)
            lepesek.append((k1 - m, k2))

        if k2 > 0 and k1 < self.K1:
            m = min(k2, self.K1 - k1)
            lepesek.append((k1 + m, k2 - m))

        if k2 > 0 and k3 < self.K3:
            m = min(k2, self.K3 - k3)
            lepesek.append((k1, k2 - m))

        if k3 > 0 and k1 < self.K1:
            m = min(k3, self.K1 - k1)
            lepesek.append((k1 + m, k2))

        if k3 > 0 and k2 < self.K2:
            m = min(k3, self.K2 - k2)
            lepesek.append((k1, k2 + m))

        return lepesek

if __name__ == "__main__":
    kancso = kancsok((5, 0), 4)
    print(kancso.rakovetkezo((2, 3)))
