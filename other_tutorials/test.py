import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = os.environ()['OPENAI_API_KEY']

from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
chunk_size=26
chunk_overlap = 4

r_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
c_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

text1='sampletextthat is more than 26'
r_splitter.split_text(text1)

#Real example:length_function refers to the functions to measure the size of the chunk, such as characters or tokens
langchain.text_splitter.CharacterTextSplitter(
    separator: str="\n\n",
    chunk_size=4000,
    chunk_overlap=200,
    length_function=<builtin function len> 
)
some_text = """When writing documents, writers will use document structure to group content. \
This can convey to the reader, which idea's are related. For example, closely related ideas \
are in sentances. Similar ideas are in paragraphs. Paragraphs form a document. \n\n  \
Paragraphs are often delimited with a carriage return or two carriage returns. \
Carriage returns are the "backslash n" you see embedded in this string. \
Sentences have a period at the end, but also, have a space.\
and words are separated by space."""

len(some_text)

c_splitter = CharacterTextSplitter(
    chunk_size=450,
    chunk_overlap=0,
    separator=' '
)

