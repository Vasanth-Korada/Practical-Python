def hedgerMarket(stock_helper, cost_helper, profit_helper, counter, final_result):
    maxindex = profit_helper.index(max(profit_helper))
    maxval = cost_helper[maxindex]
    #print(" index ",maxindex,"  val ",maxval)
    i = 0
    while(i < int(stock_helper[1])):
        if stock_helper[2] > counter and stock_helper[2] >= counter+maxval:
            counter = counter+maxval
            final_result = final_result+((maxval*profit_helper[maxindex])/100)
        else:
            print(int(final_result))
            return final_result
        i = i + 1

    profit_helper.pop(maxindex)
    cost_helper.pop(maxindex)
    hedgerMarket(stock_helper, cost_helper, profit_helper, counter, final_result)


profit_helper = []
cost_helper = []
stock_helper = []

no_of_stocks = list(map(int,input().split()))
max_amount = list(map(int,input().split()))
profit_percentage = list(map(int,input().split()))

one = len(no_of_stocks)
two = len(max_amount)
three = len(profit_percentage)

i = 1
j = 1
k = 1
while(i <= one):
    stock_helper.append(float(no_of_stocks[i]))
while(j <= two):
    cost_helper.append(float(max_amount[j]))
while(k <= three):
    profit_helper.append(float(profit_helper[k]))



counter = 0
final_result = 0
val = hedgerMarket(stock_helper, cost_helper, profit_helper, counter, final_result)
