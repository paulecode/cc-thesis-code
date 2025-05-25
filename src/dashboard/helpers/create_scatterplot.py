import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def create_scatter_plot(data, x_col, y_col, hue, xlabel, ylabel, legend_title):

    title = f"{xlabel} vs {ylabel}"
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.scatterplot(
        data=data, x=x_col, y=y_col, hue=hue,
        s=100,
        palette='tab10',
        ax=ax,
    )

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(title=legend_title, bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, linestyle='--', alpha=0.6)

    st.pyplot(fig)
