import argparse
import math

parser = argparse.ArgumentParser(description="Loan Calculator")

parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

i = float(args.interest) / 1200
msg = ''

if args.payment and args.principal:
    principal = float(args.principal)
    payment = float(args.payment)
    x = payment / (payment - i * principal)
    payment_period = math.ceil(math.log(x, i + 1))
    years = int(payment_period / 12)
    months = payment_period % 12
    msg = f'It will take {years} years and {months} months to repay this loan!'
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
    
print(msg)
