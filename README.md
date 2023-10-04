# CG_cat
# Massive dataset by Amazon

This project puts a key emphasis on the efficient management of the dataset while addressing potential challenges related to memory and time complexity.The focus lies in generating language-specific files, denoted as 'en-xx.xlsx,' for diverse languages such as English (en), Swahili (sw), and German (de). Additionally, the project entails the creation of distinct JSONL files for English (en), Swahili (sw), and German (de), comprising test, train, and dev data sets. Moreover, the endeavor aims to produce a consolidated JSON file that incorporates translations from English to all other languages, encompassing both 'id' and 'utt' data for the training sets.


## Installation
To set up the Python3 development environment and install the necessary dependencies, follow these steps:

1. Clone this repository to your local machine:
```{code}
https://github.com/lawdneo/CG_cat.git
``` 
2. Create a virtual environment (recommended):
```{code}
python3 -m venv venv
```
Activate the virtual environment:
```{code}
source venv/bin/activate
```
3. Install the required dependencies:
```{code}
pip install -r requirements.txt
```
4. Data Import:
Having already obtained the MASSIVE Dataset mentioned in the Data File, Ensure that this dataset is accessible in your project directory. Save it under the ```data``` folder in the project directory.
