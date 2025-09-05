import bs4
from langchain import hub
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document

WEBSITE_LIST = [
    "http://exam.ioe.edu.np/",
    "https://psc.sudurpaschim.gov.np/notice_list",
]

# loader = WebBaseLoader(
#     web_path=WEBSITE_LIST,
#     bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("table"))),
# )

# docs = loader.load()
# print(docs)


def scrap_notice():
    loader = WebBaseLoader(
        web_path=WEBSITE_LIST,
    )
    docs = loader.load()
    print(docs)
