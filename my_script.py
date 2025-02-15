#import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import altair as alt

# Load data
df = pd.read_csv('vehicles_us.csv')

df.info()
