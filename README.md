# Expense Management System

A full-stack expense management system built with **Streamlit (frontend)** and **FastAPI (backend)** to help users track, manage, and analyze their daily expenses efficiently.

---

## Overview

Managing personal finances can be challenging without proper tools. This project provides a simple and interactive platform where users can:

* Record daily expenses
* Categorize spending
* Analyze expense patterns
* View insights through a user-friendly interface

---

## Architecture

This project follows a **client-server architecture**:

* **Frontend**: Built with Streamlit for interactive user experience
* **Backend**: Powered by FastAPI for handling API requests and business logic

---

## Features

* Add and manage expenses
* Categorize transactions
* Visualize spending patterns
* Real-time interaction between frontend and backend
* Test cases for reliability

---

## Project Structure

```
expense-management-system/
│
├── frontend/        # Streamlit application
├── backend/         # FastAPI backend server
├── test/            # Test cases
├── requirements.txt # Dependencies
├── README.md        # Project documentation
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/expense-management-system
cd expense-management-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI server

```bash
uvicorn server:app --reload
```

### 4. Run the Streamlit app

```bash
streamlit run frontend/app.py
```

---

## Technologies Used

* Python
* Streamlit
* FastAPI
* Pandas

---

## 👤 Author

**Oluwatobi Adekoya**

---

## Acknowledgements

This project was developed as part of my journey into **data science and software engineering**, focusing on building real-world, scalable applications.
