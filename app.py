import streamlit as st
import pandas as pd
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="C&EE 150: Intro to Hydrology Study Guide", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("💧 Navigation")
page = st.sidebar.radio("Go to:", [
    "1. Welcome & Basics",
    "2. Core Chapters (1-6)",
    "3. Equation Sheet & Variables",
    "4. Advanced Topics & Visuals",
    "5. Practice Midterms"
])

# --- 1. Welcome Page ---
if page == "1. Welcome & Basics":
    st.title("💧 C&EE 150: Hydrology Midterm Study Guide")
    st.write("Welcome! This guide assumes zero prior knowledge. We will build from the basic hydrologic cycle up to advanced thermodynamics and snowmelt modeling.")
    
    st.info("💡 **Tip:** Use the sidebar to navigate through the chapters, check the equation sheet, or test yourself with the 3 practice midterms.")
    
    st.header("What is Hydrology?")
    st.write("Hydrology is the study of water, emphasizing the spatial and temporal distribution of water among reservoirs and the fluxes that connect them[cite: 62].")
    
    st.subheader("Global Water Distribution")
    # Using a markdown table for the reservoir data
    st.markdown("""
    | Reservoir | Approximate Share of Global Water |
    | :--- | :--- |
    | Oceans | 97.2% |
    | Ice caps and glaciers | 2.1% |
    | Near-surface groundwater | 0.31% |
    | Lakes and rivers | 0.017% |
    | Atmosphere | 0.0009% |
    """)
    st.caption("Data from Margulis, Chapter 1[cite: 62].")

# --- 2. Core Chapters ---
elif page == "2. Core Chapters (1-6)":
    st.title("📚 Course Content (Chapters 1-6)")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Ch 1: Hydrologic Cycle", 
        "Ch 2: Atmos. Thermo", 
        "Ch 3: Radiation", 
        "Ch 4: Circulation", 
        "Ch 5: Precipitation", 
        "Ch 6: Snow"
    ])
    
    with tab1:
        st.header("Chapter 1: The Hydrologic Cycle")
        st.write("Precipitation supplies water. Evaporation, sublimation, and runoff remove water[cite: 61].")
        st.latex(r"\frac{dS}{dt} = P - E - Q")
        st.write("*(Change in Storage = Precipitation - Evaporation - Runoff)*")
        # Placeholder for user content
        
    with tab2:
        st.header("Chapter 2: Atmospheric Thermodynamics")
        st.write("Understanding how much water vapor air can hold. Saturated vapor pressure rises rapidly as temperature increases[cite: 66].")
        st.latex(r"e_s(T) = e_0 \exp\left[\frac{L_v}{R_v}\left(\frac{1}{T_0} - \frac{1}{T}\right)\right]")
        st.markdown("**Key concepts to populate:** specific humidity, relative humidity, virtual temperature, precipitable water.")
        
    with tab3:
        st.header("Chapter 3: Radiation Processes")
        st.write("How energy reaches and leaves the surface. Shortwave (solar) vs. Longwave (terrestrial)[cite: 68].")
        st.latex(r"R_n = R_s^{\downarrow}(1 - \alpha) + R_l^{\downarrow} - R_l^{\uparrow}")
        
    with tab4:
        st.header("Chapter 4: Atmospheric Circulation")
        st.write("The tropics have a net radiation surplus; midlatitudes/poles have a deficit[cite: 72].")
        st.markdown("- **Hadley Cells:** Rising air near equator, sinking near 30° latitude[cite: 72].")
        st.markdown("- **Coriolis Effect:** Deflects moving air to the right in the Northern Hemisphere[cite: 73].")
        
    with tab5:
        st.header("Chapter 5: Precipitation Processes")
        st.write("Air must cool to reach saturation, usually through uplift[cite: 77].")
        st.markdown("**Uplift Mechanisms:** Horizontal convergence, Frontal convergence, Orographic uplift, Thermal convection[cite: 75].")
        
    with tab6:
        st.header("Chapter 6: Snow Processes")
        st.write("Snow Water Equivalent (SWE) is the hydrologic water storage in the snowpack[cite: 78].")
        st.latex(r"SWE = d_s \times \frac{\rho_s}{\rho_w}")
        st.markdown("**Melt Phases:** 1. Warming (Cold Content), 2. Ripening, 3. Melt Output[cite: 79, 80].")

# --- 3. Equation Sheet ---
elif page == "3. Equation Sheet & Variables":
    st.title("🧮 Equation Sheet & Reference")
    st.write("Quick reference guide for the midterm. All constants and equations match the provided exam sheets[cite: 25, 26, 27].")
    
    with st.expander("Physical Constants"):
        st.markdown("""
        * **Density of liquid water ($\rho_w$):** $1000 \text{ kg/m}^3$
        * **Latent heat of vaporization ($L_v$):** $2.5 \times 10^6 \text{ J/kg}$
        * **Latent heat of fusion ($L_f$):** $3.34 \times 10^5 \text{ J/kg}$
        * **Stefan-Boltzmann constant ($\sigma$):** $5.67 \times 10^{-8} \text{ W/m}^2/\text{K}^4$
        """)
        
    with st.expander("Chapter 2: Humidity & Clausius-Clapeyron"):
        st.latex(r"RH = \frac{e}{e_s} = \frac{q}{q_s}")
        st.latex(r"VPD = e_s - e")
        
    with st.expander("Chapter 6: Snow Energy Balance"):
        st.latex(r"Q_{cc} = -c_i \rho_w SWE (T_{snow} - T_m)")
        st.latex(r"Q_{melt} = SWE \rho_w L_f")

# --- 4. Advanced Topics & Visuals ---
elif page == "4. Advanced Topics & Visuals":
    st.title("📈 Advanced Topics & Visualizations")
    st.write("Interactive models to understand complex relationships.")
    
    st.subheader("Snowmelt Energy Balance Simulator")
    st.write("Adjust the sliders to see how Net Radiation ($R_n$), Sensible Heat ($H$), and Latent Heat ($LE$) affect the Ground Heat Flux ($G$) entering the snowpack[cite: 78].")
    
    rn = st.slider("Net Radiation (W/m²)", -100, 500, 150)
    le = st.slider("Latent Heat Flux (W/m²)", -50, 100, 10)
    h = st.slider("Sensible Heat Flux (W/m²)", -100, 100, -50)
    
    # G = Rn - LE - H
    g = rn - le - h
    
    st.metric(label="Surface Heat Flux (G)", value=f"{g} W/m²")
    if g > 0:
        st.success("G is positive: Energy is conducting into the snowpack (warming or melting)[cite: 78].")
    else:
        st.info("G is negative: The snowpack is cooling.")

# --- 5. Practice Midterms ---
elif page == "5. Practice Midterms":
    st.title("📝 Practice Midterms")
    st.write("Test your knowledge against the 3 sample midterms.")
    
    exam_choice = st.selectbox("Select a Practice Exam", ["CEE 150 Midterm 1", "CEE150 F24 Midterm", "CEE150 Sample Midterm"])
    
    if exam_choice == "CEE 150 Midterm 1":
        st.subheader("Exam 1 Simulator")
        st.markdown("**Question 1.1:** Would you expect to have more annual precipitation at a latitude of 0° or 30°N? Explain why.")
        with st.expander("Show Answer"):
            st.write("There will be more annual precipitation at a latitude of 0° because of the Hadley Cells. At 0°, air expands because of low pressure and rises, cooling and losing moisture resulting in rainfall. 30°N is dominated by the descending, dry branch of the Hadley Cell[cite: 1].")
            
        st.markdown("**Question 1.2:** In the Andes mountains (similar latitude to Sierra Nevada), would you expect higher precipitation on the western or eastern side?")
        with st.expander("Show Answer"):
            st.write("The western side (windward). Orographic uplift causes air to rise, cool adiabatically, and condense before being forced down the leeward side[cite: 1].")
            
    elif exam_choice == "CEE150 F24 Midterm":
        st.subheader("Fall 2024 Midterm Simulator")
        st.markdown("**Problem 1.1:** Determine the net shortwave radiation at a land surface with incoming SW = 800 W/m² and albedo = 0.26.")
        with st.expander("Show Answer"):
            st.latex(r"R_{s, net} = R_s^{\downarrow}(1 - \alpha) = 800(1 - 0.26) = 592 \text{ W/m}^2")
            st.write("If it were a north-facing slope, the net shortwave would decrease due to shading and less intensity[cite: 9].")

    elif exam_choice == "CEE150 Sample Midterm":
        st.subheader("Sample Midterm Simulator")
        st.markdown("**Problem 2.1:** Compute the vapor pressure at a station with $T=20^\circ\text{C}$, specific humidity $q=6\text{ g/kg}$, and $P=791\text{ mb}$.")
        with st.expander("Show Answer (Placeholder)"):
            st.write("Use the specific humidity equation: $q \approx \epsilon \frac{e}{P}$. Rearrange to solve for $e$. (Content to be fully populated)[cite: 19].")
