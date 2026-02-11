from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self,nama,harga):
        self.nama = nama
        self.__stok = 0
        self.__harga = harga

    def lihat_stok(self):
        return self.__stok

    def tambah_stok(self,jumlah):
        if jumlah < 0:
            print("Gagal update stok", self.nama, "!", "Stok tidak boleh negatif", f"({jumlah})")
        else:
            self.__stok = self.__stok + jumlah
            print("Berhasil menambahkan stok", self.nama, ":", jumlah, "unit.")

    def harga_dasar(self):
        return self.__harga

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self,jumlah):
        pass


class Laptop(BarangElektronik):
    def __init__(self,nama,harga,processor):
        super().__init__(nama,harga)
        self.processor = processor

    def tampilkan_detail(self):
        print("[LAPTOP]", self.nama, "| Proc:", self.processor)

    def hitung_harga_total(self,jumlah):
        pajak = self.harga_dasar() * 10 / 100
        total = (self.harga_dasar() + pajak) * jumlah
        print(" Harga Dasar: Rp", format(self.harga_dasar(),","), "| Pajak(10%): Rp", format(int(pajak),","))
        print(" Beli:", jumlah, "unit | Subtotal: Rp", format(int(total),","))
        return total


class Smartphone(BarangElektronik):
    def __init__(self,nama,harga,kamera):
        super().__init__(nama,harga)
        self.kamera = kamera

    def tampilkan_detail(self):
        print("[SMARTPHONE]", self.nama, "| Cam:", self.kamera)

    def hitung_harga_total(self,jumlah):
        pajak = self.harga_dasar() * 5 / 100
        total = (self.harga_dasar() + pajak) * jumlah
        print(" Harga Dasar: Rp", format(self.harga_dasar(),","), "| Pajak(5%): Rp", format(int(pajak),","))
        print(" Beli:", jumlah, "unit | Subtotal: Rp", format(int(total),","))
        return total


def proses_transaksi(barang):
    print("\n--- STRUK TRANSAKSI ---")
    total_semua = 0
    no = 1
    for b,jml in barang:
        print(str(no)+".", end=" ")
        b.tampilkan_detail()
        total_semua = total_semua + b.hitung_harga_total(jml)
        no += 1
    print("----------------------------------------")
    print("TOTAL TAGIHAN: Rp", format(int(total_semua),","))
    print("----------------------------------------")


print("--- SETUP DATA ---")
lap = Laptop("Lenovo Legion 5",17000000,"Ryzen 7")
hp = Smartphone("Xiaomi Redmi Note 12",3500000,"48MP")

lap.tambah_stok(5)
hp.tambah_stok(-4)
hp.tambah_stok(12)

proses_transaksi([
    (lap,2),
    (hp,1)
])
