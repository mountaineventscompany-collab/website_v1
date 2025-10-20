import streamlit as st
import pandas as pd

def flight_log_merger():
    st.subheader("Flight Log Merger")

    uploaded_files = st.file_uploader(
        "Upload multiple .CSV flight logs", type=["csv"], accept_multiple_files=True
    )

    if uploaded_files:
        dfs = []
        for file in uploaded_files:
            try:
                df = pd.read_csv(file)
                df["source_file"] = file.name  # track where it came from
                dfs.append(df)
            except Exception as e:
                st.error(f"Could not read {file.name}: {e}")

        if dfs:
            merged = pd.concat(dfs, ignore_index=True)
            st.write("### Preview of merged logs:")
            st.dataframe(merged.head(20))

            # Download option
            csv = merged.to_csv(index=False).encode("utf-8")
            st.download_button(
                "Download merged log CSV",
                csv,
                "merged_flight_logs.csv",
                "text/csv",
                key="download-csv"
            )

flight_log_merger()
