from Feladat import *

class huszarok(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        return allapot[8] == self.cel

    def rakovetkezo(self, allapot):
        lepesek = []
        s = allapot[8]

        for i in range(1, 9):
            elofeltetel = True
            for sor in range(1, s):
                if (abs(sor - s) == 2 and abs(allapot[sor - 1] - i) == 1) or (abs(sor - s) == 1 and abs(allapot[sor - 1] - i) == 2):
                    elofeltetel = False
                    break
                else:
                    elofeltetel = True

            if elofeltetel:
                uj_allapot = list(allapot)
                uj_allapot[s - 1] = i
                uj_allapot[8] = s + 1
                uj_allapot2 = tuple(uj_allapot)
                lepesek.append(uj_allapot2)

        return lepesek

if __name__ == "__main__":
    huszar = huszarok((0, 0, 0, 0, 0, 0, 0, 0, 1), 9)
    print(huszar.rakovetkezo((1, 2, 0, 0, 0, 0, 0, 0, 3)))
