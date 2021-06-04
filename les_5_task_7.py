import json

result = []
profit = {}
average = []

with open('text_7.txt', 'r', encoding='utf-8') as file_read:
    while True:
        line = file_read.readline().split()
        if not line:
            break

        profit[line[0]] = float(line[-2]) - float(line[-1])

        if profit[line[0]] > 0:
            average.append(profit[line[0]])



result = [profit, {'average_profit': sum(average) / len(average)}]

with open('text_77.json', 'w', encoding='utf-8') as file_write:
    json.dump(result, file_write, ensure_ascii=False)