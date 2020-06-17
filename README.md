# Bank Tech Test

[![Build Status](https://travis-ci.com/dpwdec/bank-tech-test.svg?branch=master)](https://travis-ci.com/github/dpwdec/bank-tech-test)

Account statement printing application that tracks transactions and outputs a statement showing balance and transaction history.

## Installation

1. Clone this repo
2. Install `pipenv` with `brew install pipenv`
3. Nagivate to the project repo
4. Run `pipenv install` to install project dependencies.
5. See the `How to use` section on how to run the code as an application.

## How to use
Via your machine's `CLI` in the interactive `Python3` REPL:
```
>>> from src.account import Account
>>> from src.printer import Printer
>>> from src.transaction import Transaction
>>> printer = Printer()
>>> account = Account(0, Transaction, printer)
>>> account.deposit(200)
>>> account.deposit(50)
>>> account.withdraw(100)
>>> acc.print_statement()
date       || credit  || debit   || balance
16/06/2020 ||         || 200.00  || 0.00   
16/06/2020 ||         || 50.00   || 200.00 
16/06/2020 || 100.00  ||         || 250.00 
```
## Tests

To run all tests:
```
pipenv run test
```

To run only unit tests:
```
pipenv run test_unit
```

Tests are structured into two modules `spec` for unit tests and `integration` for feature tests.

## Approach

Account statement printing is achieved using three objects:

- an `Account` object which tracks the a list of the users transactions.
- a `Transactions` object which is stored inside the `Account` object and tracks information about individual transactions.
- a `Printer` object as utility dependency of the `Account` object which accepts an array of transactions and prints a formatted statement using them.

Below is the object domain model for the three objects:

| Object | Message |
| --- | --- |
| Account | #transactions |
| | #transact(amount) |
| | #print_statement |

| Object | Message |
| --- | --- |
| Transaction | #value |
| | #date |
| | #is_debit |
| | #get_formatted_date |

| Object | Message |
| --- | --- |
| Printer | #print_statement |

I explored using separate `withdraw` and `deposit` methods but settled on using a single `transact` method on the `Account` object as it was clearer and cut down on repeated code. 

Furthermore, I also went back and forth on whether to directly submit a new transaction object to the `Account` object's `transact` method, but decided in the end that it was more user friendly to be able to simply specify the amount of a transaction that took place and then dependency inject the `Transaction` class into the `Account` object where it could then be used to dynamically created new instances of `Transaction` when required.

## Acceptance criteria

- User can deposit money
- User can withdraw money
- User can print a statement:
```
date       || credit  || debit   || balance
14/01/2012 ||         || 500.00  || 2500.00
13/01/2012 || 2000.00 ||         || 3000.00
10/01/2012 || 1000.00 ||         || 1000.00
```

## User Stories
```
AS A conscientious saver
SO THAT I can save for the future
I NEED to be able deposit funds into my account
```

```
AS A reckless spender
SO THAT I can take buy the things I want
I NEED to be able to withdraw funds from my account
```

```
AS A careful money manager
SO THAT I know what's going on with my account
I NEED to able to see a printed account statement
```
