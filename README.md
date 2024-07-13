# Real Estate Web Scrapping

This project is the first part of a project that aims to analyze the trends in the real estate market in Egypt and to understand more about how the distribution of the real estate properties in Egypt is happening etc...

This part of the project aims to scrap data from a well-known real estate website and then store this data in a CSV file to then in the next steps insert this data into a data warehouse.
## Installation

You will need to install the packages below.
```bash
pip install pandas
pip install bs4
pip install requests
pip install csv
pip install os
pip install dotenv
```

## Usage
After installing the project you will have to create a .env file and add the following variables. 
```text
USER_AGENT = "YOUR_USER_AGENT"
BASE_SITE_URL = "WEBSITTE_BASE_url"
INITIAL_URL = "FIRST_PAGE_URL"
```
Then you can run the Python script to start scrapping the website.
```bash
python3 Web_Data_scraping.py  
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Contact Information
If you have any questions, feel free to reach out to me at mustafamabdelaziz@gmail.com.


## License

[MIT](https://choosealicense.com/licenses/mit/)