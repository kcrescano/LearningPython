import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if args.interest is None or args.interest < 0 or \
        (args.type != "annuity" and args.type != "diff") or \
        (args.type == "diff" and args.payment is not None) or \
        len([x for x in [args.principal, args.payment, args.periods] if x is not None]) < 2 or \
        (args.principal is not None and args.principal < 0) or \
        (args.periods is not None and args.periods < 0) or \
        (args.payment is not None and args.payment < 0):
    print("Incorrect parameters")
    exit()

i = args.interest / (12 * 100)

if args.periods is None:
    n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
    years = n // 12
    months = n % 12
    if years == 0:
        print(f"It will take {months} months to repay this loan!")
    elif months == 0:
        print(f"It will take {years} year{'s' if years != 1 else ''} to repay this loan!")
    else:
        print(
            f"It will take {years} year{'s' if years != 1 else ''} and {months} month{'s' if months != 1 else ''} to repay this loan!")
    print(f"Overpayment = {args.payment * n - args.principal:.0f}")

elif args.payment is None:
    if args.type == "annuity":
        payment = math.ceil(args.principal * (i * pow(1 + i, args.periods)) / (pow(1 + i, args.periods) - 1))
        print(f"Your annuity payment = {payment}!")
        print(f"Overpayment = {payment * args.periods - args.principal:.0f}")
    else:
        total = 0
        for m in range(1, args.periods + 1):
            payment = math.ceil(
                args.principal / args.periods + i * (args.principal - (args.principal * (m - 1)) / args.periods))
            total += payment
            print(f"Month {m}: payment is {payment}")
        print(f"\nOverpayment = {total - args.principal:.0f}")

elif args.principal is None:
    principal = math.floor(args.payment / ((i * pow(1 + i, args.periods)) / (pow(1 + i, args.periods) - 1)))
    print(f"Your loan principal = {principal}!")
    print(f"Overpayment = {args.payment * args.periods - principal:.0f}")
