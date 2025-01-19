import streamlit as st
from steganography import * 


st.set_page_config(
    page_title='HideAndSeek',
    page_icon='',
    layout='wide',
    menu_items={
        'About':"This is steganograpyh tool which uses zerowidth characters to hide the message on visible text"
    }
)

if 'message' not in st.session_state:
    st.session_state['message']=""

if 'encryptMessage' not in st.session_state:
    st.session_state['encryptMessage']=""

if 'encryptedMessage' not in st.session_state:
    st.session_state['encryptedMessage']=""

if 'decryptMessage' not in st.session_state:
    st.session_state['decryptMessage']=""

if 'decrpytedMessage' not in st.session_state:
    st.session_state['decryptedMessage']=""

st.write('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)
st.write('<h1 style="text-align:center">Steganographr</h1>',unsafe_allow_html=True)

cEncrypt,cDecrypt=st.columns((1,1))

with cEncrypt:
    st.write('<div style="text-align:center">Encrypt</div>',unsafe_allow_html=True)
    st.session_state["message"]=st.text_area("Message",placeholder="Enter message which visibles")
    st.session_state["encryptMessage"]=st.text_area("Encrept Message",placeholder="Enter secrect message to encrypt in message")

    if st.button('Encrypt'):
        st.session_state['encryptedMessage']=wrap(st.session_state['message'],binToHide(strToBin(st.session_state['encryptMessage'])))

    if st.session_state["encryptedMessage"]:
        st.write('Copy the Encrypted Message')
        st.code(st.session_state["encryptedMessage"])

with cDecrypt:
    st.write('<div style="text-align:center">Decrypt</div>',unsafe_allow_html=True)
    st.session_state['decryptMessage']=st.text_area("Encrypted Message",placeholder="Enter encrypted Message to decrypt")

    if st.button('Decrypt'):
        try:
            st.session_state['decryptedMessage']=binToStr(hideToBin(unwrap(st.session_state['decryptMessage'])))
        except:
            st.session_state['decryptedMessage']=""

    if st.session_state['decryptedMessage']:
        st.write('<div style="text-align:center">Decrypt</div>',unsafe_allow_html=True)
        st.write('Copy the Secrete Message')
        st.code(st.session_state['decryptedMessage'])

st.write('<br><div style="text-align: center; font-size: 14px; color: #555;"><p>Want to see how the app works behind the scenes?</p><p><a href="https://github.com/manojn1729/steganographr" target="_blank" style="text-decoration: none; color: #007bff;">View the code on GitHub</a></p><p>Feel free to explore, report issues, or contribute!</p></div>',unsafe_allow_html=True)