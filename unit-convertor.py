import streamlit as st 
st.title("Unit Convertor ")
st.markdown("### ALL Unit Convertor")
st.write("This is a simple unit convertor app that can convert units of currency, length, weight and time ")

catagory = st.selectbox("chosse catagory" , ["Currency", "Length", "Weight", "Time"])
def convert_unit(catagory, value ,unit ):
    # Convertor code for Currency
    if catagory =="Currency":
        if unit == "Rupees to Dollars":
            return value /279.37
        elif unit == "Dollars to Rupees":
            return value * 279.37
        elif unit == "Rupees to Pounds":
            return value / 5.51
        elif unit == "Pounds to Rupees":
            return value * 5.51
        
#    Convertor code for Lenght
    elif catagory == "Length":
        if unit == "Miles to Kilometers":
            return value * 1.60934  
        elif unit == "Kilometers to Miles":
            return value / 1.60934
        # Convertor code for Weigth
    elif catagory == "Weight":   
        if unit == "Kilograms to Pounds":
            return value *2.20462262
        elif unit == "Pounds to Kilograms":
            return value / 2.20462262
    # Convertor code for Time    
    elif catagory == "Time":
        if unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Days to Hours":
            return value * 24
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Seconds":
            return value * 86400
        elif unit == "Seconds to Days":
            return value / 86400
    return 0
        
if catagory == "Currency":
    unit  = st.selectbox("select conversation",["Rupees to Dollars","Dollars to Rupees","Rupees to Pounds","Pounds to Rupees"])
 
elif catagory == "Length":
     unit = st.selectbox("select converstion ",["Kilometers to Miles","Miles to Kilometers"])
 
elif catagory == "Weight":
    unit = st.selectbox("select converstion ",["Kilograms to Pounds","Pounds to Kilograms"])
elif catagory == "Time":
    unit = st.selectbox("select converstion ",["Hours to Minutes","Minutes to Hours","Seconds to Minutes","Minutes to Seconds","Days to Hours","Hours to Days","Days to Seconds","Seconds to Days"])

       
value= st.number_input("enter the value to convert ")
if st.button("Convert"):
    result = convert_unit(catagory , value , unit)
    st.success(f"the result is {result:.2f}")
        
