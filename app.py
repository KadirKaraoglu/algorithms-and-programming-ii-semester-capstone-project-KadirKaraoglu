import streamlit as st
from algorithm import boyer_moore_search
from visualizer import visualize_search_results 

def main():
    st.set_page_config(layout="centered", page_title="Boyer-Moore String Search App")

    st.title("Boyer-Moore String Search Application")
    st.write("Enter text and a pattern to see where the pattern is found using the Boyer-Moore algorithm.")

    st.header("Enter Text and Pattern")
    text_input = st.text_area("Text to Search (Text):", height=200, help="Paste the main text here.")
    pattern_input = st.text_input("Pattern to Find (Pattern):", help="Enter the pattern you want to search for.")

    if st.button("Search"):
        if text_input and pattern_input:
            with st.spinner("Searching..."):
                indices = boyer_moore_search(text_input, pattern_input)

            if indices:
                st.success(f"Pattern '{pattern_input}' found in the text!")
                st.write(f"Found at indices: **{', '.join(map(str, indices))}**")
                
                st.subheader("Results:")
                
                visualize_search_results(text_input, pattern_input, indices) 
            else:
                st.warning(f"Pattern '{pattern_input}' not found in the text.")
        else:
            st.warning("Please enter both text and a pattern to search.")

    st.markdown("---")
    st.info("This application demonstrates the Boyer-Moore string searching algorithm and prepared by Kadir Karaoğlu")

if __name__ == "__main__":
    main()