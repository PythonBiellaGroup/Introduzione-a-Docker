import streamlit as st
from src.common.utils import get_formatted_tms, mask_credentials
import json
import uuid


def app():

    st.set_page_config(layout="centered")
    st.image(image="/app/static/login.png", width=150)

    placeholder = st.empty()

    with placeholder.form("login"):
        st.markdown("#### Enter your service credentials")
        username = st.text_input("username", placeholder="your username")
        pwd = st.text_input("password", type="password", placeholder="your password")
        submit = st.form_submit_button("Login")

    if submit and username and pwd:

        msg_login = json.dumps(
            {
                "id": str(uuid.uuid4()),
                "username": username,
                "password": mask_credentials(cred=pwd),
                "tms_login": get_formatted_tms(),
            }
        )
        st.success("Login successful")
        print(msg_login)
        return msg_login

    elif submit and (not username or not pwd):
        st.error("Login failed")

    else:
        pass
