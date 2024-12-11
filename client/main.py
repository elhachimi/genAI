import streamlit as st

navigation = st.navigation(
    [
        st.Page("generate_text.py", title="Generate Text", icon="💬"),
        st.Page("generate_audio.py", title="Generate Audio", icon="🔊"),
        st.Page("generate_image.py", title="Generate Image", icon="🖼️"),
    ]
)

navigation.run()
