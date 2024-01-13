import streamlit as st
import random
import string


# Function to generate password
def generate_password(length, include_uppercase, include_lowercase,
                      include_numbers, include_symbols):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return 'Please select at least one character set!'

    return ''.join(random.choice(characters) for i in range(length))


# Streamlit UI
st.title('Password Generator')

length = st.number_input('Password Length',
                         min_value=1,
                         max_value=20,
                         value=10)
include_uppercase = st.checkbox('Include Uppercase Letters', value=True)
include_lowercase = st.checkbox('Include Lowercase Letters', value=True)
include_numbers = st.checkbox('Include Numbers', value=True)
include_symbols = st.checkbox('Include Symbols')

if st.button('Generate'):
    password = generate_password(length, include_uppercase, include_lowercase,
                                 include_numbers, include_symbols)
    st.write('Generated Password:', password)
