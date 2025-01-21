from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="streamlit-session-manager",
    version="0.1.0",
    author="5X",
    author_email="support@5x.co",
    description="A session manager for Streamlit applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/streamlit-session-manager",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Streamlit",
    ],
    python_requires=">=3.8",
    install_requires=[
        "extra-streamlit-components"
    ],
)