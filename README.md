# tech201_python_scripting
tech201_python_scripting
# Python Scripting
## What is scripting and how is it different to coding/programming?

Scripting is the use of shorter chunks of code used to automate processes that would otherwise be done step by step. Typically scripting would be used to tell the static part of your code to do something, but not for that static content. Coding and Programming is a catch all term for the use of coding in IT.

## Why are scripts useful? How are they used?
Scripts are useful for With scripting, you can control other programs that aren’t yours using API's. Scripts are one file and do not need o be compiled.

## Why Python for scripting? Why not another language?
Scripts are almost always written in "high level" languages (easy to read) such as Python, Bash, Ruby, Node.js. Python has an added benefit of having a huge range of libraries and learning materials. Python can transfer data to other languages and operating systems for gaining the benefit of a low level language, this is called language interoperability.



## Why is scripting important for DevOps engineers?
Scripting is useful for automating tasks, DevOps have many repetitive tasks that have to be done regularly.

## 10 examples of ways we can use scripts in DevOps (for example - Python script to query a database etc.)
- Powershell automation for compiling, testing and building code. 
- Bash for automatic deploying code to github
- a python script for importing query data from an sql database
- Bash and powershell for file navigation.
- shell scripting in Bash and powershell with python
- scripting with linux/Bash
- Shell script to send data from one file to another
- Find IP address using shell script or Python
- 


## List 10 of the most important Python Modules for DevOps (link to each ones documentation if possible)
-Sys
-Os
-Subprocesses
-Math
-Random
-DateTime
-JSON

## Example of a useful Python script, as code block (optional extra)

```
filename = "testfile.txt"
filepath = os.path.join(path, filename)

#write to the new file
with open(os.path.join(path, filename),"w", ) as file1:
    toFile = "Contents of my new file"
    file1.write(toFile)

print("File" + filename + "created in" + directory + " folder")
```

## We will dive into scripting itself after lunch.

## Resources
https://devopscube.com/linux-shell-scripting-for-devops/

