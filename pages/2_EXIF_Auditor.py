import streamlit as st
import exifread
import re

def exif_audit_tool():
    st.subheader("EXIF Consistency Auditor")

    uploaded_files = st.file_uploader("Upload mission images", type=["jpg","jpeg"], accept_multiple_files=True)

    if uploaded_files:
        altitudes = []
        for file in uploaded_files:
            tags = exifread.process_file(file, details=False)

            # Log all keys + values for debugging
            st.write(f"### EXIF dump for {file.name}:")
            st.json({k: str(v) for k, v in tags.items()})

            # Look for any key containing "Altitude"
            alt_value = None
            for key, val in tags.items():
                if re.search("Altitude", key, re.IGNORECASE):
                    alt_value = val
                    break

            if alt_value:
                try:
                    altitudes.append(float(str(alt_value)))
                except Exception:
                    st.warning(f"Could not parse altitude for {file.name}: {alt_value}")

        if altitudes:
            st.write("### Sample Altitudes:")
            st.write(altitudes[:10])
            if max(altitudes) - min(altitudes) > 20:
                st.error("⚠️ Significant altitude jumps detected (possible battery swap or GNSS issue).")
            else:
                st.success("No major EXIF altitude jumps detected.")
        else:
            st.warning("No altitude-related EXIF tags found in uploaded images.")

exif_audit_tool()
