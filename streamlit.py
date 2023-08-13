import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def linear_glide_path(t, T):
    return 100 - (100 / T) * t

def convex_glide_path(t, T, steepness):
    return 100 * np.power(1 - t / T, steepness)

def concave_glide_path(t, T, steepness):
    return 100 - 100 * np.power(t / T, steepness)

def s_shape_glide_path(t, T, s_steepness):
    return 100 / (1 + np.exp(-s_steepness * (t - T / 2)))

def parabolic_glide_path(t, T, peak_time, parabolic_steepness):
    return 100 - parabolic_steepness * (t - peak_time) ** 2

st.title("Risk Glide Paths Visualization")

# Create side-by-side columns
left_column, right_column = st.columns(2)

with left_column:
    T = st.slider("Total Time Period", 50, 200, 100)
    steepness = st.slider("Steepness for Convex and Concave Paths", 1.0, 5.0, 3.0)
    peak_time = st.slider("Peak Time for Parabolic Path", 10, T-10, 50)
    parabolic_steepness = st.slider("Steepness for Parabolic Path", 0.001, 0.1, 0.01)
    s_steepness = st.slider("Steepness for S-Shape Path", 0.01, 0.5, 0.1)

t = np.linspace(0, T, 500)
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(t, linear_glide_path(t, T), label="Linear", color="red")
ax.plot(t, convex_glide_path(t, T, steepness), label="Convex", color="green")
ax.plot(t, concave_glide_path(t, T, steepness), label="Concave", color="blue")
ax.plot(t, s_shape_glide_path(t, T, s_steepness), label="S-Shape", color="magenta")
ax.plot(t, parabolic_glide_path(t, T, peak_time, parabolic_steepness), label="Parabolic", color="cyan")

ax.set_title("Risk Glide Paths")
ax.set_xlabel("Time (t)")
ax.set_ylabel("Risk (%)")
ax.legend()
ax.grid(True)

with right_column:
    st.pyplot(fig)
