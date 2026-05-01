import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from utils.predictor import predict_calories
from utils.macro_calculator import calculate_macros
from utils.diet_recommender import recommend_meals
from utils.workout_recommender import recommend_workout
from tracking.progress_tracker import add_entry, load_log, get_trend

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FitForge — AI Fitness Planner",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Plus+Jakarta+Sans:wght@300;400;500;600&display=swap');

/* Reset & base */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2.5rem 4rem 2.5rem; max-width: 1200px; }

/* Background */
.stApp {
    background: #0a0a0f;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #0f0f18 !important;
    border-right: 1px solid #1e1e2e;
}
[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1.2rem;
}

/* Typography */
h1, h2, h3 {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
}

/* Sidebar label styling */
[data-testid="stSidebar"] label {
    color: #6b6b8a !important;
    font-size: 0.72rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}

/* Input fields */
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #16161f !important;
    border: 1px solid #2a2a3d !important;
    border-radius: 8px !important;
    color: #e8e8f0 !important;
}

/* Slider */
.stSlider [data-baseweb="slider"] {
    margin-top: 0.2rem;
}
.stSlider [data-baseweb="thumb"] {
    background: #c8f542 !important;
    border: none !important;
    width: 16px !important;
    height: 16px !important;
}
.stSlider [data-baseweb="track-background"] {
    background: #1e1e2e !important;
}
.stSlider [data-baseweb="track-foreground"] {
    background: #c8f542 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    border-bottom: 1px solid #1e1e2e;
    gap: 0;
    padding-bottom: 0;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: #6b6b8a;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-size: 0.82rem;
    font-weight: 500;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    padding: 0.7rem 1.4rem;
    border: none;
    border-bottom: 2px solid transparent;
}
.stTabs [aria-selected="true"] {
    color: #c8f542 !important;
    border-bottom: 2px solid #c8f542 !important;
    background: transparent !important;
}

/* Metric cards */
[data-testid="stMetric"] {
    background: #0f0f18;
    border: 1px solid #1e1e2e;
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
}
[data-testid="stMetricLabel"] {
    color: #6b6b8a !important;
    font-size: 0.72rem !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
[data-testid="stMetricValue"] {
    color: #e8e8f0 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
}
[data-testid="stMetricDelta"] svg { display: none; }
[data-testid="stMetricDelta"] > div {
    color: #c8f542 !important;
    font-size: 0.78rem !important;
}

/* Buttons */
.stButton > button {
    background: #c8f542 !important;
    color: #0a0a0f !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.05em !important;
    padding: 0.65rem 1.4rem !important;
    width: 100% !important;
    transition: all 0.2s ease !important;
}
.stButton > button:hover {
    background: #d4f75a !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(200, 245, 66, 0.25) !important;
}

/* Divider */
hr { border-color: #1e1e2e !important; }

/* Dataframe */
[data-testid="stDataFrame"] {
    border: 1px solid #1e1e2e !important;
    border-radius: 10px !important;
    overflow: hidden;
}

/* Expander */
.streamlit-expanderHeader {
    background: #0f0f18 !important;
    border: 1px solid #1e1e2e !important;
    border-radius: 8px !important;
    color: #e8e8f0 !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.88rem !important;
}
.streamlit-expanderContent {
    background: #0c0c15 !important;
    border: 1px solid #1e1e2e !important;
    border-top: none !important;
    color: #9090a8 !important;
}

/* Info/success boxes */
[data-testid="stInfo"] {
    background: #0f1a2e !important;
    border: 1px solid #1a3a5c !important;
    border-radius: 10px !important;
    color: #7ab3e0 !important;
}
[data-testid="stSuccess"] {
    background: #0d1f0d !important;
    border: 1px solid #1a3d1a !important;
    border-radius: 10px !important;
    color: #6dba6d !important;
}

/* Progress bar */
.stProgress > div > div {
    background: #c8f542 !important;
    border-radius: 4px !important;
}
.stProgress > div {
    background: #1e1e2e !important;
    border-radius: 4px !important;
}

/* Number input */
[data-testid="stNumberInput"] input {
    background: #16161f !important;
    border: 1px solid #2a2a3d !important;
    border-radius: 8px !important;
    color: #e8e8f0 !important;
}

/* Radio */
.stRadio label { color: #9090a8 !important; font-size: 0.88rem !important; }
.stRadio [data-baseweb="radio"] > div:first-child {
    border-color: #2a2a3d !important;
    background: transparent !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0f; }
::-webkit-scrollbar-thumb { background: #2a2a3d; border-radius: 4px; }

</style>
""", unsafe_allow_html=True)


# ─── HELPER: Section header ───────────────────────────────────────────────────
def section_header(title, subtitle=""):
    st.markdown(f"""
    <div style="margin: 2rem 0 1.2rem 0;">
        <p style="color:#6b6b8a;font-size:0.7rem;letter-spacing:0.12em;text-transform:uppercase;
                  margin:0 0 0.3rem 0;font-family:'Plus Jakarta Sans',sans-serif;">
            {'— ' + subtitle if subtitle else ''}
        </p>
        <h2 style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.4rem;
                   font-weight:700;margin:0;letter-spacing:-0.01em;">
            {title}
        </h2>
    </div>
    """, unsafe_allow_html=True)


def stat_card(label, value, unit="", accent=False):
    color = "#c8f542" if accent else "#e8e8f0"
    return f"""
    <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;
                padding:1.2rem 1.4rem;height:100%;">
        <p style="color:#6b6b8a;font-size:0.68rem;letter-spacing:0.1em;
                  text-transform:uppercase;margin:0 0 0.5rem 0;font-family:'Plus Jakarta Sans',sans-serif;">
            {label}
        </p>
        <p style="color:{color};font-family:'Plus Jakarta Sans',sans-serif;font-size:1.9rem;
                  font-weight:800;margin:0;line-height:1;">
            {value}<span style="font-size:0.9rem;font-weight:500;color:#6b6b8a;margin-left:4px;">{unit}</span>
        </p>
    </div>
    """


def pill(text, color="#c8f542"):
    return f"""<span style="background:{color}18;color:{color};border:1px solid {color}33;
               border-radius:20px;padding:0.2rem 0.7rem;font-size:0.72rem;
               font-weight:600;letter-spacing:0.05em;font-family:'Plus Jakarta Sans',sans-serif;">{text}</span>"""


# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding:0.5rem 0 1.5rem 0;border-bottom:1px solid #1e1e2e;margin-bottom:1.5rem;">
        <p style="color:#6b6b8a;font-size:0.65rem;letter-spacing:0.15em;
                  text-transform:uppercase;margin:0 0 0.3rem 0;">FitForge</p>
        <h1 style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.3rem;
                   font-weight:800;margin:0;letter-spacing:-0.02em;">Your Profile</h1>
    </div>
    """, unsafe_allow_html=True)

    name     = st.text_input("NAME", "Satwik", label_visibility="visible")
    age      = st.slider("AGE", 16, 70, 20)
    weight   = st.number_input("WEIGHT (KG)", 40.0, 150.0, 64.0, step=0.5)
    height   = st.number_input("HEIGHT (CM)", 140.0, 210.0, 170.5, step=0.5)
    gender   = st.radio("GENDER", ["Male", "Female"], horizontal=True)

    activity = st.selectbox("ACTIVITY LEVEL", [
        'Sedentary (little/no exercise)',
        'Light (1-3 days/week)',
        'Moderate (3-5 days/week)',
        'Active (6-7 days/week)',
        'Very Active (athlete)'
    ])

    goal = st.selectbox("PRIMARY GOAL", ["Fat Loss", "Muscle Gain", "Maintenance"])

    st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)
    st.markdown("<p style='color:#6b6b8a;font-size:0.72rem;letter-spacing:0.08em;text-transform:uppercase;margin:0 0 0.4rem 0;'>DIET PREFERENCE</p>", unsafe_allow_html=True)
    diet_type = st.radio("DIET PREFERENCE", ["Non-Vegetarian", "Vegetarian"], horizontal=True, label_visibility="collapsed")

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    run = st.button("GENERATE PLAN →")

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)


# ─── HERO HEADER ──────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="padding:2.5rem 0 1rem 0;border-bottom:1px solid #1e1e2e;margin-bottom:0.5rem;">
    <div style="display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:1rem;">
        <div>
            <p style="color:#6b6b8a;font-size:0.7rem;letter-spacing:0.15em;
                      text-transform:uppercase;margin:0 0 0.5rem 0;
                      font-family:'Plus Jakarta Sans',sans-serif;">
                AI-Powered Fitness Intelligence
            </p>
            <h1 style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:2.8rem;
                       font-weight:900;margin:0;letter-spacing:-0.04em;line-height:1;">
                Fit<span style="color:#c8f542;">Forge</span>
            </h1>
        </div>
        <p style="color:#6b6b8a;font-size:0.82rem;margin:0;font-family:'Plus Jakarta Sans',sans-serif;">
            Personalized · Science-backed · Goal-driven
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ─── TABS ─────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "OVERVIEW", "NUTRITION", "TRAINING", "PROGRESS", "INSIGHTS"
])

# ─── COMPUTE ──────────────────────────────────────────────────────────────────
if run:
    base_cal = predict_calories(age, weight, height, gender, activity)
    macros   = calculate_macros(base_cal, goal, weight)
    meals    = recommend_meals(goal, diet_type)
    workout  = recommend_workout(goal)
    adj_cal  = macros['adjusted_calories']
    bmi      = weight / ((height / 100) ** 2)

    if bmi < 18.5:
        bmi_label, bmi_color = "Underweight", "#e07a5f"
    elif bmi < 25:
        bmi_label, bmi_color = "Healthy", "#c8f542"
    elif bmi < 30:
        bmi_label, bmi_color = "Overweight", "#f2cc8f"
    else:
        bmi_label, bmi_color = "Obese", "#e07a5f"

    deficit = adj_cal - base_cal

    # ── TAB 1: OVERVIEW ───────────────────────────────────────────────────────
    with tab1:
        st.markdown(f"""
        <div style="padding:1.2rem 0 0.5rem 0;">
            <p style="color:#6b6b8a;font-size:0.75rem;margin:0 0 0.2rem 0;font-family:'Plus Jakarta Sans',sans-serif;">Welcome back,</p>
            <h2 style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.8rem;
                       font-weight:800;margin:0;">{name} &nbsp;
                <span style="color:#c8f542">/</span>&nbsp;
                <span style="color:#6b6b8a;font-size:1.1rem;font-weight:500;">{goal}</span>
            </h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

        # Top stat row
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.markdown(stat_card("Base TDEE", f"{base_cal:,}", "kcal"), unsafe_allow_html=True)
        c2.markdown(stat_card("Daily Target", f"{adj_cal:,}", "kcal", accent=True), unsafe_allow_html=True)
        c3.markdown(stat_card("Protein Target", f"{macros['protein_g']}", "g"), unsafe_allow_html=True)
        c4.markdown(stat_card("BMI", f"{bmi:.1f}", bmi_label), unsafe_allow_html=True)
        c5.markdown(stat_card("Deficit/Surplus", f"{deficit:+}", "kcal"), unsafe_allow_html=True)

        st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

        # Two column layout
        col_left, col_right = st.columns([1.2, 1])

        with col_left:
            section_header("Macro Distribution", "Calorie breakdown")

            fig, ax = plt.subplots(figsize=(5.5, 4), facecolor='none')
            sizes  = [macros['protein_g']*4, macros['fat_g']*9, macros['carbs_g']*4]
            colors = ['#c8f542', '#7ab3e0', '#b07ae0']
            labels = ['Protein', 'Fat', 'Carbs']
            wedges, texts, autotexts = ax.pie(
                sizes, labels=None, colors=colors,
                autopct='%1.0f%%', startangle=90,
                wedgeprops=dict(width=0.55, edgecolor='#0a0a0f', linewidth=2),
                pctdistance=0.78
            )
            for at in autotexts:
                at.set_color('#0a0a0f')
                at.set_fontsize(10)
                at.set_fontweight('bold')

            # Center text
            ax.text(0, 0.08, f"{adj_cal:,}", ha='center', va='center',
                    color='#e8e8f0', fontsize=18, fontweight='bold')
            ax.text(0, -0.18, 'kcal/day', ha='center', va='center',
                    color='#6b6b8a', fontsize=9)

            legend_patches = [mpatches.Patch(color=colors[i], label=f"{labels[i]}  {sizes[i]:.0f} kcal") for i in range(3)]
            ax.legend(handles=legend_patches, loc='lower center',
                      bbox_to_anchor=(0.5, -0.12), ncol=3,
                      frameon=False, fontsize=9,
                      labelcolor='#9090a8')
            fig.tight_layout(pad=0)
            st.pyplot(fig, use_container_width=True)
            plt.close()

        with col_right:
            section_header("Daily Targets", "Per macro")

            macros_data = [
                ("Protein", macros['protein_g'], 200, "#c8f542", f"{weight*2:.0f}g optimal for {goal}"),
                ("Carbohydrates", macros['carbs_g'], 350, "#7ab3e0", "Primary energy source"),
                ("Fats", macros['fat_g'], 100, "#b07ae0", "Hormonal & joint health"),
            ]

            for macro_name, grams, max_g, color, note in macros_data:
                pct = min(grams / max_g, 1.0)
                st.markdown(f"""
                <div style="margin-bottom:1.2rem;">
                    <div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:0.4rem;">
                        <span style="color:#e8e8f0;font-size:0.88rem;font-weight:500;">{macro_name}</span>
                        <span style="color:{color};font-family:'Plus Jakarta Sans',sans-serif;
                                     font-size:1.1rem;font-weight:700;">{grams}g</span>
                    </div>
                    <div style="background:#1e1e2e;border-radius:4px;height:6px;overflow:hidden;">
                        <div style="background:{color};width:{pct*100:.0f}%;height:100%;
                                    border-radius:4px;transition:width 0.5s ease;"></div>
                    </div>
                    <p style="color:#6b6b8a;font-size:0.7rem;margin:0.3rem 0 0 0;">{note}</p>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

            # BMI gauge
            st.markdown(f"""
            <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;padding:1rem 1.2rem;">
                <div style="display:flex;justify-content:space-between;align-items:center;">
                    <div>
                        <p style="color:#6b6b8a;font-size:0.68rem;letter-spacing:0.1em;
                                  text-transform:uppercase;margin:0 0 0.2rem 0;">Body Mass Index</p>
                        <p style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.6rem;
                                  font-weight:800;margin:0;">{bmi:.1f}</p>
                    </div>
                    <span style="background:{bmi_color}18;color:{bmi_color};border:1px solid {bmi_color}33;
                                 border-radius:20px;padding:0.3rem 0.9rem;font-size:0.78rem;font-weight:600;">
                        {bmi_label}
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── TAB 2: NUTRITION ──────────────────────────────────────────────────────
    with tab2:
        section_header("Nutrition Plan", f"{diet_type} · Optimized for {goal}")

        st.markdown(f"""
        <div style="background:#0f1a0a;border:1px solid #1e3d1e;border-radius:12px;
                    padding:1rem 1.4rem;margin-bottom:1.5rem;display:flex;
                    justify-content:space-between;align-items:center;">
            <div>
                <p style="color:#6dba6d;font-size:0.72rem;letter-spacing:0.1em;
                          text-transform:uppercase;margin:0 0 0.2rem 0;">Daily Calorie Target</p>
                <p style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.4rem;
                          font-weight:700;margin:0;">{adj_cal:,} kcal
                    <span style="color:#6dba6d;font-size:0.9rem;font-weight:400;margin-left:8px;">
                        ({deficit:+d} from maintenance)
                    </span>
                </p>
            </div>
            <div style="text-align:right;">
                <p style="color:#6b6b8a;font-size:0.72rem;margin:0 0 0.2rem 0;">Strategy</p>
                <p style="color:#c8f542;font-size:0.9rem;font-weight:600;margin:0;">
                    {'Caloric Deficit' if goal == 'Fat Loss' else 'Caloric Surplus' if goal == 'Muscle Gain' else 'Maintenance'}
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        meal_cols_top = st.columns(2)
        meals_to_show = meals[:4]
        for i, m in enumerate(meals_to_show):
            with meal_cols_top[i % 2]:
                cal_pct = m['cal'] / adj_cal * 100
                st.markdown(f"""
                <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;
                            padding:1.2rem 1.4rem;margin-bottom:1rem;">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;">
                        <div>
                            <p style="color:#6b6b8a;font-size:0.65rem;letter-spacing:0.1em;
                                      text-transform:uppercase;margin:0 0 0.2rem 0;">{m['meal']}</p>
                            <p style="color:#e8e8f0;font-size:0.92rem;font-weight:500;
                                      margin:0;">{m['option']}</p>
                        </div>
                        <div style="text-align:right;flex-shrink:0;margin-left:1rem;">
                            <p style="color:#c8f542;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.2rem;
                                      font-weight:700;margin:0;">{m['cal']}</p>
                            <p style="color:#6b6b8a;font-size:0.65rem;margin:0;">kcal</p>
                        </div>
                    </div>
                    <div style="background:#1e1e2e;border-radius:3px;height:3px;">
                        <div style="background:#c8f542;width:{cal_pct:.0f}%;height:100%;border-radius:3px;"></div>
                    </div>
                    <p style="color:#6b6b8a;font-size:0.65rem;margin:0.3rem 0 0 0;">
                        {cal_pct:.0f}% of daily target
                    </p>
                </div>
                """, unsafe_allow_html=True)

        # 5th meal full width if exists
        if len(meals) == 5:
            m = meals[4]
            cal_pct = m['cal'] / adj_cal * 100
            st.markdown(f"""
            <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;
                        padding:1.2rem 1.4rem;margin-bottom:1rem;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.8rem;">
                    <div>
                        <p style="color:#6b6b8a;font-size:0.65rem;letter-spacing:0.1em;
                                  text-transform:uppercase;margin:0 0 0.2rem 0;">{m['meal']}</p>
                        <p style="color:#e8e8f0;font-size:0.92rem;font-weight:500;margin:0;">{m['option']}</p>
                    </div>
                    <div style="text-align:right;flex-shrink:0;margin-left:1rem;">
                        <p style="color:#c8f542;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.2rem;
                                  font-weight:700;margin:0;">{m['cal']}</p>
                        <p style="color:#6b6b8a;font-size:0.65rem;margin:0;">kcal</p>
                    </div>
                </div>
                <div style="background:#1e1e2e;border-radius:3px;height:3px;">
                    <div style="background:#c8f542;width:{cal_pct:.0f}%;height:100%;border-radius:3px;"></div>
                </div>
                <p style="color:#6b6b8a;font-size:0.65rem;margin:0.3rem 0 0 0;">
                    {cal_pct:.0f}% of daily target
                </p>
            </div>
            """, unsafe_allow_html=True)

        total_meal_cal = sum(m['cal'] for m in meals)
        remaining = adj_cal - total_meal_cal
        st.markdown(f"""
        <div style="background:#16161f;border:1px solid #2a2a3d;border-radius:10px;
                    padding:1rem 1.4rem;display:flex;justify-content:space-between;align-items:center;">
            <span style="color:#9090a8;font-size:0.85rem;">Plan total</span>
            <span style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.1rem;font-weight:700;">
                {total_meal_cal} kcal
                <span style="color:#6b6b8a;font-size:0.8rem;font-weight:400;">
                    / {adj_cal} target &nbsp;·&nbsp; {remaining:+d} remaining
                </span>
            </span>
        </div>
        """, unsafe_allow_html=True)

    # ── TAB 3: TRAINING ───────────────────────────────────────────────────────
    with tab3:
        section_header("Training Plan", workout['plan'])

        st.markdown(f"""
        <div style="background:linear-gradient(135deg,#0f1a0f,#0a1200);
                    border:1px solid #1e3d1e;border-radius:12px;
                    padding:1.2rem 1.6rem;margin-bottom:1.5rem;">
            <p style="color:#6dba6d;font-size:0.7rem;letter-spacing:0.1em;
                      text-transform:uppercase;margin:0 0 0.3rem 0;">Weekly Split</p>
            <h3 style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.3rem;
                       font-weight:700;margin:0 0 0.5rem 0;">{workout['plan']}</h3>
            <p style="color:#6b6b8a;font-size:0.82rem;margin:0;">
                {'High-intensity intervals combined with strength work to maximize fat oxidation.' if goal == 'Fat Loss'
                 else 'Progressive overload program designed to build muscle mass systematically.' if goal == 'Muscle Gain'
                 else 'Balanced program to maintain fitness and support overall health.'}
            </p>
        </div>
        """, unsafe_allow_html=True)

        day_colors = {
            'Monday': '#c8f542', 'Tuesday': '#7ab3e0', 'Wednesday': '#6b6b8a',
            'Thursday': '#c8f542', 'Friday': '#7ab3e0', 'Saturday': '#b07ae0', 'Sunday': '#6b6b8a'
        }
        intensity = {
            'Monday': 85, 'Tuesday': 75, 'Wednesday': 30,
            'Thursday': 85, 'Friday': 70, 'Saturday': 60, 'Sunday': 0
        }

        for d in workout['days']:
            color = day_colors.get(d['day'], '#c8f542')
            intens = intensity.get(d['day'], 50)
            is_rest = 'Rest' in d['focus'] or intens == 0
            focus = d.get('focus', '')

            st.markdown(f"""
            <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:10px;
                        padding:1rem 1.4rem;margin-bottom:0.6rem;
                        {'opacity:0.45;' if is_rest else ''}">
                <div style="display:flex;align-items:flex-start;gap:1.2rem;">
                    <div style="width:70px;flex-shrink:0;padding-top:2px;">
                        <p style="color:{color};font-size:0.68rem;font-weight:700;
                                  letter-spacing:0.08em;text-transform:uppercase;margin:0;">{d['day'][:3]}</p>
                    </div>
                    <div style="flex:1;">
                        <p style="color:#e8e8f0;font-size:0.88rem;font-weight:600;margin:0 0 0.3rem 0;">
                            {focus}
                        </p>
                        <p style="color:#6b6b8a;font-size:0.78rem;margin:0;line-height:1.6;">
                            {d['workout']}
                        </p>
                    </div>
                    <div style="width:100px;flex-shrink:0;text-align:right;">
                        <div style="background:#1e1e2e;border-radius:3px;height:4px;margin-bottom:4px;">
                            <div style="background:{color};width:{intens}%;height:100%;border-radius:3px;"></div>
                        </div>
                        <p style="color:#6b6b8a;font-size:0.62rem;margin:0;">
                            {'Rest' if is_rest else f'{intens}% intensity'}
                        </p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("""
        <div style="margin-top:1rem;padding:1rem 1.4rem;background:#0f0f18;
                    border:1px solid #1e1e2e;border-radius:10px;">
            <p style="color:#c8f542;font-size:0.78rem;font-weight:600;margin:0 0 0.3rem 0;">
                ⚡ Progressive Overload Protocol
            </p>
            <p style="color:#6b6b8a;font-size:0.8rem;margin:0;line-height:1.5;">
                Increase weight by 2.5–5kg or reps by 2–3 every week on compound lifts.
                Track each session. Consistency over intensity.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ── TAB 4: PROGRESS ───────────────────────────────────────────────────────
    with tab4:
        section_header("Progress Tracker", "Log & monitor your weight")

        col_log, col_chart = st.columns([1, 2])

        with col_log:
            st.markdown("""
            <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1rem;">
                <p style="color:#6b6b8a;font-size:0.7rem;letter-spacing:0.1em;text-transform:uppercase;margin:0 0 1rem 0;">
                    Log Today's Weight
                </p>
            """, unsafe_allow_html=True)

            log_weight = st.number_input("Weight (kg)", 40.0, 150.0, float(weight), step=0.1, label_visibility="collapsed")
            if st.button("LOG WEIGHT →"):
                add_entry(log_weight)
                st.success(f"Logged {log_weight} kg")

            st.markdown("</div>", unsafe_allow_html=True)

            log = load_log()
            if log:
                trend = get_trend(log)
                entries = len(log)
                first_w = log[0]['weight']
                last_w  = log[-1]['weight']
                total_change = last_w - first_w

                st.markdown(f"""
                <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;padding:1.2rem 1.4rem;">
                    <p style="color:#6b6b8a;font-size:0.68rem;letter-spacing:0.1em;text-transform:uppercase;margin:0 0 1rem 0;">Stats</p>
                    <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.8rem;">
                        <div>
                            <p style="color:#6b6b8a;font-size:0.65rem;margin:0 0 0.2rem 0;">Entries</p>
                            <p style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.3rem;font-weight:700;margin:0;">{entries}</p>
                        </div>
                        <div>
                            <p style="color:#6b6b8a;font-size:0.65rem;margin:0 0 0.2rem 0;">Change</p>
                            <p style="color:{'#c8f542' if total_change < 0 else '#e07a5f'};font-family:'Plus Jakarta Sans',sans-serif;font-size:1.3rem;font-weight:700;margin:0;">{total_change:+.1f}kg</p>
                        </div>
                        <div>
                            <p style="color:#6b6b8a;font-size:0.65rem;margin:0 0 0.2rem 0;">Current</p>
                            <p style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.3rem;font-weight:700;margin:0;">{last_w}kg</p>
                        </div>
                        <div>
                            <p style="color:#6b6b8a;font-size:0.65rem;margin:0 0 0.2rem 0;">Trend</p>
                            <p style="color:#7ab3e0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.3rem;font-weight:700;margin:0;">{trend:+.2f if trend else 'N/A'}</p>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

        with col_chart:
            log = load_log()
            if log and len(log) > 1:
                df_log = pd.DataFrame(log)
                fig, ax = plt.subplots(figsize=(7, 4), facecolor='none')
                ax.set_facecolor('none')
                x = range(len(df_log))
                ax.fill_between(x, df_log['weight'], alpha=0.15, color='#c8f542')
                ax.plot(x, df_log['weight'], color='#c8f542', linewidth=2, marker='o',
                        markersize=4, markerfacecolor='#c8f542', markeredgecolor='#0a0a0f', markeredgewidth=1.5)
                # Trend line
                if len(df_log) > 2:
                    z = np.polyfit(list(x), df_log['weight'], 1)
                    p = np.poly1d(z)
                    ax.plot(x, p(list(x)), '--', color='#7ab3e0', linewidth=1, alpha=0.6, label='Trend')
                ax.set_xticks(list(x))
                ax.set_xticklabels([d['date'][-5:] for d in log], color='#6b6b8a', fontsize=8, rotation=30)
                ax.tick_params(axis='y', colors='#6b6b8a', labelsize=9)
                ax.spines['bottom'].set_color('#1e1e2e')
                ax.spines['left'].set_color('#1e1e2e')
                ax.spines['top'].set_visible(False)
                ax.spines['right'].set_visible(False)
                ax.yaxis.set_label_text('kg', color='#6b6b8a', fontsize=9)
                ax.grid(axis='y', color='#1e1e2e', linewidth=0.5)
                fig.tight_layout(pad=0.5)
                st.pyplot(fig, use_container_width=True)
                plt.close()
            elif log and len(log) == 1:
                st.info("Log at least 2 entries to see your progress chart.")
            else:
                st.markdown("""
                <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;
                            padding:3rem;text-align:center;">
                    <p style="color:#6b6b8a;font-size:0.88rem;margin:0;">
                        No data yet. Start logging your weight daily to track progress.
                    </p>
                </div>
                """, unsafe_allow_html=True)

    # ── TAB 5: INSIGHTS ───────────────────────────────────────────────────────
    with tab5:
        section_header("AI Insights", "Your personal analysis")

        weekly_burn = (base_cal - adj_cal) * 7 if goal == 'Fat Loss' else 0
        weekly_loss = weekly_burn / 7700 if weekly_burn > 0 else 0
        weeks_to_5kg = 5 / weekly_loss if weekly_loss > 0 else 0

        insights = []
        if goal == 'Fat Loss':
            insights = [
                ("🎯", "Caloric Strategy", f"A {abs(deficit)} kcal daily deficit creates a weekly energy gap of ~{abs(deficit)*7:,} kcal, targeting ~{weekly_loss:.2f} kg/week of fat loss."),
                ("💪", "Protein Priority", f"At {macros['protein_g']}g/day ({macros['protein_g']/weight:.1f}g/kg), you'll preserve muscle mass during the deficit — critical for long-term results."),
                ("⏱️", "Timeline Estimate", f"At this rate, losing 5kg would take approximately {weeks_to_5kg:.0f} weeks. Sustainable, realistic fat loss."),
                ("🔥", "Metabolism Note", f"Your TDEE of {base_cal:,} kcal reflects your current metabolic rate. Recalculate every 4–6 weeks as you lose weight."),
            ]
        elif goal == 'Muscle Gain':
            insights = [
                ("🎯", "Surplus Strategy", f"A +{deficit} kcal surplus provides the energy needed for muscle protein synthesis without excessive fat gain."),
                ("💪", "Protein Synthesis", f"{macros['protein_g']}g protein/day ({macros['protein_g']/weight:.1f}g/kg) sits in the optimal range for muscle hypertrophy."),
                ("📈", "Expected Gains", f"Natural muscle gain averages 0.5–1kg/month for trained individuals. Focus on strength progression over scale weight."),
                ("🔬", "Carb Timing", f"{macros['carbs_g']}g carbs fuels your training sessions. Consume 60–80g around workouts for optimal performance."),
            ]
        else:
            insights = [
                ("⚖️", "Energy Balance", f"Your {base_cal:,} kcal target matches your energy expenditure — ideal for maintaining current body composition."),
                ("💪", "Protein Foundation", f"{macros['protein_g']}g protein/day maintains muscle mass and supports recovery from training."),
                ("🏃", "Activity Focus", f"At {activity.split('(')[0].strip()} level, consistent training will sustain your metabolism and fitness base."),
                ("📊", "Health Markers", f"BMI of {bmi:.1f} ({bmi_label}) — focus on body composition over scale weight for health outcomes."),
            ]

        for icon, title, body in insights:
            st.markdown(f"""
            <div style="background:#0f0f18;border:1px solid #1e1e2e;border-radius:12px;
                        padding:1.2rem 1.4rem;margin-bottom:0.8rem;
                        display:flex;gap:1.2rem;align-items:flex-start;">
                <span style="font-size:1.4rem;flex-shrink:0;">{icon}</span>
                <div>
                    <p style="color:#c8f542;font-size:0.78rem;font-weight:600;
                              letter-spacing:0.05em;margin:0 0 0.3rem 0;">{title.upper()}</p>
                    <p style="color:#9090a8;font-size:0.85rem;margin:0;line-height:1.6;">{body}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        # Quick profile summary
        st.markdown(f"""
        <div style="background:#0a1200;border:1px solid #1e3d00;border-radius:12px;padding:1.2rem 1.6rem;">
            <p style="color:#6dba6d;font-size:0.7rem;letter-spacing:0.1em;
                      text-transform:uppercase;margin:0 0 0.8rem 0;">Profile Summary</p>
            <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;">
                {''.join([f'<div><p style="color:#6b6b8a;font-size:0.65rem;margin:0 0 0.2rem 0;">{l}</p><p style="color:#e8e8f0;font-size:0.95rem;font-weight:600;margin:0;">{v}</p></div>'
                for l,v in [('Age',f'{age} yrs'),('Weight',f'{weight} kg'),('Height',f'{height} cm'),('Activity',activity.split("(")[0].strip())]])}
            </div>
        </div>
        """, unsafe_allow_html=True)

else:
    # ── EMPTY STATE ───────────────────────────────────────────────────────────
    with tab1:
        st.markdown("""
        <div style="height:50vh;display:flex;flex-direction:column;
                    align-items:center;justify-content:center;text-align:center;">
            <div style="width:64px;height:64px;background:#1e1e2e;border-radius:16px;
                        display:flex;align-items:center;justify-content:center;
                        font-size:1.8rem;margin-bottom:1.2rem;">⚡</div>
            <h2 style="color:#e8e8f0;font-family:'Plus Jakarta Sans',sans-serif;font-size:1.4rem;
                       font-weight:700;margin:0 0 0.5rem 0;">Ready to build your plan</h2>
            <p style="color:#6b6b8a;font-size:0.88rem;max-width:320px;margin:0;line-height:1.6;">
                Fill in your profile in the sidebar and hit <strong style="color:#c8f542;">Generate Plan</strong>
                to get your AI-powered fitness roadmap.
            </p>
        </div>
        """, unsafe_allow_html=True)