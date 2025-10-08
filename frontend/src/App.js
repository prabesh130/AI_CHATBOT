import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Navbar from "./components/Navbar"
import Home from "./components/Home"
import Signup from "./components/Signup"
import Login from "./components/Login"

export default function App() {
  return (
    <Router>
      <div className="min-h-screen  flex flex-col bg-gray-800">
        <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
          </Routes>
      </div>
    </Router>
  )
}

