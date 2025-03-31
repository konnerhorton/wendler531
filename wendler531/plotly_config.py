import plotly.graph_objects as go
import plotly.io as pio

# ===== Set Default Template =====
pio.templates.default = "plotly_white"  # or "seaborn", "ggplot2", etc.

# # ===== Customize Layout =====
# layout = go.Layout(
#     font=dict(family="Arial", size=12, color="black"),
#     title=dict(x=0.5, xanchor="center"),  # Center titles by default
#     margin=dict(l=50, r=50, b=50, t=50, pad=10),
#     plot_bgcolor="white",
#     paper_bgcolor="white",
#     xaxis=dict(showgrid=True, gridcolor="lightgrey"),
#     yaxis=dict(showgrid=True, gridcolor="lightgrey"),
# )
