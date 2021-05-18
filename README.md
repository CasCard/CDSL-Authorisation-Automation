## Setup

### 1. Download Chrome Web Driver

Find the version of the chrome that you are using by navigating to ```chrome://settings/help``` or
```Setting > About Chrome```

Download [Chrome Webdriver](https://chromedriver.chromium.org/) corresponding to your version.
Currently it is ```90.0.4430```.

### 2. Download Python

If you haven't installed python earlier you can download setup from [here](https://www.python.org/downloads/)

### 3. Install Necessary Packages

Download all the files present in this repository and place them is a separate folder, Chrome Driver ```exe``` file should also be present in the same folder.

Open a new terminal in the same directory and install necessary packages with the following command

``` pip install -r requirements.txt```

### 4. Configuring Credentials

Open ```config.py``` in a text/code editor.\
Enter your ``` Gmail```,```Kite```,```CDSL``` username and password in the required fields.

Note: In order to successfully perform automation you need to disable 2 Factor Authentication of Gmail at [myaccount.google.com](https://myaccount.google.com/) otherwise the script would fail.
Also if Kite is configured for 2FA also the process will be unsuccessful.

**Never share ```config.py``` with anyone**
   
### 5. Usage

Once you have completed the setup opens a new terminal in the directory containing the required files and type:

```python authorisation.py```

## Issues
Feel free to create a new issue in cause of any trouble will be happy to resolve.

## Contributing
Pull requests are welcome.
## License
[MIT](https://choosealicense.com/licenses/mit/)
