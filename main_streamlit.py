"""A main script to run streamlit application.

"""
import ast
import streamlit as st
import streamlit.components.v1 as components
import spacy
import pandas as pd
from src.utility.loggers import logger
from src.inference.core import generate_output
from src.utility.graph_visualization import get_graph_plot


def show_text(df, id):
    ex = [
        {
            "text": df.iloc[id]["article_text"],
            "ents": df.iloc[id]["ner"],
        }
    ]
    colors = {
        "CUSTOM_ORG": "#BE5525",
        "CUSTOM_PERSON": "#95CFDC",
        "CUSTOM_PLACE": "#55BB6A",
        "CUSTOM_ROLE": "#BE55DE",
    }
    options = {"colors": colors}
    components.html(
        spacy.displacy.render(ex, style="ent", options=options, manual=True),
        scrolling=True,
    )


st.title("Almost All NLP Application")
st.write("Assembled almost all NLP concepts in a single use case:")
st.write(
    "Data Collection,Data Cleaning,Text Classification,Topic Modeling,Entity Coreference Resolution,Entity Linking,Custom NER,Information Extraction,Knowledge Graph,Searching"
)
form = st.form(key="my-form")
input_data = form.text_area(
    "Enter query to search news articles knowledge base"
)
# only_custom_entities = form.checkbox(
#    "Extract Relationships for only Custom Entities"
# )
submit = form.form_submit_button("Elastic Search")
output_df = pd.DataFrame(
    columns=["sentiment", "topics", "URL", "article_text"]
)
if submit:
    try:
        output = generate_output(input_data)
        # output = pd.read_csv("test.csv")
        output_df["similarity_score"] = output["similarity_score"]
        output_df["sentiment"] = output["sentiment"]
        output_df["URL"] = output["article_url"]
        output_df["article_text"] = output["article_text"]
        output_df["ner"] = output["ner"]
        output_df["relationships"] = output["relationships"]
        output_df["topics"] = output["topics"]
        # st.dataframe(output_df)

        # output_plot = get_graph_plot(output_df)
        # st.pyplot(output_plot)
    except Exception as error:
        message = "Error while creating output"
        logger.error(message, str(error))

st.text("Top 3 relevant news articles:")
st.text("")


cols = st.columns((1, 1, 2, 1))
fields = ["Similarity Score", "Sentiment", "Topics", "URL"]
# header
for col, field in zip(cols, fields):
    col.write("**" + field + "**")

cols = st.columns((1, 1, 2, 1))
for id, row in output_df.iterrows():
    col1, col2, col3, col4 = st.columns((1, 1, 2, 1))
    col1.write(row["similarity_score"])  # index
    col2.write(row["sentiment"])  # email
    # col3.write(row["topics"])  # unique ID
    col3.markdown(row["topics"])
    # col4.write(row["URL"])  # email status
    col4.write(
        '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(
            row["URL"], "Article Link"
        ),
        unsafe_allow_html=True,
    )
    # button_phold = col5.empty()  # create a placeholder
    # do_action = button_phold.expander("Show")
    # do_action.write("Some Data")
    # button_phold.button(
    #    "Show", key=id, on_click=show_text, args=(output_df, id)
    # )
    with st.expander("Article Text with Custom NER"):
        show_text(output_df, id)

    with st.expander("Knowledge Graph"):
        output_plot = get_graph_plot(
            pd.DataFrame.from_records(
                ast.literal_eval(output_df.iloc[id]["relationships"])
            )
        )
        st.pyplot(output_plot)
    # expander = st.expander("Show Custom NER")
    # expander.write(show_text(output_df, id))
    st.text(
        "----------------------------------------------------------------------------------"
    )
    st.text("")
