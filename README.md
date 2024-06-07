**Project Overview**
Project Structure
The project is organized across several branches:

main: This is the default branch that contains the main codebase of the project, including main.py and test_main.py.

M-Hunain5037-patch-1: This branch includes the Continuous Integration (CI) configuration file for the project. It is responsible for setting up the CI pipeline that ensures the code is building and tests are passing with each commit.

M-Hunain5037-patch-2: This branch contains the configuration for SonarCloud, a cloud-based code quality and security service. The SonarCloud configuration allows the project to have its code automatically analyzed for code smells, bugs, and security vulnerabilities.

This project consists of two main files:

main.py: This file contains the main logic of the project.
test_main.py: This file contains unit tests for the functions defined in main.py.
Unit Tests
The unit tests are written using Python's built-in unittest module. When test_main.py is run, it tests various scenarios and edge cases for the process_numbers function defined in main.py.

Here is a snapshot of the test results when running test_main.py:

![image](https://github.com/M-Hunain5037/Assignment/assets/141824020/c53afe33-6b73-498a-8af5-12c092ae592a)


Unit Test Results


Continuous Integration
The project uses GitHub Actions for Continuous Integration (CI). The workflow is defined in .github/workflows/main.yml. This workflow is triggered on every push and pull request to the main branch. It sets up a Python environment, installs any necessary dependencies, and runs the unit tests.

![image](https://github.com/M-Hunain5037/Assignment/assets/141824020/8dece462-131c-4c49-9db9-6637549565dd)




Code Quality Analysis with SonarCloud
As a bonus, the project is also integrated with SonarCloud for code quality analysis and Pull request was successfully merged and show analysis report of my code 

![image](https://github.com/M-Hunain5037/Assignment/assets/141824020/7d079499-d59c-4dd4-b68d-82eac16b256d)
