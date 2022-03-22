from Feladat import *

class kancsok(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel
        self.K1 = 8
        self.K2 = 5
        self.K3 = 3

    def celteszt(self, allapot):
        return allapot[0] == self.cel or allapot[1] == self.cel

    def rakovetkezo(self, allapot):
        lepesek = []
        k1, k2, k3 = allapot

        if k1 > 0 and k2 < self.K2:
            m = min(k1, self.K2 - k2)
            lepesek.append((k1 - m, k2 + m, k3))

        if k1 > 0 and k3 < self.K3:
            m = min(k1, self.K3 - k3)
            lepesek.append((k1 - m, k2, k3 + m))

        if k2 > 0 and k1 < self.K1:
            m = min(k2, self.K1 - k1)
            lepesek.append((k1 + m, k2 - m, k3))

        if k2 > 0 and k3 < self.K3:
            m = min(k2, self.K3 - k3)
            lepesek.append((k1, k2 - m, k3 + m))

        if k3 > 0 and k1 < self.K1:
            m = min(k3, self.K1 - k1)
            lepesek.append((k1 + m, k2, k3 - m))

        if k3 > 0 and k2 < self.K2:
            m = min(k3, self.K2 - k2)
            lepesek.append((k1, k2 + m, k3 - m))

        return lepesek

if __name__ == "__main__":
    kancso = kancsok((8, 0, 0), 4)
    print(kancso.rakovetkezo((3, 5, 0)))
