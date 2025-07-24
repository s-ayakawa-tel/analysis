import streamlit as st
from utils import get_data
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.header("スタンドアロンアプリのデモ")

    # グラフを作成する
    fig = plt.figure(figsize=(6, 3))
    sns.set_theme(style="darkgrid")
    fmri = sns.load_dataset("fmri")
    sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri)
    # グラフを表示する
    st.pyplot(fig)


if __name__ == "__main__":
    main()

    st.title("サンプルStreamlitアプリ")
    data = get_data()
    st.write(data)
