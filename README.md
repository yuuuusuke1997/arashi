**Visualize lyrics and predict what ARASHI wanted to tell us in Python.**

## Description
* get the lyrics for all songs

* clean up for getting accurate date

* visualize lyrics by wordcloud on Jupyter Notebook

## Requirement
* Windows10
* Python 3.8.0
* Jupyter Notebook(Anaconda3)

## Install
Git clone is easiest to install these files:
```
git clone https://github.com/yuuuusuke1997/arashi.git
cd wordcloud_arashi
```

## Usage
**step1. scraping_arashi.py**

1. Add these libraries:
```
$pip install beautifulsoup4
$pip install requests
$pip install urllib3
$pip install pandas
```

2. Run the file in python console:
```
python scraping_arashi.py install
```

And then make sure you got csv file

**step2. morphological_analysis_arashi.py**

1. Add these libraries:
```
$pip install Janome
$pip install pandas
```

2. Run the file in python console:
```
python morphological_analysis_arashi.py install
```

And then make sure you got txt file

**step3. wordcloud_arashi.ipynb**

1. You should install Jupyter Notebook if you don't have it:

Check the link below. It's just 3 steps done to install Jupyter Notebook.
* First, download Python3.7 version for Windows
* Second, open Anaconda Prompt
* Third, type `$jupyter notebook` on Anaconda Prompt(Jupyter Notebook will open after you type)
> https://datachemeng.com/wp-content/uploads/anaconda_jn_windows.pdf

2. Open `wordcloud_arashi.ipynb` file on Jupyter Notebook

3. Add this library:
```
$pip install wordcloud
```

4. Run the file:

`"Ctrl + Enter"`
