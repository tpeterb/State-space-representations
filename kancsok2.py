from Feladat import *

class kancsok(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel
        self.kapacitas = [8, 5, 3]

    def celteszt(self, allapot):
        return allapot[0] == self.cel or allapot[1] == self.cel

    def rakovetkezo(self, allapot):
        lepesek = []

        for i in range(0, 3):
            elofeltetel = True
            for j in range(0, 3):
                elofeltetel = True
                if i == j:
                    elofeltetel = False
                    continue
                if allapot[i] > 0 and allapot[j] < self.kapacitas[j]:
                    elofeltetel = True
                else:
                    elofeltetel = False

                if elofeltetel:
                    uj_allapot = list(allapot)
                    m = min(allapot[i], self.kapacitas[j] - allapot[j])
                    uj_allapot[i] = uj_allapot[i] - m
                    uj_allapot[j] = uj_allapot[j] + m
                    uj_allapot2 = tuple(uj_allapot)
                    lepesek.append(uj_allapot2)

        return lepesek

if __name__ == "__main__":
    kancso = kancsok((8, 0, 0), 4)
    print(kancso.rakovetkezo((3, 5, 0)))
