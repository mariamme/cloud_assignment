# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

from functools import reduce
import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):

    data = yield context.call_activity('GetInputDataFn', "macont")
    map = []
    for i in data:
        map.append(context.call_activity("Mapper", i))
    
    res = yield context.task_all(map)

    result1 = reduce(lambda x, y :x + y, res)

    result2 = yield context.call_activity('Shuffler', result1)

    result3 = []
    for j in result2:
        res1 = yield context.call_activity('Reducer', (j, result2[j]))
        result3.append(res1)

    return result3

main = df.Orchestrator.create(orchestrator_function)