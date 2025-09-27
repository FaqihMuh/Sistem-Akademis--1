class MataKuliah:
    def __init__(self, kode_mk, nama_mk, sks, jurusan_id):
        self.kode_mk = kode_mk
        self.nama_mk = nama_mk
        self.sks = sks
        self.jurusan_id = jurusan_id

class Kelas:
    def __init__(self, kelas_id, kode_mk, dosen_nidn, tahun_ajaran, semester, kapasitas):
        self.kelas_id = kelas_id
        self.kode_mk = kode_mk
        self.dosen_nidn = dosen_nidn
        self.tahun_ajaran = tahun_ajaran
        self.semester = semester
        self.kapasitas = kapasitas
        self.jadwal = None

class JadwalKuliah:
    def __init__(self, jadwal_id, kelas_id, hari, jam_mulai, jam_selesai, ruang):
        self.jadwal_id = jadwal_id
        self.kelas_id = kelas_id
        self.hari = hari
        self.jam_mulai = jam_mulai
        self.jam_selesai = jam_selesai
        self.ruang = ruang

class KRS:
    def __init__(self, krs_id, mahasiswa_nim, tahun_ajaran, semester):
        self.krs_id = krs_id
        self.mahasiswa_nim = mahasiswa_nim
        self.tahun_ajaran = tahun_ajaran
        self.semester = semester
        self.daftar_kelas = []

    def add_kelas(self, kelas):
        self.daftar_kelas.append(kelas)
        print(f"Kelas {kelas.kode_mk} ditambahkan ke KRS.")

    def remove_kelas(self, kelas):
        self.daftar_kelas.remove(kelas)
        print(f"Kelas {kelas.kode_mk} dihapus dari KRS.")

class KHS:
    def __init__(self, khs_id, mahasiswa_nim, tahun_ajaran, semester):
        self.khs_id = khs_id
        self.mahasiswa_nim = mahasiswa_nim
        self.tahun_ajaran = tahun_ajaran
        self.semester = semester
        self.ipk_semester = 0.0
        self.ipk_kumulatif = 0.0
        self.daftar_nilai = []

class Nilai:
    def __init__(self, nilai_id, mahasiswa_nim, kode_mk, nilai_huruf, nilai_angka):
        self.nilai_id = nilai_id
        self.mahasiswa_nim = mahasiswa_nim
        self.kode_mk = kode_mk
        self.nilai_huruf = nilai_huruf
        self.nilai_angka = nilai_angka
