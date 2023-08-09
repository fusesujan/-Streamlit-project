"""
This file contain whole code for a simple employee and department managing system.
"""


import os
import pandas as pd
import streamlit as st


# Load or create DataFrames for employee and department data
employee_data = pd.read_csv('employee.csv') if os.path.exists(
    'employee.csv') else pd.DataFrame(columns=["Empno", "Ename", "Job", "Deptno"])
department_data = pd.read_csv('department.csv') if os.path.exists(
    'department.csv') else pd.DataFrame(columns=["Deptno", "Dname", "Loc"])


def manage_employees_page():
    """
    function that define the whole code to get
    - employee no
    - employee name
    - job
    - department no 

    And returned as a whole page.
    """
    st.title("Manage Employees")

    # Add Employee Form
    st.markdown("""
            <style>
                .header {
                    text-align: center;
                    font-size:20px;
                }
            </style>
        """, unsafe_allow_html=True)

    st.markdown(
        "<h1 class='header'>Add Employee Data</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #f2f2f2; margin-top:5px'>",
                unsafe_allow_html=True)

    empno = st.text_input("Employee Number (Empno)")
    ename = st.text_input("Employee Name (Ename)")
    job = st.text_input("Job")
    deptno = st.text_input("Department Number (Deptno)")

    if st.button("Add Employee"):
        if empno and ename and job and deptno:
            # Add data to employee_data DataFrame
            employeedata = employee_data.append(
                {"Empno": empno, "Ename": ename, "Job": job, "Deptno": deptno}, ignore_index=True)
            employeedata.to_csv('employee.csv', index=False)
            st.success(f"Employee '{ename}' added successfully!")
        else:
            st.error("All fields are required.")


def manage_departments_page():
    """
    function that define the whole code to get
    - department no
    - department name
    - location


    And returned as a whole page.
    """
    st.title("Manage Departments")

    # Add Department Form
    st.markdown("""
            <style>
                .header {
                    text-align: center;
                    font-size:20px;
                }
            </style>
        """, unsafe_allow_html=True)

    st.markdown(
        "<h1 class='header'>Add Department</h1>", unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #f2f2f2; margin-top:5px'>",
                unsafe_allow_html=True)
    deptno = st.text_input("Department Number (Deptno)")
    dname = st.text_input("Department Name (Dname)")
    loc = st.text_input("Location (Loc)")

    if st.button("Add Department"):
        if deptno and dname and loc:
            # Add data to department_data DataFrame
            departmentdata = department_data.append(
                {"Deptno": deptno, "Dname": dname, "Loc": loc}, ignore_index=True)
            departmentdata.to_csv('department.csv', index=False)
            st.success(f"Department '{dname}' added successfully!")
        else:
            st.error("All fields are required.")


# Main Application


def main():
    '''
    main file that control the navigation between different pages
    '''
    st.sidebar.title("Navigation")

    # Create a dictionary with page names as keys and their corresponding functions as values
    pages = {
        "Manage Employees": manage_employees_page,
        "Manage Departments": manage_departments_page,
        "Visualization": None
    }

    # Create a radio button in the sidebar to select the page
    selected_page = st.sidebar.radio("Navigate to", list(pages.keys()))

    # Display the selected page content using the corresponding function
    page_function = pages[selected_page]
    if page_function:
        page_function()

    # Join and display data from both DataFrames
    if selected_page == "Visualization":
        st.title("Data Visualization")
        st.markdown("""
            <style>
                .header {
                    text-align: center;
                    font-size:20px;
                }
            </style>
        """, unsafe_allow_html=True)

        st.markdown(
            "<h1 class='header'>Joined Employee and Department Data</h1>", unsafe_allow_html=True)
        st.markdown("<hr style='border: 2px solid #f2f2f2; margin-top:5px'>",
                    unsafe_allow_html=True)

        joined_data = pd.merge(
            employee_data, department_data, on="Deptno", how="inner")
        st.dataframe(joined_data)


if __name__ == "__main__":
    main()
