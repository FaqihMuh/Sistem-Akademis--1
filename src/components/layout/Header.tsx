import Link from 'next/link';

const Header = () => {
  return (
    <header className="bg-white shadow-md p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">Sistem Akademik</h1>
      <div>
        <Link href="/profile" className="mr-4">Profil</Link>
        <Link href="/logout">Logout</Link>
      </div>
    </header>
  );
};

export default Header;
