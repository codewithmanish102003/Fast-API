const TodoItem = ({ todo, onToggle, onDelete, onEdit }) => {
    return (
        <div className="bg-gray-800 p-4 rounded-lg shadow-md border border-gray-700 flex items-center justify-between group hover:border-blue-500 transition-colors">
            <div className="flex items-center gap-4 flex-1">
                <input
                    type="checkbox"
                    checked={todo.completed}
                    onChange={() => onToggle(todo)}
                    className="h-5 w-5 rounded border-gray-600 bg-gray-700 text-blue-600 focus:ring-blue-500 focus:ring-offset-gray-800"
                />
                <div className={`flex-1 ${todo.completed ? 'opacity-50 line-through' : ''}`}>
                    <h3 className="text-lg font-medium text-white">{todo.title}</h3>
                    {todo.description && (
                        <p className="text-gray-400 text-sm mt-1">{todo.description}</p>
                    )}
                </div>
            </div>
            <div className="flex gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <button
                    onClick={() => onEdit(todo)}
                    className="p-2 text-gray-400 hover:text-blue-400 transition-colors"
                    title="Edit"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                </button>
                <button
                    onClick={() => onDelete(todo.id)}
                    className="p-2 text-gray-400 hover:text-red-400 transition-colors"
                    title="Delete"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                        <path fillRule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd" />
                    </svg>
                </button>
            </div>
        </div>
    );
};

export default TodoItem;
