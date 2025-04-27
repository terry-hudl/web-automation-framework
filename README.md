# Web Automation Framework

A Python-based BDD framework using Selenium & Behave for Hudl Login Functionality.  

**\* Note: Development of the framework was conducted using a Mac environment.**

## Pre-requisites

- Python 3.8+ installed
- Git installed
- Google Chrome installed

## Setup

1. **Clone**
   ```bash
   git clone https://github.com/your-org/web-automation-framework.git
   cd web-automation-framework
   
2. **Create Virtuel Environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate # On Windows: .venv\Scripts\activate
   
3. **Install Dependencies**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   
4. **Add Environment Variables**  
   ```bash
   create a .env in the root directory
   [add the contents for the .env file - supplied seperately as contains sensitive data]

5. **Execute Tests**  
   ```bash
   behave
   
Following the above steps will result in the test suite being executed and a HTML report being generated, that can be found located in the /reports directory.