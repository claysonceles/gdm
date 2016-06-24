import socialNet as soc
import meetingsGen as meet
import sys

n_nodes = 1150

W_lim = 2*388800/(9)
k_clique = 4

if len(sys.argv) != 2:
	print "Wrong arguments."
	exit()

dataset = sys.argv[1];

magic_number = [500,25, 6,0.5,0.001]

#socialGraph = soc.generateBASyntheticGraph(400, 12)
#soc.plotUnweightedCommunities(socialGraph,4,400)

#socialGraph = soc.readSocialGraph(dataset,n_nodes)
#soc.plotWeightedCommunities(socialGraph,W_lim,k_clique,n_nodes)

socialGraph = soc.generateGaussian(500,10, 10,0.5,0.002);
soc.plotUnweightedCommunities(socialGraph,3,400)

meet.generateGroupSet(500,30)
