from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np

# La partie B
# Question 1.1 : Créer un réseau Bayéssien
baysNet = BayesianNetwork()
list_evenement = ['L', 'I', 'S', 'N', 'R']

for i in list_evenement:
    baysNet.add_node(i)

baysNet.add_edge('L', 'N')
baysNet.add_edge('I', 'N')
baysNet.add_edge('S', 'N')
baysNet.add_edge('S', 'R')
baysNet.add_edge('N', 'R')

# Question 1.2 : Ajoutez des CPD (tables des probabilités) à chaque noeud
cpd_I = TabularCPD('I', variable_card=2, values=[[0.21], [0.79]])
cpd_L = TabularCPD('L', 2, [[0.08, ], [0.92]])
cpd_S = TabularCPD('S', 2, [[0.12], [0.88]])
"""
    :variable_card = 当前N的变量状态，如True或False
    :values = N的条件概率分布表
    :evidence = 条件变量列表
    :evidence_card = 条件变量各有多少个状态，如S有2个：True或False。L也有两个：T或F
"""
cpd_N = TabularCPD('N', variable_card=2, values=[[0.92, 0.88, 0.79, 0.73, 0.22, 0.08, 0.17, 0.03],
                                                 [0.08, 0.12, 0.21, 0.27, 0.78, 0.92, 0.83, 0.97]
                                                 ],
                   evidence=['L', 'S', 'I'], evidence_card=[2, 2, 2])
cpd_R = TabularCPD("R", variable_card=2, values=[[0.38, 0.08, 0.16, 0.05],
                                                 [0.62, 0.92, 0.84, 0.95]
                                                 ],
                   evidence=['N', 'S'], evidence_card=[2, 2])

print(cpd_I,"\n",cpd_L,"\n",cpd_S,"\n",cpd_N,"\n",cpd_R)
print("\n\n********************************************************\n\n")
baysNet.add_cpds(cpd_R, cpd_N, cpd_L, cpd_S, cpd_I)

# Question 1.3 : Vérifiez si le modèle est correctement créé en utilisant bayesNet.check_model()
flag = baysNet.check_model()
print("check_model s'il est vrai: ",flag)

# Question 1.4 : Création d'un solveur qui utilise l'élimination de variables
solver = VariableElimination(baysNet)
solver.induced_graph(['L', 'N', 'R', 'I', 'S'])

# Question 2.2 : Calculer la probabilité de « Le projet ne doit pas être pris en compte (non noté) »
result = solver.query(['N'])
print(result)

# Question 2.3 : Calculez la probabilité de " Le projet ne doit pas être pris en compte (pas de note) étant donné que le modèle ML l'a signalé"
# p(N | L) = p(N,L) / P(L) = 0.0608 / 0.08 = 0.76
p_N_parentL = solver.query(['N'],evidence={"L":0})
print(p_N_parentL)

# Question 2.4 : Trouver les (in)dépendances entre les variable
independance = baysNet.get_independencies()
print(independance)
