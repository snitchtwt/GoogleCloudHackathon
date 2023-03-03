import axios from 'axios';
import { ADDNEW_TODO , GETALL_CURRENT_TODO ,TOGGLE_TODO,UPDATE_TODO,DELETE_TODO,TOGGLE_TABS } from './type';

const API_URL='http://localhost:8000';

// export const addNewTodo = (data) => async(dispatch) => {
//     try{
//         const res = await axios.post(`${API_URL}/todos`,{ data });
//         dispatch({type: ADDNEW_TODO, payload: res.data });

//     }
//     catch(error)
//     {
//         console.log('Error while calling addNewTodo API ',error.message);
//     }

// }

// export const getCurrentTodos = () => async(dispatch) => {
//     try{
//         const res = await axios.get(`${API_URL}/todos`,);
//         dispatch({type: GETALL_CURRENT_TODO, payload: res.data});

//     }
//     catch(error)
//     {
//         console.log('Error while calling getCurrentTodos API ',error.message);
//     }
// }

// export const toggleTodos = (id_) => async(dispatch) => {
//     try{
//         const res = await axios.get(`${API_URL}/todos/${id_}`,);
//         dispatch({type: TOGGLE_TODO, payload: res.data});

//     }
//     catch(error)
//     {
//         console.log('Error while calling toggleTodos API ',error.message);
//     }
// }

// export const updateTodo = (id_,data) => async(dispatch) => {
//     try{
//         const res = await axios.put(`${API_URL}/todos/${id_}`,{data});
//         dispatch({type: UPDATE_TODO, payload: res.data});

//     }
//     catch(error)
//     {
//         console.log('Error while calling updateTodo API ',error.message);
//     }
// }

// export const deleteTodo = (id_) => async(dispatch) => {
//     try{
//         const res = await axios.delete(`${API_URL}/todos/${id_}`,);
//         dispatch({type: DELETE_TODO, payload: res.data});

//     }
//     catch(error)
//     {
//         console.log('Error while calling deleteTodo API ',error.message);
//     }
// }

// export const toggleTab = (tab) => async(dispatch) => {
//     try{
        
//         dispatch({type: TOGGLE_TABS, selected:tab});

//     }
//     catch(error)
//     {
//         console.log('Error while calling toggleTab API ',error.message);
//     }
// }