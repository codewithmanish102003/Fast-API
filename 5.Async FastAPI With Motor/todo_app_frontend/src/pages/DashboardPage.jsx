import { useEffect, useState } from 'react';
import api from '../api/axios';
import TodoForm from '../components/TodoForm';
import TodoItem from '../components/TodoItem';

const DashboardPage = () => {
    const [todos, setTodos] = useState([]);
    const [loading, setLoading] = useState(true);
    const [editingTodo, setEditingTodo] = useState(null);

    useEffect(() => {
        fetchTodos();
    }, []);

    const fetchTodos = async () => {
        try {
            const response = await api.get('/todos/');
            setTodos(response.data);
        } catch (err) {
            console.error('Failed to fetch todos:', err);
        } finally {
            setLoading(false);
        }
    };

    const handleCreateTodo = async (todoData) => {
        try {
            await api.post('/todos/', todoData);
            fetchTodos();
        } catch (err) {
            console.error('Failed to create todo:', err);
        }
    };

    const handleUpdateTodo = async (todoData) => {
        try {
            await api.put(`/todos/${editingTodo.id}`, todoData);
            setEditingTodo(null);
            fetchTodos();
        } catch (err) {
            console.error('Failed to update todo:', err);
        }
    };

    const handleToggleTodo = async (todo) => {
        try {
            await api.put(`/todos/${todo.id}`, { ...todo, completed: !todo.completed });
            fetchTodos();
        } catch (err) {
            console.error('Failed to toggle todo:', err);
        }
    };

    const handleDeleteTodo = async (id) => {
        if (!window.confirm('Are you sure you want to delete this todo?')) return;
        try {
            await api.delete(`/todos/${id}`);
            fetchTodos();
        } catch (err) {
            console.error('Failed to delete todo:', err);
        }
    };

    if (loading) {
        return (
            <div className="flex justify-center items-center h-64">
                <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
            </div>
        );
    }

    return (
        <div className="max-w-4xl mx-auto space-y-8">
            <div className="bg-gradient-to-r from-blue-900 to-gray-800 p-8 rounded-xl shadow-2xl">
                <h1 className="text-3xl font-bold text-white mb-2">My Tasks</h1>
                <p className="text-gray-300">Manage your daily goals and todos</p>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
                <div className="md:col-span-1">
                    <div className="sticky top-8">
                        <h2 className="text-xl font-semibold text-white mb-4">
                            {editingTodo ? 'Edit Task' : 'New Task'}
                        </h2>
                        <TodoForm
                            onSubmit={editingTodo ? handleUpdateTodo : handleCreateTodo}
                            initialData={editingTodo}
                            isEdit={!!editingTodo}
                            onCancel={() => setEditingTodo(null)}
                        />
                    </div>
                </div>

                <div className="md:col-span-2 space-y-4">
                    <h2 className="text-xl font-semibold text-white mb-4">Todo List</h2>
                    {todos.length === 0 ? (
                        <div className="bg-gray-800 p-8 rounded-lg text-center text-gray-400">
                            No tasks yet. Create one to get started!
                        </div>
                    ) : (
                        todos.map((todo) => (
                            <TodoItem
                                key={todo.id}
                                todo={todo}
                                onToggle={handleToggleTodo}
                                onDelete={handleDeleteTodo}
                                onEdit={setEditingTodo}
                            />
                        ))
                    )}
                </div>
            </div>
        </div>
    );
};

export default DashboardPage;
