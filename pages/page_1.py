# import streamlit as st
# import sys
# import os

# st.write(sys.argv[0])
# st.write(os.path.basename(sys.argv[0]))

from streamlit_javascript import st_javascript
import streamlit as st

url = st_javascript("await fetch('').then(r => window.parent.location.href)")

st.write(url)
