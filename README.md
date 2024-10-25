# The Quiztine Chapel
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>

  </ol>
</details>

## About the Project
The Quiztine Chapel is a small interactive quiz experience delivered through a command-line interface. This project connects to the [https://opentdb.com/] api to get question data. The quiz can be customised for difficulty and length.


### Built With
* [![Python][Python.com]][Python-url]


## 🛠️ Getting Setup
Prerequisites:
- Python 3.x must be installed with pip3 for dependency installation.
  

## Installation
1. Clone the Quiztine repository to your local machine using the following command:
   ```sh
   git clone https://github.com/SurinaCS/The-Quiztine-Chapel.git
   ```
2. Navigate into the cloned repository.
3. *(Optional)* Create and activate a virtual environment with the following command:
   ```sh
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Install the necessary packages using:
   ```sh
   pip install -r requirements.txt
   ```
5. Start the Quiz with:
   ```sh
   python3 quiz.py
   ```
   Optionally you can add the flag `-d` for difficulty and enter "easy", "medium" or "hard" (default=easy); or the flag `-a` for number of questions (up to 10, default=1).


[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Rich.com]: https://raw.githubusercontent.com/textualize/rich/master/imgs/logo.svg
[Rich-url]: https://rich.readthedocs.io/en/latest/
