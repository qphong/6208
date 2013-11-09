from rockSample import *
from rSmdpSolver import *
from random import *


def main():
	#discount of the RB
	dis_RB=0.01
	flag=1

	rs_Mmdp=MDP()

	init_horizon=rs_Mmdp.H

	for i in range(init_horizon):
		if flag==1:
			rs_Mmdp.calTrans()
			rs_Mmdp.calRewards()
			rs_Mmdp.calRB()

		m_policy=RS_mdp_solver(rs_Mmdp,dis_RB)

			#execute part
		flag=rs_Mmdp.execution(m_policy)



if __name__=="__main__":
	main()