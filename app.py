import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración general
st.set_page_config(page_title="Universidad de la Costa - Dashboard", layout="wide")

# Título y descripción
st.title("📊 Universidad de la Costa — Panel de Análisis Estudiantil")
st.markdown("Explora las métricas institucionales por año, semestre y facultad. Los gráficos se actualizan dinámicamente con tus filtros.")

# Carga de datos
df = pd.read_csv("university_student_data.csv")

# ======= Filtros laterales =======
st.sidebar.header("🎯 Filtros")
years = st.sidebar.multiselect("Selecciona año(s):", sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
terms = st.sidebar.multiselect("Selecciona semestre(s):", df["Term"].unique(), default=df["Term"].unique())
facultades = ["Engineering Enrolled", "Business Enrolled", "Arts Enrolled", "Science Enrolled"]
facultad_sel = st.sidebar.selectbox("Selecciona facultad:", facultades)

# ======= Filtrado dinámico =======
df_filtered = df[(df["Year"].isin(years)) & (df["Term"].isin(terms))]

# ======= KPIs =======
total_apps = df_filtered["Applications"].sum()
ret_rate = df_filtered["Retention Rate (%)"].mean()
satisfaction = df_filtered["Student Satisfaction (%)"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("📥 Solicitudes Totales", f"{total_apps:,}")
col2.metric("📈 Tasa de Retención Promedio", f"{ret_rate:.2f}%")
col3.metric("💬 Satisfacción Estudiantil Promedio", f"{satisfaction:.2f}%")

st.markdown("---")

# ======= Gráficos =======
col1, col2 = st.columns(2)

# Gráfico 1: Retención a lo largo del tiempo
fig1 = px.line(df_filtered, x="Year", y="Retention Rate (%)", markers=True,
               title="Tendencia de la Tasa de Retención")
col1.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Satisfacción promedio por semestre
fig2 = px.bar(df_filtered, x="Term", y="Student Satisfaction (%)", color="Term",
              title="Satisfacción Estudiantil por Semestre", barmode="group")
col2.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Distribución por facultades
mean_fac = df_filtered[facultades].mean()
fig3 = px.pie(values=mean_fac.values, names=mean_fac.index, title="Distribución Promedio de Matrículas por Facultad")
st.plotly_chart(fig3, use_container_width=True)

st.success("✅ Panel interactivo listo. ¡Ahora súbelo a GitHub y publícalo en Streamlit Cloud!")
