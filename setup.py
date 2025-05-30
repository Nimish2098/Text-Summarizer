import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__="0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Nimish2098"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "raonimish23@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description="A small python package for NLP app",
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)