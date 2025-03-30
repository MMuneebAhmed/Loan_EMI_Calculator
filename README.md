# Loan EMI Calculator

## Overview
The **Loan EMI Calculator** is a user-friendly web application built with **Streamlit** that helps users calculate their Equated Monthly Installments (EMI) for different types of loans. The app also provides an amortization schedule, loan eligibility check, and graphical analysis of the loan structure.

## Features
- **Loan Eligibility Check**: Determines whether the user is eligible for a loan based on employment status, income, expenses, and credit score.
- **EMI Calculation**: Computes the monthly installment based on loan amount, interest rate, and tenure.
- **Amortization Schedule**: Displays the monthly breakdown of EMI payments, including principal and interest.
- **Extra & Balloon Payments**: Allows users to factor in additional monthly payments or lump-sum balloon payments.
- **Interactive Charts**: Provides a graphical representation of the loan balance over time and the principal vs. interest breakdown.
- **Dark Mode**: Option to switch to dark mode for better visibility.
- **Multi-Currency Support**: Users can select their preferred currency.
- **Multi-Language Support**: Available in English and Urdu.
- **Predefined Loan Types**: Supports home loans, car loans, and personal loans with default settings.

## Installation
To run this application locally, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/loan-emi-calculator.git
   cd loan-emi-calculator
   ```
2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Dependencies
This project requires the following Python libraries:
- `streamlit`
- `numpy`
- `pandas`
- `plotly`

You can install them using:
```sh
pip install streamlit numpy pandas plotly
```

## Usage
1. Open the app and check your **loan eligibility** by entering employment status, income, expenses, and credit score.
2. If eligible, enter loan details such as loan amount, interest rate, and tenure.
3. (Optional) Add extra monthly payments or balloon payments.
4. Click **Calculate EMI** to view the results, including EMI, total interest paid, and amortization schedule.
5. Explore the graphical insights on loan balance and principal-interest distribution.

## Contributing
Contributions are welcome! If you want to improve this project:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit: `git commit -m 'Add new feature'`
4. Push to your branch: `git push origin feature-branch`
5. Open a pull request.

## Contact
For any queries or suggestions, feel free to contact me at **your.email@example.com** or open an issue on GitHub.

---
Enjoy using the Loan EMI Calculator! 🚀

