import React, { useEffect } from 'react'
import { useState } from 'react';
import { Link, useNavigate} from 'react-router-dom';
import axios from 'axios'

export default function Signup() {
    const navigate = useNavigate
    const [message, setMessage] = ''
    const [form, setForm] = useState({
        fullname: '',
        email: '',
        password: '',
        confirmPassword: ''
    })

    const handleChange = async (e) => {
        const { name, value } = e.target
        setForm(prev => ({ ...prev, [name]: value }))
        if (name === 'email') { // checking whether the email already exist or not
            const response = await axios.post("http://localhost:5000/api/checkEmail", { email: value })
            setMessage(response.data.message)
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        try {
            if (message === 'Email already taken') {
                return
            }
            else {
                if (form.password === form.confirmPassword) {
                    const response = await axios.post('http://localhost:5000/api/users', form)
                    console.log(response.data)
                }
                else {
                    setMessage("Passwords doesnot match!!")
                }
            }
        } catch (error) {
            setMessage('SERVER IS NOT ONLINE')
        }
    }

    useEffect(() => {
        const checkLogin = () => { // to check whether JWT token already exists; user already signed in
            const token = localStorage.getItem('token')
            if (token) { navigate('/dashboard') }
        }
        checkLogin()
    }, [navigate])
    return (
        <>
            <div className="h-[calc(100vh-70px)] flex justify-center items-center bg-[#d6f5d6] ">
                <div className='flex flex-col items-center bg-[#eafaea] p-6 shadow-black rounded-3xl'>
                    <div>
                        <div className="flex flex-col  items-center space-y-4">
                            <h2 className="text-2xl font-bold text-center">Create an account</h2>
                            <div className="flex justify-center">
                                <Link
                                    to="/signup"
                                    className="w-[300px] flex items-center justify-center gap-2 bg-[#eafaea] border border-gray-400 rounded-2xl px-4 py-2 hover:bg-blue-200 transition"
                                >
                                    <svg className='h-5 w-5' xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="100" height="100" viewBox="0 0 48 48">
                                        <path fill="#FFC107" d="M43.611,20.083H42V20H24v8h11.303c-1.649,4.657-6.08,8-11.303,8c-6.627,0-12-5.373-12-12c0-6.627,5.373-12,12-12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C12.955,4,4,12.955,4,24c0,11.045,8.955,20,20,20c11.045,0,20-8.955,20-20C44,22.659,43.862,21.35,43.611,20.083z"></path><path fill="#FF3D00" d="M6.306,14.691l6.571,4.819C14.655,15.108,18.961,12,24,12c3.059,0,5.842,1.154,7.961,3.039l5.657-5.657C34.046,6.053,29.268,4,24,4C16.318,4,9.656,8.337,6.306,14.691z"></path><path fill="#4CAF50" d="M24,44c5.166,0,9.86-1.977,13.409-5.192l-6.19-5.238C29.211,35.091,26.715,36,24,36c-5.202,0-9.619-3.317-11.283-7.946l-6.522,5.025C9.505,39.556,16.227,44,24,44z"></path><path fill="#1976D2" d="M43.611,20.083H42V20H24v8h11.303c-0.792,2.237-2.231,4.166-4.087,5.571c0.001-0.001,0.002-0.001,0.003-0.002l6.19,5.238C36.971,39.205,44,34,44,24C44,22.659,43.862,21.35,43.611,20.083z"></path>
                                    </svg>
                                    <span className="text-sm font-medium text-gray-700">Connect with Google</span>
                                </Link>
                            </div>
                        </div >
                        <div className='text-center mt-3 font-bold'>OR</div>
                        <form onSubmit={handleSubmit} className="flex flex-col gap-3 p-3 bg-[#eafaea] w-full max-w-sm mb-3">
                            <input
                                type="text"
                                name="fullname"
                                placeholder="Full Name"
                                value={form.fullname}
                                onChange={handleChange}
                                required
                                className="w-[300px] p-2 border bg-[#eafaea] border-gray-300 rounded-xl"
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
                                name="confirmPassword"
                                placeholder="Confirm Password"
                                value={form.confirmPassword}
                                onChange={handleChange}
                                required
                                className="p-2 border bg-[#eafaea] border-gray-300 rounded-xl"
                            />
                            <div className="w-full h-[20px] text-sm font-bold text-red-600 uppercase animate-bounce">{message}</div>
                            <button
                                type="submit"
                                className="bg-[#1e90ff] text-white font-semibold py-2 rounded-2xl hover:bg-[#1873cc] transition"
                            >
                                Create an account
                            </button>
                        </form>
                        <div className='text-sm flex items-center justify-center'>
                            <span className="font-medium text-gray-700 mr-2">Already have an Account?</span>
                            <Link
                                to="/login"
                                className="font-semibold text-black  hover:text-[#1e90ff]"
                            >
                                LOGIN
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}
