# This file updates the README.md file with the questions
# It does this using the rcph helper files

import json, os

# edit readme.md file

with open('./src/.rcph/info.json', 'r', encoding='utf-8') as json_file:
    problems = json.load(json_file)

above_text = """# Quera Implementation Problems Bank

Here I have tried to solve the problems of implementing Quora. I have also used a Python program to update the README.
"""

problems_table = "| problem letter (file) | problem name (link) | percentage of solve |\n"
problems_table += "|:---:|:---:|:---:|\n"

for problem in problems['problems']:
    problems_table += f"| [{problem['letter']}](./src/{problem['letter'].lower()}.cpp) | [{problem['name'] if problem['name'] else '-'}]({problem['link']}) | {problem['percentage']}% |\n" 
    
with open('./README.md', 'w') as readme:
    readme.write(above_text + '\n---\n' + problems_table)

print('readme file updated successfully!')

# edit testcases.md file

def addTestCase(letter, name, testcases):
    result =  f"""<details>
<summary>{letter + ' ' + name if name else ''}</summary>\n\n"""

    i = 1
    for inp, out in testcases:
        result += f"""### test case num {i}:\n
##### input:
```bash
{inp}
```
##### output:
```bash
{out}
```
"""
        i += 1
    
    result += "\n\n</details>\n\n"
    return result

testcase = ""
for problem in problems['problems']:
    tc = []
    
    testcase_path = os.path.join(os.getcwd(), 'src', '.rcph', 'tc', problem['letter'])
    
    i = 1
    while True:
        inp_path = os.path.join(testcase_path, f'{i}.in')
        out_path = os.path.join(testcase_path, f'{i}.ans')
        if os.path.exists(inp_path) and os.path.exists(out_path):
            with open(inp_path, 'r') as inp_file, open(out_path, 'r') as out_file:
                tc.append([inp_file.read(), out_file.read()])
            i += 1
        else:
            break
    
    if len(tc):
        testcase += addTestCase(problem['letter'], problem['name'], tc)

with open('./testcases.md', 'w') as tc_file:
    tc_file.write(testcase)
    
print('testcases file updated successfully!')