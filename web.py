import streamlit as st
from modules import functions
import random
todos = functions.get_todos()


def add_todo():
    new_to_do = st.session_state['new_to_do']
    todos.append(new_to_do + '\n')
    functions.write_todos(todos)
    st.session_state['new_to_do'] = ''


st.title("Todo App")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key='new_to_do')

