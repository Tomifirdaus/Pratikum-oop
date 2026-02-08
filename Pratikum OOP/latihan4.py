class Hero:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        # Enkapsulasi: HP bersifat private
        self.__hp = hp_awal

    # GETTER: melihat HP
    def get_hp(self):
        return self.__hp

    # SETTER: mengubah HP dengan aturan
    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru

    def diserang(self, damage):
        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP: {self.get_hp()}")


# -- Main Program --
hero1 = Hero("Layla", 100)

# Coba set HP negatif
hero1.set_hp(-50)
print(hero1.get_hp())  # Output: 0

# Coba cheat HP
hero1.set_hp(9999)
print(hero1.get_hp())  # Output: 1000

# Coba diserang
hero1.diserang(200)