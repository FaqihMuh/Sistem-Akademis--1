const MahasiswaPage = () => {
  // Dummy data
  const mahasiswa = [
    { nim: '123', nama: 'Budi', jurusan: 'Teknik Informatika' },
    { nim: '456', nama: 'Ani', jurusan: 'Sistem Informasi' },
  ];

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Data Mahasiswa</h1>
      <table className="min-w-full bg-white">
        <thead>
          <tr>
            <th className="py-2 px-4 border-b">NIM</th>
            <th className="py-2 px-4 border-b">Nama</th>
            <th className="py-2 px-4 border-b">Jurusan</th>
          </tr>
        </thead>
        <tbody>
          {mahasiswa.map((m) => (
            <tr key={m.nim}>
              <td className="py-2 px-4 border-b text-center">{m.nim}</td>
              <td className="py-2 px-4 border-b text-center">{m.nama}</td>
              <td className="py-2 px-4 border-b text-center">{m.jurusan}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default MahasiswaPage;
