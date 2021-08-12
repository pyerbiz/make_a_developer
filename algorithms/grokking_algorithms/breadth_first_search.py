"""simple graph based algorithms"""

# hash table -> graph -> queue
# First implement a graph (a hash table with the graph values)

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "clairem"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

person_is_seller = lambda x: x[-1] == "m"
search_queue = deque()
search_queue += graph["you"]  # your neighbours


def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a seller")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
