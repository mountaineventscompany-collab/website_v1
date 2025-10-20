import streamlit as st

def overlap_tool():
    st.subheader("Overlap & Sidelap Recommender")

    terrain = st.selectbox("Terrain type:", ["Forest", "Urban", "Fields", "Mixed"])
    altitude = st.number_input("Flight altitude (m AGL):", min_value=20, max_value=500, value=100)
    focal_length = st.number_input("Focal length (mm):", min_value=10.0, max_value=50.0, value=24.0)

    if st.button("Recommend overlap"):
        if terrain == "Forest":
            fwd, side = 85, 80
        elif terrain == "Urban":
            fwd, side = 80, 70
        elif terrain == "Fields":
            fwd, side = 75, 65
        else:
            fwd, side = 80, 70

        st.success(f"Recommended Forward: {fwd}% | Sidelap: {side}%")
        st.info("Tip: Increase overlap if using rolling shutter cameras or flying low/fast.")

overlap_tool()
