import streamlit as st
import exifread

def exif_audit_tool():
    st.subheader("EXIF Consistency Auditor")

    uploaded_files = st.file_uploader("Upload mission images", type=["jpg","jpeg"], accept_multiple_files=True)

    if uploaded_files:
        altitudes = []
        for file in uploaded_files:
            tags = exifread.process_file(file, stop_tag="EXIF DateTimeOriginal", details=False)
            alt = tags.get("GPS GPSAltitude")
            if alt:
                try:
                    altitudes.append(float(str(alt)))
                except ValueError:
                    pass

        if altitudes:
            st.write("### Sample Altitudes:")
            st.write(altitudes[:10])
            if max(altitudes) - min(altitudes) > 20:
                st.error("⚠️ Significant altitude jumps detected (possible battery swap or GNSS issue).")
            else:
                st.success("No major EXIF altitude jumps detected.")
        else:
            st.warning("No GPSAltitude data found in uploaded images.")

exif_audit_tool()
