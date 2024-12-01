# L12-T1: Rock-Paper-Scissors-Lizard-Spock
#
# Written by: Md Hamidur Rahman Khan
#

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
        self.G = GameGraph(self.rules_statement)
        print("Welcome to Rock-Paper-Scissors-Lizard-Spock!")
        
    def start(self):
        while True:
            user_input = input("Choose Rock, Paper, Scissors, Lizard, or Spock (type 'exit' to quit): ").capitalize()
            if user_input == "Exit":
                break
            if user_input in self.G.options:
                computer_input = random.choice(list(self.G.options))
                print(f"Computer chose {computer_input}.")
                if user_input == computer_input:
                    print("Tie!")
                else:
                    if self.G.has_successor(user_input, computer_input):
                        print(f"You won! {user_input} {self.G.search_rule(user_input, computer_input)} {computer_input}.")
                    else:
                        print(f"You lost! {computer_input} {self.G.search_rule(computer_input, user_input)} {user_input}.")
            else:            
                print("Invalid input. Please try again.")
        
            while True:
                user_continuation_input =  input("Do you want to play again? (yes/no): ").strip().lower()
                if user_continuation_input in ["no", "n"]:
                    print("Thanks for playing! Goodbye!")
                    return
                elif user_continuation_input in ["yes", "y"]:
                    break
                else:
                    print("Invalid input. Please try again.")
                    
Game().start()

