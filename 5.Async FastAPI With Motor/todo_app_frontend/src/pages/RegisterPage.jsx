import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import api from '../api/axios';

const RegisterPage = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await api.post('/auth/register', { email, password });
            navigate('/login');
        } catch (err) {
            setError(err.response?.data?.detail || 'Registration failed');
        }
    };

    return (
        <div className="max-w-md mx-auto mt-20 bg-gray-800 p-8 rounded-lg shadow-lg">
            <h2 className="text-2xl font-bold text-white mb-6 text-center">Create an Account</h2>
            {error && (
                <div className="bg-red-900 border border-red-700 text-red-100 px-4 py-3 rounded mb-4">
                    {error}
                </div>
            )}
            <form onSubmit={handleSubmit} className="space-y-6">
                <div>
                    <label className="block text-sm font-medium text-gray-300">Email</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        className="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-white shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-2"
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-300">Password</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-white shadow-sm focus:border-blue-500 focus:ring-blue-500 px-4 py-2"
                    />
                </div>
                <button
                    type="submit"
                    className="w-full bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-800 transition-colors"
                >
                    Register
                </button>
            </form>
            <div className="mt-4 text-center">
                <p className="text-gray-400">
                    Already have an account?{' '}
                    <Link to="/login" className="text-blue-500 hover:text-blue-400">
                        Login here
                    </Link>
                </p>
            </div>
        </div>
    );
};

export default RegisterPage;
