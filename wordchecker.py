import streamlit as st
st.title("Text Analyzer by AR")
st.markdown("## this is app that show your paragraph length ,word,and more")

st.write("Please 📝write something this is Box")
inputuser = st.text_area('''✍ input text''')

if not inputuser.strip():
        st.error("Please enter a valid paragraph (not empty).")
else:
        inputuser=str(inputuser)
 
st.markdown("### Not Modified text")
st.write(f"{inputuser}")

uppercase = inputuser.upper() 
if st.button("🔠uppercase"):
    st.write("### Paragraph in 🔠Upper Case")
    st.markdown(f"{uppercase}")  
 
lower_case = inputuser.lower()     
if st.button("🔡LowerCase"):
    st.write("### Paragraph in 🔡Lower Case")
    st.markdown( f"{lower_case}")
       
length = len(inputuser)    
if st.button("Counts Number of 🔤Alphabets"):
    st.write("### Counts of 🔤Alphabets")
    st.markdown(f"The Number of the Alphabets is: {length}")  


words=len(inputuser.split())     
if st.button("Count number of 🆕word"):
    st.write("### Counts of 🆕word")
    st.markdown(f"The number of word is : {words}")       

vowels=("aeiouAEIOU")
vowel_count = sum(1 for char in inputuser if char in vowels)
vowel_count_str = str(vowel_count)
if st.button("vowels"):
    st.write("### Number Vowels in Paragraph:")
    st.write(f"Total Vowels: {vowel_count_str}")
search_word=st.text_input(" 🔍search word for 🔁replacements")
replace_word=st.text_input(" 🔁replace word for 🔁replacements")
if search_word and replace_word:
    modiefied_paragraph=inputuser.replace(search_word,replace_word)
    st.write(modiefied_paragraph)
    
search_word=st.text_input("#### 🔎search word for 🔍searching 🔤word")
if search_word in inputuser:
    st.success("Search word ✔found in pargraph")   
else:
    st.warning("Search word is ❌not found")    
    