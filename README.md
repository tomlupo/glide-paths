# Glide Paths

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io)

Interactive visualization tool for comparing investment risk glide path strategies — commonly used in retirement planning and target-date funds.

![Screenshot](screenshot.png)
<!-- Add a screenshot of your app here -->

## Features

Compare 5 different mathematical models for managing risk over time:

| Model | Description |
|-------|-------------|
| **Linear** | Constant, steady risk reduction |
| **Convex** | Aggressive early reduction, slower later |
| **Concave** | Slower early, aggressive near the end |
| **S-Shape** | Sigmoid curve with gradual acceleration |
| **Parabolic** | Quadratic curve centered on a peak time |

Adjust parameters in real-time:
- Total time period
- Steepness for convex/concave paths
- Peak timing for parabolic curves
- S-shape steepness

## Installation

```bash
git clone https://github.com/tomlupo/glide_paths.git
cd glide_paths
uv sync
```

## Usage

```bash
uv run streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## License

MIT
