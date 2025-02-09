# Text-to-SQL LLM App

This repository contains a Text-to-SQL application that utilizes a large language model (LLM) to generate SQL queries from natural language input. The project is built using Streamlit for the user interface and integrates the Groq AI model for processing text queries.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tools and Technologies](#tools-and-technologies)

## Introduction

The Text-to-SQL LLM App allows users to interact with a SQLite database using natural language queries. The application translates user queries into SQL commands and retrieves data from the student.db database. It is designed to simplify database interaction for users without SQL knowledge.

## Features

- Converts natural language queries into SQL commands.

- Connects to an SQLite database (student.db).

- Provides a Streamlit-based user interface.

- Uses Groq AI for query generation.

- Supports dynamic database interaction.

## Installation

1. Clone the repository to your local machine:

```
   git clone https://github.com/srijosh/Text-to-SQL-LLM-App.git
```

2. Navigate to the project directory:

```
   cd Text-to-SQL-LLM-App
```

3. Install the required dependencies:

```
   pip install -r requirements.txt
```

4. Set up environment variables by creating a .env file (Use .env.sample as a reference for setting up your .env file.)

## Usage

1. Run the database initialization script:

```
python database.py
```

2. Start the Streamlit application:

```
   streamlit run app.py

```

## Tools and Technologies

- Groq API: AI-based text-to-SQL processing.

- SQLite: Lightweight relational database.

- Streamlit: Web framework for interactive UI.

- Python-dotenv: Loads environment variables from a .env file.
