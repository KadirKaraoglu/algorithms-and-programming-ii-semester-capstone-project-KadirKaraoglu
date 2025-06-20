import streamlit as st

def visualize_search_results(text, pattern, indices):
    """
    Visualizes the search results by highlighting the found patterns in the text.
    
    Args:
        text (str): The original text.
        pattern (str): The pattern that was searched.
        indices (list): A list of starting indices where the pattern was found.

    Gemini was used to help create this class.
    """
    if not indices:
        st.info("No occurrences to visualize.")
        return

    highlighted_text = ""
    last_end = 0

    for start_idx in indices:
        end_idx = start_idx + len(pattern)
       
        highlighted_text += text[last_end:start_idx]
      
        highlighted_text += f"<span style='background-color: yellow; font-weight: bold; padding: 2px;'>{text[start_idx:end_idx]}</span>"
        
        last_end = end_idx
    
    highlighted_text += text[last_end:]
   
    st.markdown(highlighted_text, unsafe_allow_html=True)
