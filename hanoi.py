from Feladat import *

class tornyok(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        return allapot == self.cel

    def rakovetkezo(self, allapot):
        lepesek = []

        for melyik in range(0, 3):
            elofeltetel = True
            for hova in ['P', 'Q', 'R']:
                elofeltetel = True
                if allapot[melyik] == hova:
                    elofeltetel = False
                    continue
                for i in range(0, melyik):
                    if allapot[i] != allapot[melyik] and allapot[i] != hova:
                        elofeltetel = True
                    else:
                        elofeltetel = False
                        break

                if elofeltetel:
                    uj_allapot = list(allapot)
                    uj_allapot[melyik] = hova
                    uj_allapot2 = tuple(uj_allapot)
                    lepesek.append(uj_allapot2)

        return lepesek

if __name__ == "__main__":
    torony = tornyok(('P', 'P', 'P'), ('R', 'R', 'R'))
    print(torony.rakovetkezo(('R', 'P', 'P')))
