import streamlit as st
import random
import string
user_input = st.slider("password length",1,100,1)
dig=st.checkbox("include digits")
alp=st.checkbox("include alphabets")
sym=st.checkbox("include symbols")
password=''
#st.stop()
if dig and alp and sym:
    password=''.join(random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(user_input))
elif not alp and dig and sym:
    password=''.join(random.choice(string.punctuation+string.digits) for i in range(user_input))
elif not dig and alp and sym:
    password=''.join(random.choice(string.ascii_letters+string.punctuation) for i in range(user_input))
elif not sym and dig and alp:
    password=''.join(random.choice(string.ascii_letters+string.digits) for i in range(user_input))
elif not sym and not dig and alp:
    password=''.join(random.choice(string.ascii_letters) for i in range(user_input))
elif not dig and not alp and sym:
    passsword=''.join(random.choice(string.punctuation) for i in range(user_input))
elif not alp and not sym and dig:
    password=''.join(random.choice(string.digits) for i in range(user_input))
st.write("Your password:\n")
st.write(password)
