# Try to utilize the template given to solve the task.        
import asyncio

async def square_number(num):
    return num ** 2

async def parallel_execution(number):
    tasks = [asyncio.create_task(square_number(num)) for num in number]
    return await asyncio.gather(*tasks)
  
    # tasks = []
    # for num in nums:
    #     tasks.append(asyncio.create_task(square(num)))
    # return await asyncio.gather(*tasks)

numbers = [int(i) for i in input().split()]
results = asyncio.run(parallel_execution(numbers))
print(*results)
