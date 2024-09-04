import streamlit as st

def render_stats_bar(user_stats):
    st.metric(label="Total Users", value=user_stats['total_users'])
    st.metric(label="Currently Watching", value=user_stats['currently_watching'])
    st.metric(label="Users Active in Last Week", value=user_stats['active_last_week'])

def render_library_table(library_data):
    st.dataframe(library_data, use_container_width=True)

