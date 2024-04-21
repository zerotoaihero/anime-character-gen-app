import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import streamlit as st

dotenv.load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.8)

# Initialize session state if necessary
if "name" not in st.session_state:
    st.session_state["name"] = ""

# Elements that should always be visible
st.title("AI-Powered Anime Character Generator")
name_prompt = st.text_input("Give me a theme for your anime character")  

# Container for elements changing based on interactions
container = st.container() 
with container:
    if st.button("Generate Name"):
        theme = name_prompt  
        prompt = f"Generate a unique Japanese Anime character name with the theme of {theme}"
        response = chat.invoke(
            [HumanMessage(content=prompt)]
        )
        st.session_state["name"] = response.content 
    st.write("Your Anime Name:", st.session_state["name"])  
    wise_quote = st.checkbox("Wise", key="wise")  
    dramatic_quote = st.checkbox("Dramatic", key="dramatic")
    humorous_quote = st.checkbox("Humorous", key="humorous")

    if st.button("Get a Quote"):
        selected_styles = []
        if wise_quote:
            selected_styles.append("wise")
        if dramatic_quote:
            selected_styles.append("dramatic")
        if humorous_quote:
            selected_styles.append("humorous")

        if selected_styles:
            prompt = "Write a quote said by an anime character named " + st.session_state["name"] + " that is " + ", ".join(selected_styles)
            response1 = chat.invoke(
                [
                    HumanMessage(
                        content=prompt
                    )
                ]
            )
            st.write(response1.content) 
        else:
            st.write("Please select at least one quote style.") 
