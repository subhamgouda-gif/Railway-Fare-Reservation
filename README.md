# Railway Fare and Reservation Calculator

Calculates sample fares for multiple passengers using distance slabs, class rates, age concessions, reservation fees, and a cancellation penalty.

## What it demonstrates

Variables, numbers, strings, tuples, lists, loops, conditions, arithmetic and comparison operators, and tuple unpacking. No imports or user-defined functions are used.

## Sample assumptions

- The first 100 km use the class base rate, the next 200 km use 1.5 times the rate, and further distance uses twice the rate.
- Children aged 12 or younger receive 50% off the distance fare; passengers aged 60 or older receive 40% off it.
- Reservation fee is added after the age concession.
- Cancellation fee is 25% of the calculated fare.

Passenger and class examples are editable at the top of `main.py`.

## Algorithm

1. Find the passenger's class rate and reservation fee.
2. Calculate distance fare by consuming each distance slab.
3. Apply an age concession to the distance fare, then add the reservation fee.
4. If the action is cancellation, calculate the fee and refund; otherwise print the booking fare.

## Pseudocode

```text
FOR each passenger
    find class rate
    IF passenger or class is invalid, report invalid record
    ELSE calculate fare by distance slabs
        apply age concession and add reservation fee
        IF cancelled, calculate cancellation fee and refund
        ELSE print reservation fare
```

## Flowchart

```text
START -> Read passenger -> Find class and validate
       -> Valid? --no--> Print invalid record
            | yes
            v
       Calculate slab fare -> Apply concession and reservation fee
            -> Cancelled? --yes--> Calculate refund
                            --no--> Print booking fare
       -> Next passenger or END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://railway-fare-reservation-abfugneccsuk2wqnenw46d.streamlit.app/
