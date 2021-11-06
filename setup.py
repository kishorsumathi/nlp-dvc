from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
with open("requirements.txt", "r", encoding="utf-8") as f:
    LIST_OF_REQUIREMENT= f.read()

## edit below variables as per your requirements -
REPO_NAME = "nlp-dvc"
AUTHOR_USER_NAME = "kishorsumathi"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = [LIST_OF_REQUIREMENT]


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="simple nlp usecase",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="kishorbrindha18@gmail.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires="==3.7.0",
    install_requires=LIST_OF_REQUIREMENTS
)
