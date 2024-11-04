class PriorityQueue:
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        if self.is_empty():
            return
        return self.data[0]

    def enqueue(self, prioritas, data):
        self.data.append((prioritas, data))
        self.data.sort(reverse=True)


    def dequeue(self):
        if self.is_empty():
            return
        return self.data.pop(0)

    def write_all_data(self):
        print(self.data)

def print_pasien(pq : PriorityQueue):
    #Cara 1
    # data = pq.data
    # prioritas = ""
    # pasien = ""
    # awalan = 1
    # for pas, pasien in data:
    #     if pas == 3:
    #         prioritas = "Sudah meninggal"
    #     elif pas == 2:
    #         prioritas = "Merah"
    #     elif pas == 1:
    #         prioritas = "Kuning"
    #     else:
    #         prioritas = "Invalid status"
    #     print(f"{awalan}. {pasien}, status: {prioritas}")
    #     awalan += 1
    
    #Cara 2
    data = pq.data
    status_prioritas = {
        3: "Sudah meninggal",
        2: "Merah",
        1: "Kuning"
    }
    awalan = 1
    for pas, pasien in data:
        prioritas = status_prioritas.get(pas, "Status tidak valid")
        print(f"{awalan}. {pasien}, status: {prioritas}")
        awalan += 1


if __name__ == "__main__":
    #Cara 1
    # a = PriorityQueue()
    # print("Masukkan 3 Pasien")
    # for i in range (3):    
    #     nama = input("Nama pasien: ")
    #     respirasi = int(input("Kecepatan Respirasi Per Menit: "))
    #     if respirasi == 0:
    #         Prio = 3
    #     elif respirasi < 10 or respirasi > 30:
    #         Prio = 2
    #     else:
    #         denyut = input("Denyut lemah/tidak terasa (y/n): ").lower()
    #         if denyut == "y":
    #             Prio = 2
    #         else:
    #             perintah = input("Apakah Bisa Diperintah? (y/n): ").lower()
    #             if perintah == "y":
    #                 Prio = 1
    #             else:
    #                 Prio = 2
    #     a.enqueue(Prio,nama)
    #     print ()
    # print ("=== Hasil Data Pasien ===")
    # print_pasien(a)
    antrian_pasien = PriorityQueue()
    print("Masukkan 3 Pasien")
    for i in range(3):    
        nama_pasien = input("Nama pasien: ")
        kecepatan_respirasi = int(input("Kecepatan Respirasi Per Menit: "))
        if kecepatan_respirasi == 0:
            prioritas_pasien = 3
        elif kecepatan_respirasi < 10 or kecepatan_respirasi > 30:
            prioritas_pasien = 2
        else:
            denyut_nadi = input("Denyut lemah/tidak terasa (y/n): ").strip().lower()
            if denyut_nadi == "y":
                prioritas_pasien = 2
            else:
                status_mental = input("Apakah Bisa Diperintah? (y/n): ").strip().lower()
                if status_mental == "y":
                    prioritas_pasien = 1
                else:
                    prioritas_pasien = 2
        antrian_pasien.enqueue(prioritas_pasien, nama_pasien)
        print()
    print("=== Hasil Data Pasien ===")
    status_prioritas = {
        3: "Sudah meninggal",
        2: "Merah",
        1: "Kuning"
    }
    nomor = 1
    for prio, nama in antrian_pasien.data:
        status = status_prioritas.get(prio, "Status tidak valid")
        print(f"{nomor}. {nama}, status: {status}")
        nomor += 1