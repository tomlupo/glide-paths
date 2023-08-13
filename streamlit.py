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
    return 100 - 100 / (1 + np.exp(-s_steepness * (t - T / 2)))

def parabolic_glide_path(t, T, peak_time
