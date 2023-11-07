import argparse
import math

parser = argparse.ArgumentParser(description="Loan Calculator")

parser.add_argument("--payment")
parser.add_argument("--principal", default=0.)
parser.add_argument("--periods")
parser.add_argument("--interest", default=0.)
parser.add_argument("--type")

args = parser.parse_args()

i = float(args.interest) / 1200
paid_total = 0
msg = 'Incorrect parameters'

principal = args.principal
payment = args.payment
periods = args.periods
interest = args.interest
type = args.type

annuity = args.type == 'annuity' and interest
diff = args.type == 'diff' and bool(principal and periods and interest)

if annuity:
    if payment and principal:
        principal = float(principal)
        payment = float(payment)
        x = payment / (payment - i * principal)
        payment_period = math.ceil(math.log(x, i + 1))
        years = int(payment_period / 12)
        months = payment_period % 12
        msg = f'It will take {years} years'
        if months:
            msg += f' and {months} months'
        msg += ' to repay this loan!'
        msg += f'\nOverpayment = {payment_period * payment - principal}'
    elif args.periods and args.principal:
        principal = float(args.principal)
        periods = float(args.periods)
        payment_period = principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
        msg = f'Your monthly payment = {math.ceil(payment_period)}!'
    else:
        payment = float(args.payment)
        periods = float(args.periods)
        payment_period = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
        msg = f'Your loan principal = {math.ceil(payment_period)}!'
elif diff:
    for x in range(int(periods)):
        principal = float(principal)
        periods = float(periods)
        monthly = math.ceil((principal / periods) + i * (principal - principal * (x) / periods))
        print(f'Month {x}: payment is {monthly}')
        paid_total += monthly
    msg = f'Overpayment = {paid_total - int(principal)}'

if int(principal) < 0:
    msg = "Incorrect parameters"
if float(interest) < 0:
    msg = "Incorrect parameters"
if payment:
    if float(payment) < 0:
        msg = "Incorrect parameters"
if periods:
    if int(periods) < 0:
        msg = "Incorrect parameters"
print(msg)
