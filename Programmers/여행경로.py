tickets = [['ICN', 'A'], ['ICN', 'A'], ['A', 'ICN'], ['A' , 'C']]

from collections import defaultdict

airports = defaultdict(list)
visited = defaultdict(list)
A = []

def make_airports(airport,visited):
    airports[airport[0]].append(airport[1])
    visited[airport[0]].append(False)
    return

def dfs(airport, Answer, Tickets):
    if A:
        return
    
    if len(Answer) == len(Tickets) + 1:
        aa = Answer.copy()
        A.append(aa)
        return
    
    if airport in airports:
        for i in airports[airport]:
            if airports[airport]:
                if not visited[airport][airports[airport].index(i)]:
                    visited[airport][airports[airport].index(i)] = True
                    Answer.append(i)
                    dfs(i, Answer, Tickets)
                    visited[airport][airports[airport].index(i)] = False
                    Answer.pop()

def solution(tickets):
    answer = ["ICN"]
    cnt = 1
    print(answer)
    for airport in tickets:
        make_airports(airport, visited)
    
    for airport_list in airports.values():
        if airport_list:
            airport_list.sort()
    print(airports)
    dfs("ICN", answer, tickets)
    print(A)
    
    return A

solution(tickets)