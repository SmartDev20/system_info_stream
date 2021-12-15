import streamlit as st
import platform as plf
import os
import sys
import getpass
import psutil as psu

st.header('System Information')
st.write("Platform :  "  , plf.platform())
st.write('System :  '  , plf.system())
st.write('Version :  ' , plf.version())
st.write('Mac Version :  ' , plf.mac_ver())
st.write('Release : ' , plf.release())
st.write('Machine : ' , plf.machine())
st.write('Processor : ', plf.processor())
st.write('Machine Name : ' , plf.node())
st.write('Platform uname : ' , plf.uname())
st.write('Platform Architecture :  ' , plf.architecture()  )
st.write('Os Name : ', os.name)
st.write('Os uname : ' , os.uname())
st.write('Sys platform : ' , sys.platform)
st.write('OS Login : ' , os.getlogin())
st.write('Get user : ' , getpass.getuser())
st.write('PSU : ' , psu.net_if_addrs())

