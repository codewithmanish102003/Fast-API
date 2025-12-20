import { useEffect, useState } from 'react';

const TodoForm = ({ onSubmit, initialData = null, isEdit = false, onCancel }) => {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    useEffect(() => {
        if (initialData) {
            setTitle(initialData.title);
            setDescription(initialData.description || '');
        }
    }, [initialData]);

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ title, description });
        if (!isEdit) {
            setTitle('');
            setDescription('');
        }
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-4 bg-gray-800 p-6 rounded-lg shadow-lg">
            <div>
                <label htmlFor="title" className="block text-sm font-medium text-gray-300">
                    Title
                </label>
                <input
                    type="text"
                    id="title"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                    className="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-white shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-4 py-2"
                    placeholder="What needs to be done?"
                />
            </div>
            <div>
                <label htmlFor="description" className="block text-sm font-medium text-gray-300">
                    Description (Optional)
                </label>
                <textarea
                    id="description"
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    rows="3"
                    className="mt-1 block w-full rounded-md bg-gray-700 border-gray-600 text-white shadow-sm focus:border-blue-500 focus:ring-blue-500 sm:text-sm px-4 py-2"
                    placeholder="Add details..."
                />
            </div>
            <div className="flex gap-2">
                <button
                    type="submit"
                    className="flex-1 bg-blue-600 text-white px-4 py-2 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 focus:ring-offset-gray-800 transition-colors"
                >
                    {isEdit ? 'Update Todo' : 'Add Todo'}
                </button>
                {isEdit && (
                    <button
                        type="button"
                        onClick={onCancel}
                        className="flex-1 bg-gray-600 text-white px-4 py-2 rounded-md hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2 focus:ring-offset-gray-800 transition-colors"
                    >
                        Cancel
                    </button>
                )}
            </div>
        </form>
    );
};

export default TodoForm;
