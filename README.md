AI Agent Development Using ADK – Google Startup Task

This repository provides a complete record of the work carried out to develop an AI Agent using Google’s Agent Development Kit (ADK) for the Google Startup Task.
It documents the environment configuration, key setup, project structure, deployment attempts, issues encountered, and the troubleshooting measures implemented during the process.

1. Getting Started
1.1 Environment Setup

A dedicated virtual environment was created for the project using:

python -m venv .venv

The environment must be activated each time the project is executed.
macOS and Linux users should run source .venv/bin/activate,
Windows CMD users should run .venv\Scripts\activate.bat,
and Windows PowerShell users should run .venv\Scripts\Activate.ps1.

Once activated, the necessary dependencies were installed through:

pip install -r requirements.txt

2. Setting Up API Keys

Google Cloud was used to generate the required API key.
A new cloud project was created, followed by navigation to Google AI Studio where the Personal API Key was generated.
The key was then assigned to the project, and a billing account connection was completed to ensure full functionality.

After obtaining the key, a .env file was created in the root directory, and the key was added in the following format:

GOOGLE_API_KEY=your_api_key_here


This ensured secure and isolated access to the key during execution.

3. Project Overview

The objective of the project was to create an ADK-based AI agent and validate its execution and deployment workflow.
The process included preparing the development environment, configuring ADK, integrating the API key, and attempting agent execution through different terminals and approaches.
The repository serves as formal documentation of the entire workflow, including configuration steps and error analysis.

4. Development Workflow
4.1 Environment Configuration

The virtual environment was created and configured with all necessary libraries.
ADK installation and version alignment with Python were evaluated to avoid compatibility issues.

4.2 Project Structure

The repository contains the core development files, including agent.py, __init__.py, .env, and requirements.txt, along with supporting logs and documentation.
These files collectively define the agent's setup, configuration, and execution process.

4.3 Google Cloud and API Studio Configuration

Initial difficulties were encountered due to free-tier restrictions in Google Cloud.
After multiple attempts, a project was successfully created and linked to AI Studio.
API key generation required repeated attempts because the key generation page failed to load properly.
Once resolved, the key was configured correctly in the local environment.

4.4 Deployment Attempts

Multiple deployment attempts were made through VS Code, PowerShell, and CMD.
Although the server initiated successfully, the interface consistently displayed the error message “Failed to load agent,” indicating an issue with agent initialization or configuration.

5. Challenges Encountered

Several challenges arose during the process.
Google Cloud free-tier limitations affected project setup and prevented several required operations.
The API key generation page repeatedly failed to load, delaying the setup.
ADK and Python compatibility issues caused execution failures.
Folder duplication occurred during renaming, resulting in incorrect import paths.
Dependency installation issues and environment mismatches led to repeated deployment failures even when the server was running successfully.

6. Troubleshooting Steps

A series of troubleshooting actions were carried out.
These included reinstalling ADK, reinstalling and switching Python versions, regenerating API keys, restructuring the project folders, testing the execution environment across different terminals, resetting the virtual environment, and reviewing error logs to trace configuration issues.
Despite multiple attempts, deployment remained unsuccessful due to platform and configuration constraints.

7. Key Learnings

The task provided insight into ADK–Python compatibility requirements and showed the importance of precise environment configuration.
It highlighted the limitations of the Google Cloud free-tier environment and revealed how folder structure and naming directly influence module imports.
It also demonstrated that successful server initiation does not necessarily mean the agent will load correctly.
