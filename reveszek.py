from Feladat import  *

class reveszek(Feladat):
    def __init__(self, kezdo, cel):
        self.kezdo = kezdo
        self.cel = cel

    def celteszt(self, allapot):
        return allapot == self.cel

    def rakovetkezo(self, allapot):
        lepesek = []
        kecske, farkas, kaposzta, hajo = allapot

        for i in range(0, 4):
            elofeltetel = True
            if i == 0 and (kecske == kaposzta or kecske == farkas):
                elofeltetel = False
                continue
            if i != 0 and allapot[i - 1] != hajo:
                elofeltetel = False
                continue
            if i == 1:
                elofeltetel = True
            if i == 2 and kecske == kaposzta == hajo:
                elofeltetel = False
                continue
            if i == 3 and kecske == farkas == hajo:
                elofeltetel = False
                continue

            if elofeltetel:
                uj_allapot = list(allapot)
                uj_allapot[i - 1] = 1 - hajo
                uj_allapot[3] = 1 - hajo
                uj_allapot2 = tuple(uj_allapot)
                lepesek.append(uj_allapot2)

        return lepesek

if __name__ == "__main__":
    revesz = reveszek((0, 0, 0, 0), (1, 1, 1, 1))
    print(revesz.rakovetkezo((0, 1, 0, 0)))
