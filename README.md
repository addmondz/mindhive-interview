### MindHive Interview - README
This repository contains the code for the MindHive Interview project. Follow the instructions below to set up and run the project on your local machine.

### Prerequisites
Before you begin, ensure you have met the following requirements:

1. Python (>= 3.x) installed on your local machine.
2. Git installed for cloning the repository.
3. MySQL database server installed and configured.
4. Apache2 or other web server software installed (if applicable).

### Installation
1. Clone the repository to your local machine:
git clone https://github.com/addmondz/mindhive-interview

2. Navigate to the project directory:
cd mindhive-interview

3. Copy the example environment file and fill in the necessary credentials:
cp .env.example .env

4. Install the project's Python dependencies using pip:
pip install -r requirements.txt

5. Run the web scraping script to start the application:
python -m app.scripts.run_scrapping

6. Start the application
python run.py