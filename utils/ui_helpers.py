import streamlit as st


def show_ai_result(
    button_label,
    spinner_text,
    callback,
    text,
    download_name,
    key,
):
    """
    Display a reusable AI action with download support.
    """

    if st.button(
        button_label,
        key=key,
        use_container_width=True,
    ):

        with st.spinner(spinner_text):

            result = callback(text)

        st.success("Completed successfully.")

        st.markdown(result)

        st.download_button(
            "Download Result",
            result,
            file_name=download_name,
            mime="text/markdown",
            use_container_width=True,
            key=f"{key}_download",
        )