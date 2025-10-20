import streamlit as st
import exifread

def exif_audit_tool():
    st.subheader("EXIF Consistency Auditor")

    uploaded_files = st.file_uploader("Upload mission images", type=["jpg","jpeg"], accept_multiple_files=True)

    if uploaded_files:
        altitudes = []
        for file in uploaded_files:
            tags = exifread.process_file(file, details=False)

            # Log all available EXIF keys so we can inspect DJI files
            st.write(f"### Keys found in {file.name}:")
            st.json(list(tags.keys()))  # print keys in a clean JSON view

            # Try multiple keys, since drones label them differently
            possible_keys = ["GPS GPSAltitude", "GPSAltitude", "EXIF GPS GPSAltitude"]
            alt_value = None
            for key in possible_keys:
                if key in tags:
                    alt_value = tags[key]
                    break

            if alt_value:
                try:
                    # Some values are ratios like 710/1 → convert to float
                    altitudes.append(float(str(alt_value)))
                except Exception:
                    st.warning(f"Could not parse altitude for {file.name}")

        if altitudes:
            st.write("### Sample Altitudes:")
            st.write(altitudes[:10])
            if max(altitudes) - min(altitudes) > 20:
                st.error("⚠️ Significant altitude jumps detected (possible battery swap or GNSS issue).")
            else:
                st.success("No major EXIF altitude jumps detected.")
        else:
            st.warning("No GPS altitude data found in uploaded images.")

exif_audit_tool()
