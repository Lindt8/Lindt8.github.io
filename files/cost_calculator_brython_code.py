from browser import document, html

def caclulate_cost_distribution(people,expenses,decimal_precision=0,sorting_on=False):
    '''
    Inputs:
       people = list of strings of names
       expenses = list of integers/floats of the amounts paid by each person (length must be same as people)
    Outputs:
       cost_str = string describing the transfers necessary to make expenditures even across all people
    '''
    p,x = people,expenses
    dpadd = 0
    if decimal_precision > 0:
        dpadd = decimal_precision + 1
    if sorting_on:
        p = [i for _,i in sorted(zip(x,p))] # reorder people based on amount
        x.sort() # reorder corresponding amount list
    T = sum(x) # total expended
    o = [(T/len(x)) - i for i in x] # amount owed by each
    d  = [] # debtors
    da = [] # amounts owed (positive)
    c  = [] # collectors
    ca = [] # amounts to be collected (negative)
    for i in range(len(x)):
        if o[i]<0:
            c.append(p[i])
            ca.append(o[i])
        else:
            d.append(p[i])
            da.append(o[i])
    if sorting_on:
        c.reverse()
        ca.reverse()
    ci, di = 0, 0
    cost_str = ''
    max_name_len = max([len(i) for i in p])
    name_format_lstr = '{:>' + str(int(max_name_len)) + '}'
    name_format_rstr = '{:' + str(int(max_name_len)) + '}'
    transactions = []
    while abs(sum(da))>=1e-3:
        if da[di] <= -1*ca[ci]:
            d2c = da[di]
        else:
            d2c = -1*ca[ci]
        ca[ci] += d2c
        da[di] += -1*d2c
        transactions.append([d[di],d2c,c[ci]])
        if ca[ci]==0: ci += 1
        if da[di]==0: di += 1
    max_transfer = max([transactions[i][1] for i in range(len(transactions))])
    number_format_str = ' --({:' + str(dpadd+len(str(int(max_transfer)))) + '.' + str(int(decimal_precision)) + 'f})--> '
    for i in range(len(transactions)):
        cost_str += name_format_lstr.format(transactions[i][0]) + number_format_str.format(transactions[i][1]) + name_format_rstr.format(transactions[i][2]) + '\n'
    return cost_str


def show_values(event):
    sorting_on = False # order such that people who owe the most will pay first to who owes the most
    inputa = document["input16a"].value
    inputb = document["input16b"].value
    dp = int(document["select16"].value)
    rawp = inputa.split(',')
    people = [i.strip() for i in rawp]
    expenses = [float(i) for i in inputb.split(',')]
    cstr = caclulate_cost_distribution(people,expenses,decimal_precision=dp,sorting_on=False)
    cstr_list = cstr.split('\n')
    
    total_paid = sum(expenses)
    cost_per_person = total_paid/len(people)
    number_format_str = '{:' + str(len(str(int(total_paid)))) + '.' + str(int(dp)) + 'f}'
    total_paid_str =      'Total cost over all participants: ' + number_format_str.format(total_paid)
    cost_per_person_str = 'Fair cost for each participant:   '.format(str(len(people))) + number_format_str.format(cost_per_person)
    explanation_str = 'The following transfers will make the net expense per person even over all participants:'
    document["zone16"].clear()
    document["zone16"] <= (f"{total_paid_str}",html.BR())
    document["zone16"] <= (f"{cost_per_person_str}",html.BR(),html.BR())
    document["zone16"] <= (f"{explanation_str}",html.BR(),html.BR())
    for i in range(len(cstr_list)):
        document["zone16"] <= (f"{cstr_list[i]}",html.BR())

document["button16"].bind("click", show_values)