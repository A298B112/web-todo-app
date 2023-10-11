import streamlit as st
import functions

todos = functions.get_todos()


def add_todo(task):
    task = task + "\n"
    todos.append(task)
    functions.write_todos(todos)


st.title("To-Do app")
st.subheader("This is a todo app.")
st.write("This app is to increase your productivity.")
st.write("Today you have ", len(todos),  "to complete.")

for i, t in enumerate(todos):
    checkbox = st.checkbox(t, key=t)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[t]
        st.rerun()

with st.form("New task", clear_on_submit=True):
    new_task = st.text_input("Enter a new todo:", placeholder="Write the new todo here")
    submitted = st.form_submit_button("Submit")
    if submitted:
        add_todo(new_task)
        st.rerun()
