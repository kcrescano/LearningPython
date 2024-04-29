# Try to utilize the template given to solve the task.        
import asyncio

async def calculate_sum(numbers, future):
    future.set_result(sum(numbers))

async def calculate_product(numbers, future):
    result = 1
    for num in numbers:
        result *= num
    future.set_result(result)

async def calculate_results(numbers):
    sum_future = asyncio.Future()
    product_future = asyncio.Future()
    
    await asyncio.gather(
        calculate_sum(numbers, sum_future),
        calculate_product(numbers, product_future),
    )
    return sum_future.result(), product_future.result()

number = [int(i) for i in input().split()]
results = asyncio.run(calculate_results(number))
print(", ".join([str(i) for i in results]))
