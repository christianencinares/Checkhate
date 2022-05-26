# CheckHate


CHECKHATE is an application that uses deep learning techniques to detect and classify harmful texts in Filipino language.

This project is developed by: 

* A. Aloveros (THW)
* C. Encinares (THW)
* J. Doros (THW)
* R. Delos Reyes (THW)

## Installation
You may opt to [activate a virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) before installing the dependencies, .

1. Open the terminal
2. Change the directory to the project's root directory
3. Install the dependencies in `requirements.txt`:

```cmd
> pip install -r requirements.txt
```
4. You may encounter problems installing wordcloud. If that happens, follow these steps:

    - Download the .whl file compatible with your Python version and your windows distribution (32bit or 64bit) [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud)
    - Change your directory to the path containing the downloaded .whl file
    - Run this command, replacing `<filename>` to the name of the .whl file previously downloaded (e.g. `wordcloud‑1.8.1‑cp310‑cp310‑win_amd64.whl`):
  
    ```cmd
    > python -m pip install <filename>
    ```
  
### Running the models

1. Open Jupyter Notebook
```cmd
> jupyter notebook
```
2. Go to "models"
3. Click on your desired model to run: LSTM or NaiveBayes