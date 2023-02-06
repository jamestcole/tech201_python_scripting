#Sys module scripts
import math
import sys
import os
print(sys.version)

print(os.getcwd())
#change directory
#os.chdir("C:/Users/James Cole/PycharmProjects/python/tech201_python_scripting/tech201_python_scripting/scripting_intro.py")
#make new directory
#os.mkdir("path")
#subprocessmodule
#can be used to create and ineract with subprocesses managed by our python interpreter.
import subprocess
# same folder can just be file name
subprocess.run(["python","HelloWorld.py"])

# Math module scripts
import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)

# Random module scripts
import random
random = random.randrange(1, 10)
print(random)

# DateTime module scripts
import datetime
whatisthedate = datetime.datetime.now()
print(whatisthedate)

# JSON module script
import json
x = {
    "name": "John",
    "age": 30,
    "city": "London"
}
y = json.dumps(x)
print(y)