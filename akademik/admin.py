from django.contrib import admin
from .models import (
    Fakultas, Jurusan, Mahasiswa, Dosen, MataKuliah, 
    Kelas, JadwalKuliah, KRS, Nilai
)

admin.site.register(Fakultas)
admin.site.register(Jurusan)
admin.site.register(Mahasiswa)
admin.site.register(Dosen)
admin.site.register(MataKuliah)
admin.site.register(Kelas)
admin.site.register(JadwalKuliah)
admin.site.register(KRS)
admin.site.register(Nilai)
