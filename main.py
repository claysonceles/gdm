import social as soc
import sys

n_nodes = 1150

W_lim = 2*388800/(9)
k_clique = 4

if len(sys.argv) != 2:
	print "Wrong arguments."
	exit()

dataset = sys.argv[1];

socialGraph = soc.readSocialGraph(dataset,n_nodes)
soc.plotWeightedCommunities(socialGraph,W_lim,k_clique,n_nodes)

socialGraph = soc.generateBASyntheticGraph(400, 12)
soc.plotUnweightedCommunities(socialGraph,4,n_nodes)

		#plt.show() # display

