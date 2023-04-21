import streamlit as st
import pickle

model = pickle.load(open('ultrafiltration-regression.sav', 'rb'))

def welcome():
	return 'welcome all'

# this is the main function in which we define our webpage
def main():
	# giving the webpage a title
	st.title("E-Coating Ultrafiltration Prediction")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
	html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Streamlit E-Coating Ultrafiltration Prediction App </h1>
	</div>
	"""
	
	# this line allows us to display the front end aspects we have
	# defined in the above code
	st.markdown(html_temp, unsafe_allow_html = True)
	
	# the following lines create text boxes in which the user can enter
	# the data required to make the prediction
	PE1 = st.text_input("Pressure 1", "Type Here")
	PE2 = st.text_input("Pressure 2", "Type Here")
	PE3 = st.text_input("Pressure 3", "Type Here")
	PE4 = st.text_input("Pressure 4", "Type Here")
	TP1 = st.text_input("Temperature 1", "Type Here")
	TP2 = st.text_input("Temperature 2", "Type Here")

	predict = ''
		
	# the below line ensures that when the button called 'Predict' is clicked,
	# the prediction function defined above is called to make the prediction
	# and store it in the variable result
	if st.button("Predict"):
		predict = model.predict([[PE1, PE2, PE3, PE4, TP1, TP2]])

if __name__=='__main__':
	main()
