import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def linear_glide_path(t, T):
    return 100 - (100 / T) * t

def convex_glide_path(t, T, steepness):
    return 100 * np.power(1 - t / T, steepness)

def concave_glide_path(t, T, steepness):
    return 100 * np.power(t / T, steepness)

def s_shape_glide_path(t, T, s_steepness):
    return 100 / (1 + np.exp(s_steepness * (T / 2 - t)))

def parabolic_glide_path(t, T, peak_time, parabolic_steepness):
    a = -parabolic_steepness / (peak_time * (peak_time - T))
    return a * (t - peak_time) ** 2

def plot_glide_paths(T, steepness, peak_time, parabolic_steepness, s_steepness):
    t = np.linspace(0, T, 500)
    
    plt.figure(figsize=(10, 6))
    
    plt.plot(t, linear_glide_path(t, T), label="Linear", color="red")
    plt.plot(t, convex_glide_path(t, T, steepness), label="Convex", color="green")
    plt.plot(t, concave_glide_path(t, T, steepness), label="Concave", color="blue")
    plt.plot(t, s_shape_glide_path(t, T, s_steepness), label="S-Shape", color="magenta")
    plt.plot(t, parabolic_glide_path(t, T, peak_time, parabolic_steepness), label="Parabolic", color="cyan")
    
    plt.title("Risk Glide Paths")
    plt.xlabel("Time (t)")
    plt.ylabel("Risk (%)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    st.pyplot()

st.title("Risk Glide Paths Visualization")

T = st.slider("Total Time Period", 50, 200, 100)
steepness = st.slider("Steepness for Convex and Concave Paths", 1.0, 5.0, 3.0)
peak_time = st.slider("Peak Time for Parabolic Path", 10, T-10, 50)
parabolic_steepness = st.slider("Steepness for Parabolic Path", 1.0, 5.0, 2.0)
s_steepness = st.slider("Steepness for S-Shape Path", 0.01, 0.5, 0.1)

plot_glide_paths(T, steepness, peak_time, parabolic_steepness, s_steepness)
