# groq_chatbot

groq_chatbot is an open-source developer tool that simplifies building AI-powered chatbots with a user-friendly web interface. It integrates with the Groq API to facilitate real-time conversations, making it easy to deploy conversational applications quickly.

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

---

## Overview

groq_chatbot streamlines the development of interactive chatbots by combining robust backend API communication with an intuitive frontend.

### Why **groq_chatbot**?

This project offers a clear and extendable structure for building chat interfaces. Its core features include:

- 🛡️ **Secure API Key Management**: Uses environment variables to keep your API keys safe.  
- 💬 **Real-Time Web Interface**: Sleek, responsive chat UI for seamless user interactions.  
- 🧩 **Modular Architecture**: Built with Flask and templating for easy customization and extension.  
- 🚀 **Fast Deployment**: A ready-to-use framework for integrating conversational AI into your applications.  
- 🖥️ **User-Friendly Design**: Structured templates for an accessible and engaging chat experience.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python  
- **Package Manager:** Conda

---

## Installation

Build **groq_chatbot** from source and install dependencies.

### 1. Clone the repository:

```bash
git clone https://github.com/manasi582/groq_chatbot
```

### 2. Navigate to the project directory:

```bash
cd groq_chatbot
```

### 3. Install the dependencies:

Using **conda**:

```bash
conda env create -f conda.yml
```

---

## Usage

Run the project with:

```bash
conda activate {venv}
python {entrypoint}
```

---

## Testing

groq_chatbot uses the **pytest** test framework. Run the test suite with:

```bash
conda activate {venv}
pytest
```
