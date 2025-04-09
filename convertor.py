# Project 01: Unit Convertor
# Build a Google Unit Convertor using Python and Streamlit:
import streamlit as st
st.markdown(
    """
    <style>
    body {
    background-color: #lele2f;
    colour: white;
    }
    .stApp{
     background: linear-gradient(135deg, #00feba, #5b548a);
     padding 30px;
     border-radius:15px;
     box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }
    h1{
    text-align: center;
    font-size: 36px;
    colour:white;
    }
    .stButton>button{
    background: linear-gradient(45deg, #0b5394, #351c75);
    color:white;
    font-size:18px:
    padding:10px 20px;
    border-radius:10px;
    transitions:0.3s;
    box-shadow:0px 5px 15px rgba(0,201,255,0.4);
    }
    .stButton>button:hover{
    transform:scale(1.05);
    background: linear-gradient(45deg, #92fe9d,#00c9ff);
    color:black;
    }
    .result{
    font-size:20px;
    font-weight:bold;
    color:white;
    text-align:center;
    margin-top:20px;
    box-shadow:0px 5px 15px rgba(0,201,255,0.4);
    }
    .footer{
    text-align:center;
    margin-top50px;
    font-size:14px;
    color:black;
    }
    </style>
    """
    ,
    unsafe_allow_html=True
)
#title and description
st.markdown("<h1> Unit Convertor using Python and Streamlit</h1>",unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature with our simple and accurate conversion tool.")

#sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type",["Length","Weight","Temperature"])
length = st.number_input("Enter Value",value=0.0,step=0.1)
col1,col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From Unit",["Meter","Kilometer","Centimeter","Millimeter","Micrometer","Nanometer","Mile","Yard","Foot","Inch"])
    with col2:
        to_unit = st.selectbox("To Unit",["Meter","Kilometer","Centimeter","Millimeter","Micrometer","Nanometer","Mile","Yard","Foot","Inch"])
    
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From Unit",["Kilogram","Gram","Milligram","Microgram","Pound","Ounce"])
    with col2:
        to_unit = st.selectbox("To Unit",["Kilogram","Gram","Milligram","Microgram","Pound","Ounce"])
    
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From Unit",["Celsius","Fahrenheit","Kelvin"])
    with col2:
        to_unit = st.selectbox("To Unit",["Celsius","Fahrenheit","Kelvin"])
#conversion fuc=nction
def convertor_length(length,from_unit,to_unit):
    length_units = {
        "Meter":1,
        "Kilometer":1000,
        "Centimeter":0.01,
        "Millimeter":0.001,
        "Micrometer":0.000001,
        "Nanometer":0.000000001,
        "Mile":1609.34,
    }
    return (length / length_units[from_unit]) * length_units[to_unit]
def convertor_weight(weight,from_unit,to_unit):
    weight_units = {
        "Kilogram":1,
        "Gram":0.001,
        "Milligram":0.000001,
        "Microgram":0.000000001,
    }
    return (weight / weight_units[from_unit]) * weight_units[to_unit]
def convertor_temperature(temperature,from_unit,to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (temperature * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return temperature + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (temperature - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (temperature - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return temperature - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (temperature - 273.15) * 9/5 + 32        
    #button to perform conversion
    if st.button("Convert"):
        if conversion_type == "Length":
            result = convertor_length(length,from_unit,to_unit)
        elif conversion_type == "Weight":
            result = convertor_weight(length,from_unit,to_unit)
        elif conversion_type == "Temperature":
            result = convertor_temperature(length,from_unit,to_unit)
        #display result
        st.success(f"Result: {result} {to_unit}")
        #footer
        st.markdown("<p class='footer'>Developed by [Your Name]</p>",unsafe_allow_html=True)
        #footer
        st.markdown("<p class='footer'>Developed by [Your Name]</p>",unsafe_allow_html=True)
        #footer
        st.markdown("<p class='footer'>Developed by [Your Name]</p>",unsafe_allow_html=True)
        #footer
        st.markdown("<p class='footer'>Developed by [Your Name]</p>",unsafe_allow_html=True)    
    
        
            
                

