from django.db import models
from django.contrib.auth.models import User

class Fakultas(models.Model):
    nama_fakultas = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_fakultas

class Jurusan(models.Model):
    fakultas = models.ForeignKey(Fakultas, on_delete=models.CASCADE)
    nama_jurusan = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_jurusan

class Mahasiswa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    tanggal_lahir = models.DateField()
    jurusan = models.ForeignKey(Jurusan, on_delete=models.PROTECT)

    def __str__(self):
        return self.nama

class Dosen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nidn = models.CharField(max_length=20, unique=True)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    spesialisasi = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class MataKuliah(models.Model):
    jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE)
    kode_mk = models.CharField(max_length=10, unique=True)
    nama_mk = models.CharField(max_length=100)
    sks = models.IntegerField()

    def __str__(self):
        return self.nama_mk

class Kelas(models.Model):
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    dosen = models.ForeignKey(Dosen, on_delete=models.SET_NULL, null=True)
    tahun_ajaran = models.CharField(max_length=9) # e.g., 2024/2025
    SEMESTER_CHOICES = [('Ganjil', 'Ganjil'), ('Genap', 'Genap')]
    semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES)
    kapasitas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.mata_kuliah} - {self.dosen}"

class JadwalKuliah(models.Model):
    kelas = models.OneToOneField(Kelas, on_delete=models.CASCADE)
    HARI_CHOICES = [
        ('Senin', 'Senin'), ('Selasa', 'Selasa'), ('Rabu', 'Rabu'),
        ('Kamis', 'Kamis'), ('Jumat', 'Jumat'), ('Sabtu', 'Sabtu')
    ]
    hari = models.CharField(max_length=6, choices=HARI_CHOICES)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    ruang = models.CharField(max_length=20)

    def __str__(self):
        return f"Jadwal {self.kelas}"

class KRS(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    kelas = models.ManyToManyField(Kelas)
    tahun_ajaran = models.CharField(max_length=9)
    semester = models.CharField(max_length=6, choices=Kelas.SEMESTER_CHOICES)

    class Meta:
        unique_together = ('mahasiswa', 'tahun_ajaran', 'semester')

    def __str__(self):
        return f"KRS {self.mahasiswa} - {self.tahun_ajaran} {self.semester}"

class Nilai(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    NILAI_HURUF_CHOICES = [
        ('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C+', 'C+'),
        ('C', 'C'), ('D', 'D'), ('E', 'E')
    ]
    nilai_huruf = models.CharField(max_length=2, choices=NILAI_HURUF_CHOICES)
    
    @property
    def nilai_angka(self):
        konversi = {'A': 4.0, 'B+': 3.5, 'B': 3.0, 'C+': 2.5, 'C': 2.0, 'D': 1.0, 'E': 0.0}
        return konversi.get(self.nilai_huruf, 0.0)

    class Meta:
        unique_together = ('mahasiswa', 'kelas')

    def __str__(self):
        return f"Nilai {self.mahasiswa} - {self.kelas.mata_kuliah}"

