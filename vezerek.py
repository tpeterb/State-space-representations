from Feladat import *

class vezerek(Feladat):
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
            for m in range(1, s):
                if allapot[m - 1] != i and abs(s - m) != abs(i - allapot[m - 1]):
                    elolfeltetel = True
                else:
                    elolfeltetel = False
                    break

            if elolfeltetel:
                uj_allapot = list(allapot)
                uj_allapot[s - 1] = i
                uj_allapot[8] = s + 1
                uj_allapot2 = tuple(uj_allapot)
                lepesek.append(uj_allapot2)

        return lepesek

if __name__ == "__main__":
    vezer = vezerek((0, 0, 0, 0, 0, 0, 0, 0, 1), 9)
    print(vezer.rakovetkezo((1, 3, 6, 0, 0, 0, 0, 0, 4)))
