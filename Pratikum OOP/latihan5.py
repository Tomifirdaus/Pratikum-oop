from abc import ABC, abstractmethod

# 1. Abstract Class / Interface
# Ini adalah KONTRAK untuk semua unit game
class GameUnit(ABC):

    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass


# 2. Class Hero (Implementasi dari GameUnit)
class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")

    def info(self):
        print(f"Saya adalah Hero: {self.nama}")


# 3. Class Monster (Implementasi dari GameUnit)
class Monster(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")

    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")


# ===== UJI COBA =====
# unit = GameUnit()  # ERROR: abstract class tidak bisa dibuat objek

h = Hero("Alpha")
m = Monster("Serigala")

h.info()
h.serang("Serigala")

m.info()
m.serang("Alpha")
