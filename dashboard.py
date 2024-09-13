import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
st.set_page_config(
    layout='wide',
    page_icon="🎉",
    page_title="pokemon dashboard",
)

@st.cache_data
def load_data():
    file = "pokemon.csv"
    data = pd.read_csv(file)
    return data

def main():
    # st.image('image.jpg',use_column_width=True)
    st.title("pokemon dashboard")
    with st.spinner("loading pokemons..."):
      df =load_data()

     # st.snow()
    rows, columns = df.shape
    col_names = df.columns.tolist()
    c1,c2,c3 = st.columns(3)
    c1.subheader(f"Total rows: {rows}")
    c2.subheader(f"Total columns: {columns}")
    c3.subheader(f"columns:{",".join(col_names)}")
    c1.metric("Pokemon Power", df.Total.sum(), delta=df.Total.mean())

    count = df['Type 1'].value_counts()
    fig = px.pie(count, values=count.values, names=count.index, 
                title="Pokemon Type Distribution", hole=.4)
    c2.plotly_chart(fig)
    c3.subheader("Pokemon Type 2 Distribution")
    count2 = df['Type 2'].value_counts()
    fig2 = px.bar(count2, count2.index, count2.values)
    c3.plotly_chart(fig2)

    cols = ['Attack','Defense','Sp. Atk','Sp. Def','Speed','HP']
    c1.subheader("Pokemon Stats")
    selections = c1.multiselect("Select Stats", cols, default=['HP','Attack'])

    if selections:
        fig3 = px.scatter_matrix(df, dimensions=selections,
                        color='Generation', height=800)
        st.plotly_chart(fig3, use_container_width=True)
        fig4 = px.histogram(df, x=selections, height=600)
        st.plotly_chart(fig4, use_container_width=True)

    c1, c2, c3, c4 = st.columns(4)
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()[1:]+['Generation']
    x = c1.selectbox("Select X-axis", num_cols, index=0)
    y = c2.selectbox("Select Y-axis", num_cols, index=1)
    z = c3.selectbox("Select Hue", num_cols, index=2)
    face = c4.selectbox("Select Face", cat_cols)

    fig5 = px.scatter(df, x=x, y=y, color=z, size='Total', 
                    hover_name='Name', 
                    facet_col=face, 
                    height=1500, 
                    facet_col_wrap=4)
    st.plotly_chart(fig5, use_container_width=True)

    fig6 = px.scatter_3d(df, x=x, y=y, z=z, color='Generation', 
                        size='Total', hover_name='Name', height=800)
    st.plotly_chart(fig6, use_container_width=True)


    

# yaha double underscore h 4 baaar

if __name__=="__main__":
    main()

# run command= streamlit run dashboard.py
