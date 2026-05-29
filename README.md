# ARTIFICIAL INTELLIGENCE ASSIGNMENT 5

**Name:** Jayasimha Reddy
**Roll Number:** SE24UCSE004
**Course:** Artificial Intelligence

---

# Overview

This assignment covers several important topics in Artificial Intelligence including adversarial search algorithms, intelligent recommendation systems, knowledge representation using Knowledge Graphs, and probabilistic reasoning using Bayesian Networks. The objective of the assignment is to understand the theoretical concepts and implement practical AI applications using Python.

---

# Question 1: Adversarial Search Algorithms

## Objective

The objective of this project is to implement and compare different adversarial search algorithms used in game-playing Artificial Intelligence systems.

## Algorithms Implemented

### 1. Minimax Search

Minimax is a decision-making algorithm used in two-player games. It assumes that one player attempts to maximize the utility value while the opponent attempts to minimize it. The algorithm explores the game tree and selects the optimal move.

### 2. Alpha-Beta Pruning

Alpha-Beta Pruning improves the efficiency of Minimax by eliminating branches that cannot influence the final decision. This significantly reduces the number of nodes explored while producing the same optimal result.

### 3. Heuristic Alpha-Beta Search

Heuristic Alpha-Beta Search combines pruning with heuristic evaluation functions. Instead of exploring the entire game tree, heuristic values are used to estimate the quality of intermediate states.

### 4. Monte Carlo Tree Search (MCTS)

Monte Carlo Tree Search uses random simulations to evaluate game states. It is widely used in modern game-playing AI systems because it can handle large search spaces efficiently.

## Problem Environment

A Tic-Tac-Toe game environment was created to test and compare the performance of the implemented algorithms.

## Features

* Tic-Tac-Toe board representation
* Move generation
* Game state evaluation
* Minimax implementation
* Alpha-Beta pruning
* Heuristic search
* Monte Carlo simulations

---

# Question 2: AI Based Travel Planner

## Objective

The objective of this project is to design an intelligent travel recommendation system using an existing knowledge base.

## Description

The Travel Planner recommends destinations, tourist attractions, food options, and estimates travel costs based on user inputs.

The user provides:

* Destination
* Budget
* Number of days

The system then generates a personalized travel plan.

## Knowledge Base

The planner stores information regarding:

* Tourist places
* Food recommendations
* Travel costs

for multiple cities including:

* Goa
* Hyderabad
* Delhi
* Bangalore

## Features

* Tourist place recommendation
* Food recommendation
* Personalized itinerary generation
* Cost assessment
* Budget validation

## AI Concept Used

Knowledge-based recommendation system.

---

# Question 3: Knowledge Graphs and Tools for Building Knowledge Graphs

## Objective

To understand the concept of Knowledge Graphs and explore the tools used to create and manage them.

## What is a Knowledge Graph?

A Knowledge Graph is a structured representation of entities and their relationships. Information is stored in the form of nodes and edges, allowing AI systems to understand connections between concepts.

## Example Used

Entities:

* Hyderabad
* Goa
* Delhi

Relationships:

* hasPlace
* hasFood
* locatedIn

Example:

Hyderabad → hasPlace → Charminar

Hyderabad → hasFood → Hyderabadi Biryani

Hyderabad → locatedIn → Telangana

## Advantages of Knowledge Graphs

* Efficient knowledge representation
* Better information retrieval
* Relationship discovery
* Semantic search
* Intelligent recommendation systems

## Tools Explored

### Neo4j

A graph database that stores data as nodes and relationships.

### Protégé

An ontology editor used for semantic web applications.

### RDFLib

A Python library used for RDF graph creation and manipulation.

### Apache Jena

A Java framework used for semantic web and linked-data applications.

### GraphDB

An RDF database designed for storing and querying knowledge graphs.

---

# Question 4: Bayesian Networks

## Objective

To explore modelling, problem representation, and inference using Bayesian Networks.

## What is a Bayesian Network?

A Bayesian Network is a probabilistic graphical model that represents variables and their conditional dependencies using a Directed Acyclic Graph (DAG).

Bayesian Networks help AI systems reason under uncertainty.

## Example Implemented

Medical Diagnosis Bayesian Network

Network Structure:

Disease → Fever

Disease → Cough

In this model:

* Disease is the cause
* Fever and Cough are symptoms

## Probabilities Used

* P(Disease)
* P(Fever | Disease)
* P(Fever | No Disease)
* P(Cough | Disease)
* P(Cough | No Disease)

## Inference

Using Bayes' Theorem, the probability of disease is calculated given the evidence that a patient has fever.

This demonstrates probabilistic inference and reasoning under uncertainty.

## Tools Explored

### GeNIe

Graphical modelling and inference tool for Bayesian Networks.

### Netica

Software package for probabilistic reasoning and decision support.

### pgmpy

Python library for probabilistic graphical models.

### BayesiaLab

Professional Bayesian Network modelling platform.

### Hugin

Commercial Bayesian Network and decision support software.

---

# Technologies Used

* Python 3
* Artificial Intelligence Algorithms
* Knowledge Representation
* Search Techniques
* Knowledge Graphs
* Bayesian Networks
* Probabilistic Reasoning

---

# Learning Outcomes

Through this assignment, the following concepts were studied and implemented:

* Adversarial Search
* Game Playing AI
* Recommendation Systems
* Knowledge Representation
* Knowledge Graph Construction
* Bayesian Modelling
* Probabilistic Inference
* Decision Making Under Uncertainty

---

# Conclusion

This assignment demonstrates practical applications of Artificial Intelligence techniques across different domains. Search algorithms were applied to game-playing environments, recommendation systems were used for travel planning, knowledge graphs were used for structured knowledge representation, and Bayesian Networks were used for reasoning under uncertainty. Together, these projects provide a strong foundation in core AI concepts and their real-world applications.
