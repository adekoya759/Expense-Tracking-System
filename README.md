# Expense management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.

## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **test/**: Contains the test cases for both frontend and backend
- **requirements.txt/**: Lists the required Python packages.
- **REAM.md/**: Provides an overview and instructions for the project

## Setup Instruction

1. **Clone the repository**:
   ```bash
    git clone https://github.com/yourusername/expense-management-system
    cd expense-management-system
    ```
2. **Install dependencies**:
    ```commandline
    pip install -r requirements.txt
    ```
3. **Run the FastAPI server**:
    ```commandline
   uvicorn server:app --reload
   ```
4. **Run the Streamlit app**:
    ```commandline
    streamlit run frontend/app.py
```

