
#Kutay Özbay 270201017 HW3

#Imports



import random


"""
S ----> States

A ----> Actions

R ----> Reward function which is number of fish caught

P ----> Probability of transaction


"""


S = [* range(0, 101)]
A = [* range(0, 101)]



def value_iterations(S, A):
    V = {s:0 for s in S}
    gamma = 1
    optimal_policy = {s:0 for s in S}
    while True:
        oldV = V.copy()
        for s in S:
            Q = {}
            for a in A:
                summ = 0
                for s_next in S:
                    if s >= a and (s-a)*1.75 < 100:
                        p1 = (s-a)* 1
                        p2 = (s-a)* 1.25
                        p3 = (s-a)* 1.5
                        p4 = (s-a)* 1.75
                        p_list = [p1, p2, p3, p4]
                        temp = random.choices(p_list, weights=(2, 3, 3, 2), k=1)
                        if temp == p1 or temp == p4:
                            p = 0.2
                            if temp == p1:
                                n = p1
                            else:
                                n = p4
                        else:
                            p = 0.3
                            if temp == p2:
                                n = p2
                            else:
                                n = p3
                        D= round(n)
                        summ = summ + gamma * (p * oldV[D])
                Q[a] = a + summ

            V[s] = float("{:.2f}".format(max(Q.values())))
            optimal_policy[s] = max(Q, key=Q.get)

        if V == oldV or optimal_policy[57] == 0:
            break

    return V, optimal_policy


V, optimal_policy = value_iterations(S, A)

print(V)

print(optimal_policy)



def policy_iterations(S, A):
    policy = {s: A[0] for s in S}
    gamma = 0.9
    while True:
        oldV = V.copy()
        for s in S:
            Q = {}
            for a in A:
                summ = 0
                for s_next in S:
                    if s >= a and (s - a) * 1.75 < 100:
                        p1 = (s - a) * 1
                        p2 = (s - a) * 1.25
                        p3 = (s - a) * 1.5
                        p4 = (s - a) * 1.75
                        p_list = [p1, p2, p3, p4]
                        temp = random.choices(p_list, weights=(2, 3, 3, 2), k=1)
                        if temp == p1 or temp == p4:
                            p = 0.2
                            if temp == p1:
                                n = p1
                            else:
                                n = p4
                        else:
                            p = 0.3
                            if temp == p2:
                                n = p2
                            else:
                                n = p3
                        D = round(n)
                        summ = summ + gamma * (p * oldV[D])
                Q[a] = a + summ

            V[s] = float("{:.2f}".format(max(Q.values())))
            optimal_policy[s] = max(Q, key=Q.get)

        if V == oldV or optimal_policy[57] == 0:
            break

    return policy

def policy_evaluation(policy, S):

    V = {s: 0 for s in S}

    while True:
        oldV = V.copy()

        for s in S:

            a = policy[s]

            V[s] = R(s, a) + sum(P(s_next, s, a) * oldV[s_next]
                                 for s_next in S)
        if oldV == V:
            break
    return V


def policy_improvement(V, S, A):
    policy = {s: A[0] for s in S}

    for s in S:
        Q = {}
        for a in A:
            summ = 0
            for s_next in S:
                if s >= a and (s - a) * 1.75 < 100:
                    p1 = (s - a) * 1
                    p2 = (s - a) * 1.25
                    p3 = (s - a) * 1.5
                    p4 = (s - a) * 1.75
                    p_list = [p1, p2, p3, p4]
                    temp = random.choices(p_list, weights=(2, 3, 3, 2), k=1)
                    if temp == p1 or temp == p4:
                        p = 0.2
                        if temp == p1:
                            n = p1
                        else:
                            n = p4
                    else:
                        p = 0.3
                        if temp == p2:
                            n = p2
                        else:
                            n = p3
                    D = round(n)
                    summ = summ + gamma * (p * oldV[D])
            Q[a] = a + summ

        policy[s] = max(Q, key=Q.get)

optimal_policy_iter = policy_iterations(S, A)
print(optimal_policy_iter)

#Policy Iterartion is more time efficient than Value Iteration
#When discount factor taken as 1 future is become more 	insignificant