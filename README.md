
## How to use
```
>>> from src.account import Account
>>> from src.printer import Printer
>>> from src.transaction import Transaction
>>> p = Printer()
>>> acc = Account(0, Transaction, p)
>>> acc.transact(200)
>>> acc.transact(50)
>>> acc.print_statement()
date       || credit  || debit   || balance
16/06/2020 ||         || 200.00  || 0.00   
16/06/2020 ||         || 50.00   || 200.00 
```

## Acceptance criteria

```
date       || credit  || debit   || balance
14/01/2012 ||         || 500.00  || 2500.00
13/01/2012 || 2000.00 ||         || 3000.00
10/01/2012 || 1000.00 ||         || 1000.00
```

## Interaction

How should we model the clients interaction with the `Account` object when making deposits and withdrawals?
- just directly pass in the amount to deposit:
  `account_object.deposit(200)`
- pass in a `Transaction` type object that records the time of the deposit or withdrawal:
  ```
  transaction_object = Transactio(Date, 200)
  account_object.transaction(transaction_object)
  ```

## Objects

| Object | Message |
| --- | --- |
| Account | #transactions |
| | #transaction(amount) |
| | #current_balance |
| | #print_statement |

| Object | Message |
| --- | --- |
| Transaction | #type |
| | #amount |
| | #date |

## Mocking

Should I be mocking the `date` part of my transaction

At the moment my `account` object prints a statement and when I say
`transact` it takes a transaction and creates a new transaction object with the time with `date.now`
