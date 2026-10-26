import streamlit as st
import math

# =====================================================
# KONFIGURASI
# =====================================================

st.set_page_config(page_title="Wind Correction Angle")
st.title("Wind Correction Angle")

st.divider()

# =====================================================
# INPUT
# =====================================================

st.subheader("Data Kondisi Penerbangan")

col1, col2 = st.columns(2)

with col1:

    runway = st.number_input("Runway Heading (°)", min_value=0.0, max_value=360.0, value=90.0, step=1.0)
    airspeed = st.number_input("Kecepatan Pesawat (knot)", min_value=1.0, max_value=500.0, value=100.0, step=1.0)

with col2:

    wind_direction = st.number_input("Arah Angin (°)", min_value=0.0, max_value=360.0, value=45.0, step=1.0)
    wind_speed = st.number_input("Kecepatan Angin (knot)", min_value=0.0, max_value=200.0, value=20.0, step=1.0)


# =====================================================
# PERHITUNGAN
# =====================================================

if st.button("Hitung WCA", type="primary"):

    # -------------------------------------------------
    # Menghitung selisih arah
    # -------------------------------------------------

    angle_difference = (wind_direction - runway)

    # -------------------------------------------------
    # Menghitung WCA
    # -------------------------------------------------

    crosswind_component = (wind_speed * math.sin(math.radians(angle_difference)))
    ratio = (crosswind_component / airspeed)

    if abs(ratio) > 1:
        st.error("Pendaratan Tidak Dapat Dilakukan. Angin Terlalu Ekstrem!!")
        st.stop()

    wca = math.degrees(math.asin(ratio))

    # =================================================
    # HASIL
    # =================================================
    
    st.success("Perhitungan selesai!")
    st.metric("Wind Correction Angle", f"{wca:.2f}°")
       
    if abs(wca) < 1:
        st.info("Angin hampir sejajar dengan runway. Tidak perlu ada koreksi.")

    elif wca > 0:
        st.warning(f"Pesawat perlu melakukan koreksi "f"{abs(wca):.2f}° ke kanan.")

    else:
        st.warning(f"Pesawat perlu melakukan koreksi "f"{abs(wca):.2f}° ke kiri.")
