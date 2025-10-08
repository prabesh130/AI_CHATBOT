import React, { useState, useEffect } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import axios from 'axios'

export default function Signup() {
    const navigate = useNavigate()
    const [message, setMessage] = useState('')
    const [form, setForm] = useState({
        username: '',
        email: '',
        password: '',
        password2: ''
    })

    // Handle form input changes
    const handleChange = (e) => {
        const { name, value } = e.target
        setForm(prev => ({ ...prev, [name]: value }))
    }

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault()
        setMessage('')  // clear previous messages
        try {
            const response = await axios.post('http://127.0.0.1:8000/register/', form)
            console.log(response.data)
            setMessage('User registered successfully!')
            navigate('/login')  // redirect to login page after success
        } catch (error) {
            if (error.response && error.response.data) {
                // Show the first error returned by Django
                const firstKey = Object.keys(error.response.data)[0]
                setMessage(`${firstKey}: ${error.response.data[firstKey]}`)
            } else {
                setMessage('Server is not online')
            }
        }
    }

    // Check if user is already logged in
    useEffect(() => {
        const token = localStorage.getItem('token')
        if (token) navigate('/dashboard')
    }, [navigate])

    return (
        <div className="h-[calc(100vh-70px)] flex justify-center items-center bg-[#d6f5d6]">
            <div className='flex flex-col items-center bg-[#eafaea] p-6 shadow-black rounded-3xl'>
                <h2 className="text-2xl font-bold text-center mb-4">Create an account</h2>

                <form onSubmit={handleSubmit} className="flex flex-col gap-3 w-full max-w-sm">
                    <input
                        type="text"
                        name="username"
                        placeholder="Username"
                        value={form.username}
                        onChange={handleChange}
                        required
                        className="p-2 border bg-[#eafaea] border-gray-300 rounded-xl"
                    />
                    <input
                        type="email"
                        name="email"
                        placeholder="Email"
                        value={form.email}
                        onChange={handleChange}
                        required
                        className="p-2 border bg-[#eafaea] border-gray-300 rounded-xl"
                    />
                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        value={form.password}
                        onChange={handleChange}
                        required
                        className="p-2 border bg-[#eafaea] border-gray-300 rounded-xl"
                    />
                    <input
                        type="password"
                        name="password2"
                        placeholder="Confirm Password"
                        value={form.password2}
                        onChange={handleChange}
                        required
                        className="p-2 border bg-[#eafaea] border-gray-300 rounded-xl"
                    />

                    <div className="text-sm font-bold text-red-600 h-[20px]">{message}</div>

                    <button
                        type="submit"
                        className="bg-[#1e90ff] text-white font-semibold py-2 rounded-2xl hover:bg-[#1873cc] transition"
                    >
                        Create an account
                    </button>
                </form>

                <div className='text-sm flex items-center justify-center mt-3'>
                    <span className="font-medium text-gray-700 mr-2">Already have an account?</span>
                    <Link
                        to="/login"
                        className="font-semibold text-black hover:text-[#1e90ff]"
                    >
                        LOGIN
                    </Link>
                </div>
            </div>
        </div>
    )
}
