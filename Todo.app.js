import React,{useState} from ':eact';
import TodoForm from'./TodoForm';
import {RiCLoseCircleLine} from'react-icons/ri';
import{TiEdit} from 'react-icons/ti';

const Todo = ({todos, completeTodo, removeTodo, updateTodo}) => {
    const [edit,setEdit] = useState({
        id:null,
        value:''
    });
const submitUpdate = value => {
    updateTodo(edit.id,value);
    setEdit({
        id:null,
        value:''
    });
};

if (edit.id) {
    return <TodoForm edit={edit} onSubmit={submitUpdate} />;
}
return todos.map((todo,index) => (
    <><div
        className={todo.isComplete ? 'todo-row-complete' : 'todo-row'}
        key={index}
    >
        <div key={todo.id} OnClick={() => completeTodo(todo.id)}></div>
        {todo.text}
    </div><div className='icons'>
            <RiCLoseCircleLine
                OnClick={() => removeTodo(todo.id)}
                className='delete-icon' />
            <TiEdit
                Onclick={() => removeTodo(todo.id)}
                className='edit-icon' />
        </div></>
));
};

export  default Todo;