const Sidebar = () => {
  return (
    <aside className="w-64 bg-gray-800 text-white p-4">
      <nav>
        <ul>
          <li className="mb-2"><a href="/dashboard">Dashboard</a></li>
          <li className="mb-2"><a href="/mahasiswa">Data Mahasiswa</a></li>
          <li className="mb-2"><a href="/dosen">Data Dosen</a></li>
          <li className="mb-2"><a href="/matakuliah">Data Mata Kuliah</a></li>
          <li className="mb-2"><a href="/krs">KRS</a></li>
          <li className="mb-2"><a href="/khs">KHS</a></li>
          <li className="mb-2"><a href="/jadwal">Jadwal Kuliah</a></li>
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
