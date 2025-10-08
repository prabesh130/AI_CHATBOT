import { Link, useNavigate } from 'react-router-dom';

export default function Navbar() {
  const token = localStorage.getItem('token')
  const navigate = useNavigate()

  const handleLogout = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <>
      <nav className="w-full h-[70px] bg-[#28a428] px-16 z-50">
        <div className="w-full h-full flex items-center justify-between">
          <Link to="/" className="flex items-center space-x-3">
            <span className="text-3xl font-mono  font-semibold dark:text-white">CHATBOT</span>
          </Link>

          <div className="flex gap-9 text-white text-lg font-medium">
            <Link to="/chat" className="hover:text-black">Chat</Link>
            <a href="#features" className="hover:text-black">Features</a>
            <Link to="#" className="hover:text-black">Pricing</Link>
            <Link to="#" className="hover:text-black">Resources</Link>
          </div>

          <div className="w-[80px] h-[38px] bg-white grid place-content-center rounded-md shadow-[0_5px_0_#B6B4B3] duration-75 active:translate-y-[3px] active:shadow-[1px_2px_0_#B6B4B3s] font-semibold">
            {!token ?/*Authentication Part */
              <Link to="/signup">Start</Link> :
              <div className='cursor-pointer' onClick={handleLogout}>Logout</div>
            }
          </div>

        </div>
      </nav>
    </>
  );
}