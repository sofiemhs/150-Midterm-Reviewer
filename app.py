import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="C&EE 150 Study Guide", layout="wide", initial_sidebar_state="expanded")

# --- Sidebar ---
st.sidebar.title("💧 C&EE 150: Intro to Hydrology")
page = st.sidebar.radio("Navigation", [
    "Welcome & Overview",
    "Chapter 1: Hydrologic Cycle",
    "Chapter 2: Atmospheric Thermodynamics",
    "Chapter 3: Radiation Processes",
    "Chapter 4: Atmospheric Circulation",
    "Chapter 5: Precipitation Processes",
    "Chapter 6: Snow Processes",
    "Homework Solutions Archive",
    "Practice Midterms"
])

# --- Welcome ---
if page == "Welcome & Overview":
    st.title("💧 C&EE 150: Comprehensive Midterm Study Guide")
    st.markdown("""
    This interactive guide covers Chapters 1-6 of Margulis's *Introduction to Hydrology* (2017a Edition), integrating all equations, homework solutions, and sample midterms[cite: 90, 91].
    
    ### Core Framework
    * **Water Budget:** Precipitation supplies water. Evaporation, sublimation, and runoff remove it. Storage changes balance the difference[cite: 91].
    * **Energy Budget:** Radiation, sensible heat, latent heat, and conduction determine if a surface warms, cools, evaporates, or melts[cite: 91].
    """)

# --- Chapter 1 ---
elif page == "Chapter 1: Hydrologic Cycle":
    st.header("Chapter 1: The Hydrologic Cycle & Mass Balance")
    
    st.subheader("Global Reservoirs")
    st.markdown("""
    * **Oceans:** 97.2% of global water (residence time ~2500 years)[cite: 92, 94].
    * **Ice caps & glaciers:** 2.1%[cite: 92].
    * **Groundwater (Near-surface):** 0.31% (residence time ~8 years)[cite: 92, 94].
    * **Atmosphere:** 0.0009% (residence time ~9 days), but turns over rapidly to drive weather[cite: 92, 94].
    """)
    
    st.subheader("Conservation of Mass (Control Volumes)")
    st.latex(r"\frac{dS}{dt} = \sum I - \sum O")
    st.markdown("For a standard watershed, assuming no deep groundwater leakage: Change in Storage = Precipitation - Evapotranspiration - Runoff[cite: 94].")
    st.latex(r"\frac{dS}{dt} = P - E - Q")
    st.info("**Key Concept:** Over a long period (e.g., an annual cycle), $\\frac{dS}{dt} \\approx 0$, meaning $Q \\approx P - E$[cite: 149].")
    
    st.subheader("Interactive Application: Stormwater Rooftop (HW1, Q4)")
    st.markdown("For a flat rooftop with one drain, the mass balance is $\\frac{dS}{dt} = P - E - Q$[cite: 148]. During an intense storm, evaporation ($E$) is negligible compared to precipitation ($P$) and drainage ($Q$)[cite: 148].")
    p_input = st.slider("Precipitation Rate (mm/hr)", 0, 50, 20)
    q_input = st.slider("Drain Capacity (mm/hr)", 0, 50, 10)
    if p_input > q_input:
        st.error(f"$\\frac{{dS}}{{dt}} > 0$: Storage increases by {p_input - q_input} mm/hr. The roof is flooding[cite: 148].")
    else:
        st.success("Drain capacity exceeds or equals rainfall. No significant accumulation.")

# --- Chapter 2 ---
elif page == "Chapter 2: Atmospheric Thermodynamics":
    st.header("Chapter 2: Atmospheric Thermodynamics")
    
    st.subheader("Ideal Gas Law & Density")
    st.latex(r"\rho = \frac{p}{R_d T_v} \quad \text{where} \quad T_v = \frac{T}{1 - (1 - \epsilon)\frac{e}{p}}")
    st.markdown("Water vapor makes moist air *less dense* than dry air at the same temperature and pressure because $H_2O$ has a lower molecular mass than $N_2$ or $O_2$[cite: 95, 164].")
    
    st.subheader("Clausius-Clapeyron (Saturation Vapor Pressure)")
    st.latex(r"e_s(T) = e_0 \exp\left[\frac{L_v}{R_v}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right]")
    st.markdown("Constants: $e_0 = 611$ Pa, $T_0 = 273.15$ K, $L_v = 2.5 \\times 10^6$ J/kg, $R_v = 461$ J/kg/K[cite: 96, 161, 178].")
    
    st.subheader("Humidity Metrics")
    st.latex(r"q \approx \epsilon \frac{e}{p} \quad (\epsilon \approx 0.622)")
    st.latex(r"RH = \frac{e}{e_s} = \frac{q}{q_s}")
    st.latex(r"VPD = e_s - e")
    
    st.subheader("Interactive HW2 Q1 Simulator")
    st.markdown("Calculate properties for Lone Pine Creek[cite: 139].")
    temp_c = st.number_input("Air Temp (°C)", value=23.8)
    press_pa = st.number_input("Pressure (Pa)", value=76066)
    spec_hum = st.number_input("Specific Humidity (g/kg)", value=6.87)
    
    t_k = temp_c + 273.15
    q_kg = spec_hum / 1000
    e_calc = (q_kg * press_pa) / 0.622 # Simplified approximation[cite: 139]
    es_calc = 611 * np.exp((2.5e6 / 461) * ((1/273.15) - (1/t_k)))
    
    st.write(f"**Calculated Vapor Pressure ($e$):** ~{e_calc:.0f} Pa[cite: 139]")
    st.write(f"**Calculated Saturation Vapor Pressure ($e_s$):** ~{es_calc:.0f} Pa[cite: 139]")
    st.write(f"**Calculated RH:** ~{(e_calc/es_calc)*100:.1f}%[cite: 140]")

# --- Chapter 3 ---
elif page == "Chapter 3: Radiation Processes":
    st.header("Chapter 3: Radiation Processes")
    
    st.subheader("Surface Energy Balance")
    st.latex(r"R_n = R_s^{\downarrow}(1 - \alpha) + R_l^{\downarrow} - R_l^{\uparrow}")
    st.markdown("""
    * **$R_s^{\\downarrow}$**: Incoming shortwave (solar)[cite: 98].
    * **$\\alpha$**: Albedo (reflectivity). Snow reflects heavily, bare soil absorbs more[cite: 98].
    * **$R_l$**: Longwave (thermal). Downwelling from atmosphere, upwelling from surface[cite: 98].
    """)
    
    st.subheader("Atmospheric Emissivity (Clear Sky Models)")
    st.markdown("Used to find $R_l^{\\downarrow} = \epsilon_a \sigma T_a^4$[cite: 100].")
    st.markdown("* **Brunt:** $\epsilon_{a} = 0.605 + 0.048 \sqrt{e_a}$ (with $e_a$ in mb)[cite: 100, 136].")
    st.markdown("* **Prata:** $\epsilon_{a} = 1 - (1 + W_p)\exp(-\sqrt{1.2 + 3W_p})$ (with $W_p$ in cm)[cite: 100, 137].")
    
    st.subheader("Terrain Shading & Aspect (HW3 Q4)")
    st.info("A south-facing slope ($A=180^\circ$) receives significantly higher direct beam shortwave radiation ($1050$ W/m²) than a north-facing slope ($813$ W/m²) in the Northern Hemisphere[cite: 135, 136]. Panels in the Mojave desert should face South[cite: 164].")

# --- Chapter 4 ---
elif page == "Chapter 4: Atmospheric Circulation":
    st.header("Chapter 4: Atmospheric Circulation")
    
    st.subheader("Global Heat Redistribution")
    st.markdown("The tropics have a net radiation surplus ($R_n > 0$); midlatitudes/poles have a deficit. Circulation transports heat poleward[cite: 102, 126].")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Hadley Cell (0° to 30°)**")
        st.markdown("Air rises at the equator (low pressure $\\rightarrow$ condensation & persistent rain) and sinks near 30° (high pressure $\\rightarrow$ dry deserts)[cite: 102, 116, 126].")
    with col2:
        st.markdown("**Midlatitudes (30° to 60°)**")
        st.markdown("Heat is transported by horizontal eddies and frontal storm systems. Westerlies prevail here[cite: 102, 126, 127].")
        
    st.subheader("Geostrophic Balance & Coriolis")
    st.markdown("Coriolis force deflects moving air to the right in the Northern Hemisphere[cite: 103]. Geostrophic winds blow parallel to pressure contours when the pressure-gradient force balances the Coriolis acceleration[cite: 103].")

# --- Chapter 5 ---
elif page == "Chapter 5: Precipitation Processes":
    st.header("Chapter 5: Precipitation Processes")
    
    st.subheader("Uplift Mechanisms")
    st.markdown("1. **Horizontal Convergence:** Intertropical Convergence Zone (ITCZ)[cite: 105].")
    st.markdown("2. **Frontal Convergence:** Warm air over cold air; drives winter precipitation in Lone Pine Creek[cite: 105, 127].")
    st.markdown("3. **Orographic Uplift:** Air forced over mountains. Creates heavy rain on the windward side and a dry rain-shadow on the leeward side (e.g., Eastern Sierra Nevada, Eastern Andes)[cite: 105, 164].")
    st.markdown("4. **Thermal Convection:** Surface heating causes air to become buoyant[cite: 105].")
    
    st.subheader("Cloud Thermodynamics (Lapse Rates)")
    st.markdown("Before condensation, a rising parcel cools at the dry adiabatic lapse rate ($\Gamma_d = 9.8$ K/km)[cite: 104]. Once it reaches the Lifting Condensation Level (LCL, where $q = q_s$), latent heat is released, and it cools at the slower moist adiabatic lapse rate ($\sim 6-8$ K/km)[cite: 104].")
    
    st.subheader("HW4 Q3: Precipitation Disaggregation")
    st.latex(r"P(z) = P(z_{gage}) \frac{1 + \Gamma_p (z - z_{gage})}{1 - \Gamma_p (z - z_{gage})}")
    st.markdown("Used to estimate precipitation at higher elevations accounting for orography[cite: 130]. A warming climate raises the rain-snow transition elevation, meaning more precipitation falls as rain rather than accumulating as snow[cite: 131].")

# --- Chapter 6 ---
elif page == "Chapter 6: Snow Processes":
    st.header("Chapter 6: Snow Processes")
    
    st.subheader("Snow Water Equivalent (SWE)")
    st.latex(r"SWE = d_s \left(\frac{\rho_s}{\rho_w}\right)")
    st.markdown("Snow depth ($d_s$) tells you thickness. SWE tells you how much actual water is stored[cite: 108, 111]. If snow compacts, depth decreases but SWE remains the same[cite: 109, 117].")
    
    st.subheader("Surface Energy Balance & Melt Phases")
    st.latex(r"G = R_n - LE - H")
    st.markdown("In Margulis's convention, $LE$ and $H$ are positive away from the surface. $G$ is positive *into* the snowpack[cite: 108].")
    
    st.markdown("**Phase 1: Warming (Cold Content)**")
    st.latex(r"Q_{cc} = c_i \rho_w SWE (T_m - T_{snow})")
    st.markdown("Energy required to bring subfreezing snow to 0°C[cite: 109, 110, 124].")
    
    st.markdown("**Phase 2 & 3: Ripening & Output**")
    st.latex(r"M = \frac{G}{\rho_w L_f}")
    st.markdown("Once isothermal at 0°C, energy ($G$) drives phase change (melting). $L_f = 3.34 \\times 10^5$ J/kg[cite: 110, 124].")

# --- Homework Archive ---
elif page == "Homework Solutions Archive":
    st.header("📚 Key Homework Problem Walkthroughs")
    
    with st.expander("HW 5: Snow Energy Balance (Sensible/Latent Heat)"):
        st.markdown("""
        **Problem:** $R_n = 150$ W/m², $H = -50$ W/m², $LE = 7\%$ of $R_n$. Find $G$.[cite: 120]
        * $LE = 0.07 \\times 150 = 10.5$ W/m²[cite: 121]
        * $G = R_n - LE - H = 150 - 10.5 - (-50) = 189.5$ W/m²[cite: 121]
        * *Concept:* A negative $H$ means sensible heat is transferring from the atmosphere *into* the snowpack, warming it[cite: 121].
        """)
        
    with st.expander("HW 4: Disaggregating Lapse Rates"):
        st.markdown("""
        **Problem:** Gage at 2481m has $T = 280$ K. Find rain-snow transition (where $T = 273.15$ K). $\Gamma_{Ta} = -6.5$ K/km[cite: 130].
        * $T(z) = T_{gage} + \Gamma_{Ta}(z - z_{gage})$[cite: 130]
        * $273.15 = 280 + (-6.5 \text{ K/km}) \times (z - 2481\text{m})$[cite: 130]
        * $z \approx 3535$ m[cite: 130]
        """)

# --- Practice Midterms ---
elif page == "Practice Midterms":
    st.header("📝 Sample Midterm Problems")
    
    st.subheader("Fall 2024 Midterm - Problem 1")
    st.markdown("**Q:** Determine outgoing longwave radiation if $T_s = 29^\circ\text{C}$ and $\epsilon_s = 0.95$.[cite: 172, 173]")
    st.latex(r"R_l^{\uparrow} = \epsilon_s \sigma T_s^4 = 0.95 \times (5.67 \times 10^{-8}) \times (29 + 273.15)^4 = 448.95 \text{ W/m}^2")
    
    st.subheader("Sample Midterm - Rainwater Capture System")
    st.markdown("**Q:** Roof area $100\text{ m}^2$, wet season precip rate $2.5\text{ mm/day}$ for 165 days. Minimum tank storage?[cite: 165]")
    st.markdown("""
    * $P = 2.5 \text{ mm/day} = 0.0025 \text{ m/day}$[cite: 165]
    * $\text{Total Volume} = P \times \text{Area} \times \text{Days} = 0.0025 \times 100 \times 165 = 41.25 \text{ m}^3$[cite: 165]
    """)
    
    st.subheader("Conceptual: Andes Mountains")
    st.markdown("**Q:** In the Andes mountains, would you expect higher precipitation on the western or eastern side?[cite: 164]")
    st.markdown("**A:** Western (windward) side due to orographic uplift causing air masses to cool adiabatically, condense, and precipitate before being forced down the leeward (eastern) side[cite: 164].")
