import streamlit as st

st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #1e1e1e;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("Initiative_RGB_Blue.png", use_container_width=True)
st.title("Initiative EE Data Downloader")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.email = None

# Login form
if not st.session_state.logged_in:
    email = (st.text_input("Email")).lower()
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        try:
            
            if get_user_data(email)[1] == password:
                st.session_state.logged_in = True
                st.session_state.email = email
                st.rerun()  # Refresh the app
            else:
                st.error("Invalid email or password!")
        except Exception as e:
            st.error("Error during login.")
            #st.exception(e)

