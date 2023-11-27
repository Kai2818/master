# Template
How to work with the code

Install Python 3
Install pip3


DOWNLOAD THE REPOSITORY TO YOUR LOCAL SYSTEM

**Run this**

cd Template
pip3 install -r requirements

source venv/bin/activate

uvicorn --host localhost  main:app --reload

**end**

Now the janusgate should be running on port 8000 by default but you can change the port by adding the port parameter

uvicorn --host localhost  main:app --reload --port 9898


Documentation of the API should be accessible via http://localhost:8000/docs

![Screen Shot 2022-04-27 at 9 46 50 AM](https://user-images.githubusercontent.com/30108579/165421807-7066e74d-cd03-4541-869c-4604e46720b5.png)


