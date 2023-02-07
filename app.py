import streamlit as st
import pandas as pd



import mysql.connector

import pandas as pd
#try:
#    mydb = connection.connect(host="127.0.0.1", database = 'first_project',user="root", passwd="backpacker0220!!",use_pure=True)
#    query = "Select * from watch_me;"
#    result_dataFrame = pd.read_sql(query,mydb)
#    mydb.close() #close the connection
#except Exception as e:
#    mydb.close()

import pandas as pd
st.sidebar.slider("Aga",min_value=8, max_value=80)

db_connection = mysql.connector.connect(host='127.0.0.1',
    database='for_imp', 
    user='root', 
    password='backpacker0220!!')

db_cursor = db_connection.cursor()
db_cursor.execute("Select * from watch_me")   
result = db_cursor.fetchall()
df = pd.DataFrame(result, columns=db_cursor.column_names)

db_connection.commit()


st.write(df)
st.write('Alfabeta')
st.write(df['brand'].unique())
text_in = st.text_input("Please tell Brand")
st.success("Grrean")
