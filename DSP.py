import numpy as np

def clean(raw, start_time):
    return list(filter(lambda x: x[1] > start_time, map(lambda x: [int(x.split(",")[0]),int(x.split(",")[1][:-1]), ''], raw)))

def avg_of_mid(raw, bot, top):
    mid = sorted(raw, key=lambda x: x[0])
    midran = range(int(len(mid)*bot), int(len(mid)*top))
    add = 0
    for i in midran:
        add = add + mid[i][0]
    avg = round(add/len(midran),2)
    return avg

def add_avg(avg, data):
    for i in range(len(data)):
        data[i].append(avg)
    return data

def label_R(data):
    f = open('process_r.txt', 'w')
    st = ''
    for i in range(len(data)):
        if data[i][0] > 600 and data[i][0] > data[i-1][0] and data[i][0] > data[i+1][0]:
            data[i][2] = 'R'
        st = st + str(data[i][0]) + ',' + str(data[i][1]) + ',' + str(data[i][2]) + ',' + str(data[i][3]) + "\n"
    f.write(st)
    return data

def calc_R_rate(data):
    begin = 0
    end = 0
    time = []
    for i in range(len(data)):
        if data[i][2] == 'R':
            end = data[i][1]
            time.append((end - begin))
            begin = data[i][1]
    time.pop(0)
    rate = []
    for i in time:
        rate.append(round(61440/i))
    print(time)
    print(rate)
    return(time)



def main():
    f = open('Joris_9.txt', 'r')
    l = f.readlines()
    raw = clean(l, 29366)
    f.close()
    avg = avg_of_mid(raw, 0.25, 0.75)
    a = add_avg(avg, raw)
    k = label_R(a)
    calc_R_rate(k)


if __name__ == '__main__':
    main()
