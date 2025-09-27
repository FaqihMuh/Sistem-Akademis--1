from abc import ABC, abstractmethod
from datetime import date

class User(ABC):
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def login(self):
        print(f"User {self.username} logged in.")

    def logout(self):
        print(f"User {self.username} logged out.")

class Admin(User):
    def __init__(self, user_id, username, password, admin_id):
        super().__init__(user_id, username, password, "Admin")
        self.admin_id = admin_id

    def manage_users(self):
        print(f"Admin {self.username} is managing users.")

    def manage_system_settings(self):
        print(f"Admin {self.username} is managing system settings.")

class Mahasiswa(User):
    def __init__(self, user_id, username, password, nim, nama, alamat, tanggal_lahir, jurusan_id):
        super().__init__(user_id, username, password, "Mahasiswa")
        self.nim = nim
        self.nama = nama
        self.alamat = alamat
        self.tanggal_lahir = tanggal_lahir
        self.jurusan_id = jurusan_id
        self.krs = []
        self.khs = []

    def view_krs(self):
        print(f"Mahasiswa {self.nama} is viewing KRS.")

    def view_khs(self):
        print(f"Mahasiswa {self.nama} is viewing KHS.")

    def view_jadwal(self):
        print(f"Mahasiswa {self.nama} is viewing jadwal.")

class Dosen(User):
    def __init__(self, user_id, username, password, nidn, nama, alamat, spesialisasi):
        super().__init__(user_id, username, password, "Dosen")
        self.nidn = nidn
        self.nama = nama
        self.alamat = alamat
        self.spesialisasi = spesialisasi

    def input_nilai(self):
        print(f"Dosen {self.nama} is inputting nilai.")

    def view_jadwal_mengajar(self):
        print(f"Dosen {self.nama} is viewing jadwal mengajar.")
