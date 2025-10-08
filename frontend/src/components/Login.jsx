import React, { useEffect, useState } from 'react'
import { Link, useNavigate} from 'react-router-dom';
import axios from 'axios'

export default function Login() {
    const navigate = useNavigate
    const [message, setMessage] = useState('')
    const [form, setForm] = useState({
        username: '',
        password: ''
    })

    const handleChange = (e) => {
        const { name, value } = e.target
        setForm(prev => ({ ...prev, [name]: value }))
    }
    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            const response = await axios.post('http://127.0.0.1:8000/login/', form)
            console.log(response.data)
        } catch (error) {
            setMessage("SERVER IS NOT ONLINE")
        }
    }

    useEffect(() => {
        const checkLogin = () => { // to check whether a JWT token already exists in localstorage; user already signed in
            const token = localStorage.getItem('token')
            if (token) { navigate('/chat') }
        }
        checkLogin()
    }, [navigate])
    return (
        <>
            <div className="h-[calc(100vh-70px)] flex flex-col justify-center items-center relative bg-[#d6f5d6] "><></>
                <div className='flex flex-col items-center bg-[#eafaea] p-6 shadow-black rounded-3xl'>
                    <div className="flex flex-col  items-center mb-10">
                        <h2 className="text-2xl font-bold text-center">Welcome back!!</h2>
                    </div >
                    <form className="flex flex-col  space-y-3 bg-[#eafaea] p-3 w-full max-w-sm mb-3" onSubmit={handleSubmit}>
                        <input
                            type="text"
                            name="username"
                            value={form.username}
                            onChange={handleChange}
                            placeholder="Username"
                            required
                            className="p-2 w-[300px] border bg-[#eafaea] border-gray-300 rounded-xl"
                        />
                        <input
                            type="password"
                            name="password"
                            value={form.password}
                            onChange={handleChange}
                            placeholder="Password"
                            required
                            className="p-2 border bg-[#eafaea] border-gray-300 rounded-xl"
                        />
                        <div className="w-full h-[20px] text-sm font-bold text-red-600 uppercase animate-bounce">{message}</div>
                        <button
                            type="submit"
                            className="bg-[#1e90ff] text-white font-semibold  py-2 rounded-2xl hover:bg-[#1873cc] transition"
                        >
                            Login
                        </button>


                    </form>
                    <div className='text-sm flex items-center'>
                        <span className="font-medium text-gray-700 mr-2">Don't have an Account?</span>
                        <Link
                            to="/signup"
                            className="font-semibold text-black hover:text-[#1e90ff]"
                        >
                            CREATE ONE
                        </Link>
                    </div>
                </div>
            </div>
        </>
    )
}
