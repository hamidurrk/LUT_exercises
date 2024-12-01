'''
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitate Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
'''

import random

rules_statement = [
    "Scissors cuts Paper",
    "Paper covers Rock",
    "Rock crushes Lizard",
    "Lizard poisons Spock",
    "Spock smashes Scissors",
    "Scissors decapitate Lizard",
    "Lizard eats Paper",
    "Paper disproves Spock",
    "Spock vaporizes Rock",
    "Rock crushes Scissors"
]

class GameGraph():
    def __init__(self, rules_statement):
        self.graph = {}
        self.nodes = {}
        self.edges = {}
        self.node_count = 0
        self.edge_count = 0
        self.rules_statement = rules_statement
        self.rules = []
        self.options = set()
        for node in rules_statement:
            node = node.split(" ")
            self.rules.append(node)
            self.options.add(node[0])
            self.add_edge(node[0], node[2])
    
    def __str__(self):
        return str(self.graph)
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
            self.nodes[u] = self.node_count
            self.node_count += 1
        if v not in self.graph:
            self.graph[v] = []
            self.nodes[v] = self.node_count
            self.node_count += 1
        self.graph[u].append(v)
        self.edges[(u, v)] = self.edge_count
        self.edge_count += 1
    
    def successors(self, u):
        return self.graph[u]

    def predecessors(self, u):
        predecessors = [node for node in self.graph if u in self.graph[node]]
        return predecessors

    def has_successor(self, u, v):
        return v in self.graph[u]
    
    def has_predecessor(self, u, v):
        return u in self.graph[v]
    
    def search_rule(self, u, v):
        for rule in self.rules:
            if rule[0] == u and rule[2] == v:
                return rule[1]
        return None
    
class Game():
    def __init__(self):
        self.rules_statement = [
            "Scissors cuts Paper",
            "Paper covers Rock",
            "Rock crushes Lizard",
            "Lizard poisons Spock",
            "Spock smashes Scissors",
            "Scissors decapitate Lizard",
            "Lizard eats Paper",
            "Paper disproves Spock",
            "Spock vaporizes Rock",
            "Rock crushes Scissors"
        ]
        self.G = GameGraph(rules_statement)
        print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
        
    def start(self):
        while True:
            user_input = input("Choose Rock, Paper, Scissors, Lizard, or Spock (type 'exit' to quit): ").capitalize()
            if user_input == "Exit":
                break
            if user_input not in self.G.options:
                print("Invalid input. Please try again.")
                continue
            else:
                computer_input = random.choice(list(self.G.options))
                print(f"Computer chose {computer_input}.")
                
            print(user_input)
            while True:
                user_continuation_input =  input("Do you want to play again? (yes/no): ").capitalize()
                if user_continuation_input == "No":
                    return
                elif user_continuation_input == "Yes":
                    break
                else:
                    print("Invalid input. Please try again.")
                    continue
        
Game().start()

