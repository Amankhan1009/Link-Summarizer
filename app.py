import validators, streamlit as st
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain         
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader


## streamlit APP
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

## Get the Groq API Key and url(YT or website)to be summarized      
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")
generic_url = st.text_input("URL", label_visibility="collapsed")                    



prompt_template="""
Provide a summary of the following content in 300 words:
Content:{text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])                 

if st.button("Summarize the Content from YT or Website"):
    ## Validate all the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
        
    elif not validators.url(generic_url):
        st.error("Please enter a valid Url. It can may be a YT video utl or website url")
    else:
        try:
            with st.spinner("Waiting..."):

                ## Gemma Model USsing Groq API
                llm = ChatGroq(model="qwen/qwen3-32b", groq_api_key=groq_api_key)
                ## loading the website or yt video data
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                                    generic_url,
                                    add_video_info=False
                                )
                    docs = loader.load()

                else:
                    loader = UnstructuredURLLoader(urls=[generic_url], ssl_verify=False,
                                                   headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})                             
                docs = loader.load()

                if not docs:
                    st.error("❌ This YouTube video has no transcript/captions available. Try another video.")
                    st.stop()

                ## Chain For Summarization
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)
                st.success(output_summary)

        except Exception as e:
            if "youtube" in generic_url:
                st.error("❌ Unable to extract transcript from this YouTube video. Try another video with captions enabled.")
            else:
                st.error("❌ Failed to load website content.")
            st.exception(e)
 
