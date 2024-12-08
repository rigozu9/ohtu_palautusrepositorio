KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None or kasvatuskoko is None:
            self.kapasiteetti = KAPASITEETTI
            self.kasvatuskoko = OLETUSKASVATUS

        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti
            self.kasvatuskoko = kasvatuskoko

        self.alkiot = self._luo_lista(self.kapasiteetti)

        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.alkiot

    def lisaa(self, n):
        if self.alkioiden_lkm == 0:
            self.alkiot[0] = n
            self.alkioiden_lkm += 1
            return True

        if not self.kuuluu(n):
            self.alkiot[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.alkiot) == 0:
                self.alkiot = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)

            return True

        return False

    def poista(self, n):
        kohta = -1
        apu = 0

        if n in self.alkiot:
            kohta = self.alkiot.index(n)
            self.alkiot[kohta] = 0

        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.alkiot[j]
                self.alkiot[j] = self.alkiot[j + 1]
                self.alkiot[j + 1] = apu

            self.alkioiden_lkm -= 1
            return True

        return False    

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.mahtavuus())

        for i in range(0, len(taulu)):
            taulu[i] = self.alkiot[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for i in a.to_int_list() + b.to_int_list():
            x.lisaa(i)
        return x
    
    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        yhteiset = set(a.to_int_list()) & set(b.to_int_list())
        for i in yhteiset:
            y.lisaa(i)
        return y
    
    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        erotus = set(a.to_int_list()) - set(b.to_int_list())
        for i in erotus:
            z.lisaa(i)
        return z
    
    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.alkiot[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.alkiot[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.alkiot[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
