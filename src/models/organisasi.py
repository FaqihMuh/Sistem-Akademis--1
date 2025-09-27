class Fakultas:
    def __init__(self, fakultas_id, nama_fakultas):
        self.fakultas_id = fakultas_id
        self.nama_fakultas = nama_fakultas
        self.jurusan = []

class Jurusan:
    def __init__(self, jurusan_id, nama_jurusan, fakultas_id):
        self.jurusan_id = jurusan_id
        self.nama_jurusan = nama_jurusan
        self.fakultas_id = fakultas_id
        self.mahasiswa = []
        self.dosen = []
        self.mata_kuliah = []
