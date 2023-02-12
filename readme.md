# Loan Repayment Calculator
### This is a loan repayment calculator that calculates the total interest to be paid over a loan term, the total amount to be repaid over the loan term, and provides a breakdown of the loan repayments over the loan term.

## Getting Started
To get started, clone this repository to your local machine:

```
$ git clone https://github.com/your-username/loan-repayment-calculator.git
Prerequisites
To run this program, you will need the following installed on your machine:

Python 3.6 or higher
Django 3.2 or higher
Django REST framework 3.12 or higher
Installing
To install the required packages, run the following command:

$ pip install -r requirements.txt
Running the Application
To run the application, navigate to the project directory and run the following command:

$ python manage.py runserver
This will start the development server at http://127.0.0.1:8000/.
```

## API Endpoints
```
The following API endpoints are available:

POST /api/calculate-loan-repayment/
Calculates the loan repayment based on the given parameters. The input parameters are:

loan_amount (required) - The amount of the loan
loan_term (required) - The term of the loan in months
interest_rate (required) - The interest rate per year
repayment_frequency (required) - The frequency of the loan repayment (monthly, bi-monthly, or weekly)
The output parameters are:

total_interest - The total interest to be paid over the loan term
total_amount - The total amount to be repaid over the loan term
repayments - A list of the loan repayments, including the principal and interest amounts, and the remaining balance after each repayment.
Example:


POST /api/calculate-loan-repayment/
{
    "loan_amount": 10000,
    "loan_term": 12,
    "interest_rate": 10,
    "repayment_frequency": "monthly"
}
Response:

json
Copy code
HTTP 200 OK
{
    "total_interest": 500,
    "total_amount": 10500,
    "repayments": [
        {
            "repayment_no": 1,
            "repayment_date": "2023-02-01",
            "principal": 877.29,
            "interest": 83.33,
            "balance": 9122.71
        },
        {
            "repayment_no": 2,
            "repayment_date": "2023-03-01",
            "principal": 878.87,
            "interest": 81.76,
            "balance": 8243.84
        },
        ...
    ]
}
```

## Running the tests
To run the test suite, navigate to the project directory and run the following command:

```
$ python manage.py test
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.