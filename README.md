## Experiments with Large Language Models (LLMs) and Langchain framework.

Prompt:
*Write a python code for a simple calculator app the does addition, substraction,
 division, and multiplication. Save the code in the current directory as calculator.py.
 Test the script for two inputs, and then save the tests results in tests.txt file.*


```shell     
> Entering new AgentExecutor chain...

Action:
\```
{
  "action": "Python REPL",
  "action_input": "
# Create calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Test calculator.py
print(add(2, 3))
print(subtract(2, 3))
print(multiply(2, 3))
print(divide(2, 3))

# Save tests results in tests.txt
with open('tests.txt', 'w') as f:
    f.write(str(add(2, 3)) + '\n')
    f.write(str(subtract(2, 3)) + '\n')
    f.write(str(multiply(2, 3)) + '\n')
    f.write(str(divide(2, 3)) + '\n')
"
}
\```


Observation: SyntaxError('unterminated string literal (detected at line 22)', ('<string>', 22, 30, "    f.write(str(add(2, 3)) + '", 22, 30))
Thought: I need to check if the code works
Action:
\```
{
  "action": "Python REPL",
  "action_input": "
# Create calculator.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Test calculator.py
print(add(2, 3))
print(subtract(2, 3))
print(multiply(2, 3))
print(divide(2, 3))

# Save tests results in tests.txt
with open('tests.txt', 'w') as f:
    f.write(str(add(2, 3)) + '\n')
    f.write(str(subtract(2, 3)) + '\n')
    f.write(str(multiply(2, 3)) + '\n')
    f.write(str(divide(2, 3)) + '\n')
"
}


> Finished chain.
```
