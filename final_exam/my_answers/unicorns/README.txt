my_answers/unicorns contains the following files:
    (csv and tsv data files to construct graph)
--- companies.csv
--- investments.csv
--- unicorns.tsv
--- investors_in_unicorns.tsv
--- future_unicorns.tsv
--- investors_in_future_unicorns.tsv
--- unicorns_solution_graph1.py (python code for the first graph)
--- unicorns_solution_graph2.py (python code for the second graph)
--- unicorns_solution_graph3.py (python code for the third graph)
--- README.txt


Answers for (a)~(e):
1st Graph:
--- number of connected components:139
--- As you will see in graph "log(degree_distribution) ~ rank" generated by "unicorns_solution_graph1.py", the degree values after log transformation
nearly forms a linear line with rank, which indicates power law. The top10
degree distribution before log transformation is shown below:
	number 0: Airbnb 103
	number 1: Dropbox 77
	number 2: Nextdoor 73
	number 3: Lookout 73
	number 4: Stripe 71
	number 5: Domo 70
	number 6: Ola 70
	number 7: Snapchat 69
	number 8: Jet 68
	number 9: Uber 67
--- top 10 eigenvector centrality of nodes are shown below:
	number 0: Airbnb 0.190040439483
	number 1: Dropbox 0.16692387733
	number 2: Stripe 0.15427781202
	number 3: Lookout 0.153681014236
	number 4: Nextdoor 0.151887565969
	number 5: Instacart 0.151163562039
	number 6: Jawbone 0.14854995163
	number 7: Snapchat 0.147953472124
	number 8: Domo 0.145398666345
	number 9: Ola 0.141618955943
--- diameter:4
--- clustering coefficient = 0.5368910527667101
Compared to random graph clustering coefficient, this is a small-world graph.

2nd Graph:
--- number of connected components: 177
--- As you will see in graph "log(degree_distribution) ~ rank" generated by "unicorns_solution_graph1.py", the degree values after log transformation
nearly forms a linear line with rank, which indicates power law. The top10
degree distribution before log transformation is shown below:
	number 0: Airbnb 131
	number 1: Dropbox 105
	number 2: Nextdoor 99
	number 3: Lookout 97
	number 4: Stripe 94
	number 5: Domo 92
	number 6: Uber 91
	number 7: Slack 89
	number 8: Jet 88
	number 9: Snapchat 86

--- top 10 eigenvector centrality of nodes are shown below:
	number 0: Airbnb 0.169530788046
	number 1: Dropbox 0.154142145825
	number 2: Lookout 0.141982459982
	number 3: Nextdoor 0.141645433259
	number 4: Stripe 0.141395599976
	number 5: Jawbone 0.136087693294
	number 6: Instacart 0.136009695394
	number 7: Domo 0.135275326479
	number 8: Slack 0.132659392033
	number 9: Snapchat 0.129651158625
--- diameter: 4
--- clustering coefficient = 0.530878238936
Compared to random graph clustering coefficient, this is a small-world graph.
--- future unicorn that is disconnected from all current unicorns.
	Edaijia
	Harry's Razor Company
	Postmates
	Privia Health
	Takealot Online
	Uxin Pai

3rd Graph:
--- number of connected components: 40932
--- As you will see in graph "log(degree_distribution) ~ rank" generated by "unicorns_solution_graph1.py", the degree values after log transformation
nearly forms a linear line with rank, which indicates power law. The top10
degree distribution before log transformation is shown below:
	number 0: FundersClub 3303
	number 1: Dropbox 3303
	number 2: Uber 3299
	number 3: Airbnb 3263
	number 4: Karma 3210
	number 5: AngelList 3191
	number 6: Mattermark 3179
	number 7: Ark 3042
	number 8: Zesty 2901
	number 9: Stripe 2891
--- top 10 eigenvector centrality of nodes are shown below:
	number 0: Mattermark 0.0459
	number 1: Zesty 0.0451
	number 2: E la Carte 0.0449
	number 3: Experiment 0.0446
	number 4: LeadGenius 0.0437
	number 5: Zencoder 0.0434
	number 6: Airbnb 0.0423
	number 7: Dropbox 0.0421
	number 8: Homejoy 0.0419
	number 9: PlanGrid 0.0416
--- diameter: 6
--- clustering coefficient = 0.70
Compared to random graph clustering coefficient, this is a small-world graph.