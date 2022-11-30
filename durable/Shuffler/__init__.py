# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(input: list) -> dict:
    res = {}
    for i in input:
        (word, counts) = i
        j = res.get(word)

        if j is None:
            j = []
            j.append(counts)
        else:
            j.append(counts)
            
        res[word] = j
        
    return res