# Course: Intelligent Document Extraction with OpenAI GPT & LangChain

In this hands-on course, you will learn how to build a fully automated Document AI System that uses:

- GPT Vision models to extract text from the document (invoice/business card)
- GPT-5.1 (or latest GPT text model) to analyze and extract structured entities
- LangChain to build robust, production-grade workflows
- MongoDB as a Database (Atlas)
- FastAPI for WebApp and API endpoint

## Pre-requisite

- It is assumed that you already have at least a beginner-level understanding of Python.
- If you are new to Python or do not have it installed yet
> please go through this video series first: https://www.youtube.com/playlist?list=PLC3dwsznxb3JkzJbR9aiFr557aB3CBqTS
​

## Setting Up Couse:
- Download or clone the folder structure from  
  GitHub: <https://github.com/vedicskill/udemy-intelligent-doc-openai>.

- Open a terminal in the project root folder and carefully install the dependencies as described below using Poetry.


### Install Poetry Dependency Library

Poetry is used as the dependency manager and virtual environment tool for this course.
> Official documentations of Poetry: <https://python-poetry.org/docs/>

1. Install Poetry (recommended official installer):

> **Linux / macOS:**
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

>**Windows (PowerShell):**
   ```
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

2. Ensure `poetry` is on your PATH and verify:
   ```
   poetry --version
   ```

Basic Usage: <https://python-poetry.org/docs/basic-usage/>

1. Initialising a pre-existing project
    ```
    cd pre-existing-project
    poetry init
    ```
2. Allow Python is greater or equal to >= <your Python version>, <4.0.0
    ```
    requires-python= ">=<python_version>,<4.0.0"
    ```
3. To install package use command `add`
    ```
    poetry add <package-name>
    ```

3. Inside the project folder, install all dependencies from `pyproject.toml`:
   ```
   poetry install
   ```
   This will create a virtual environment and install all required packages.

4. To activate the virtual environment:
   ```
   poetry shell
   ```


### MongoDB required libraries

This course uses MongoDB (e.g., MongoDB Atlas) for storing extracted document data.
> Official Documentation: <https://www.mongodb.com/docs/languages/python/pymongo-driver/current/>

1. Add the official MongoDB Python driver (PyMongo) using Poetry:
   ```
   poetry add pymongo[srv]
   ```

2. Example connection string you will use in the code (to be configured later in `.env`):
   ```
   MONGODB_URI=mongodb+srv://{user_name}:{password}@{cluster}.mongodb.net
   ```


### FastAPI required libraries

FastAPI is used to expose the Document AI pipeline as a web API/web app.

1. Add FastAPI and Uvicorn (ASGI server):
   ```
   poetry add fastapi[standard] uvicorn httpx httpie requests
   ```

2. During development, you will typically run the app with:
   ```
   poetry run uvicorn app.main:app --reload
   ```
   (Module path may vary depending on this repository structure.) 


### Langchain required libraries

LangChain is used to build the multi-step intelligent workflows (OCR → LLM → validation → DB).

1. Add core LangChain + OpenAI integration and environment helper:
   ```
   poetry add langchain langchain-openai openai python-dotenv
   ```

2. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   Then load it in code using `python-dotenv` (already added above).


## Project Details
Course URL: `https://www.udemy.com/course/intelligent-document-processing-with-openai-gpt-langchain/?referralCode=BF6564A9B3D71875F3E7`  
(Replace with the final course link once published.)

You will build real projects such as:


Document extraction app
- Document used: Invoice and Business card
- Models used → OpenAI Vision and LLM models (e.g., GPT-4o / GPT-5.x for text + JSON extraction) 
- Database: MongoDB Atlas for storing extracted entities and raw text
- WebApp : FastAPI-based backend with REST endpoints for upload and analysis


This is a complete end-to-end, project-based course with no prior AI experience required.


What You Will Learn
- OCR using OpenCV and Tesseract as a baseline for text extraction
- Prompt engineering for structured entity extraction (JSON responses)
- GPT-5.1 for text analysis, JSON extraction, and parsing from documents 
- LangChain for chaining steps and building intelligent workflows and tools 
- Validation pipelines with regex & fallback rules for robust outputs
- Integrating OCR → LLM → JSON parsing → App backend → Database
- Building a Document Scanner & Analyzer App with real invoice/business card examples
- Deploying the AI App locally using Uvicorn & FastAPI 


Technologies Used
- OpenAI API (Vision + Text models) 
- LangChain and langchain-openai for model orchestration 
- FastAPI for backend APIs and web entrypoints 
- MongoDB (Atlas or local) to persist document data 
- Poetry for dependency management and reproducible environments
