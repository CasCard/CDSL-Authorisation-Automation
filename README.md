# Update : SMS Based Verification

After few usage I came to know that e-mail based verification not much faster.So I have create a new script which actually fetches OTP from direct mobile SMS.
This is done using ```https://messages.google.com/``` . A service by google in which you can view you mobile SMS in your browser.

For the CDSL verification SMS I have created a separate repository ,so that for people who still need email based can use this.

SMS based repository is at : [https://github.com/CasCard/CDSL-Authorisation-Automation-SMS](https://github.com/CasCard/CDSL-Authorisation-Automation-SMS)

You can read the instructions there . :)

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

Note: In order to successfully perform automation you need to disable 2 Factor Authentication of Gmail at [myaccount.google.com](https://myaccount.google.com/security) otherwise the script would fail.
Also if Kite is configured for 2FA with Authenticator also the process will be unsuccessful.

**Never share ```config.py``` with anyone**
   
### 5. Usage

Once you have completed the setup opens a new terminal in the same directory containing the required files and type:

```python authorisation.py```

you only needed to type this command whenever authorisation is necessary

## Issues
Feel free to create a new issue in cause of any trouble will be happy to resolve.

## Contributing
Pull requests are welcome.
## License
[MIT](https://choosealicense.com/licenses/mit/)
