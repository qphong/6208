import battlesship as bat
from LearnTrueMdp import *

def main():

	battle_p = Battle_Ship()

	flag=1

	print battle_p.true_Model

	while True:

		if flag==1:
			battle_p.sample_Mdps=bat.getRandomSols(battle_p.obs, battle_p.Sample_Size)
			battle_p.bel=[1.0/battle_p.Sample_Size]*battle_p.Sample_Size

		battle_p.calRB(battle_p.sample_Mdps, battle_p.obs, battle_p.H)

		#print "RB"
		#print battle_p.RB

		#print "sample_Mdps:", battle_p.sample_Mdps[0]

		action=battle_p.ActionSelection(battle_p.sample_Mdps)

		result=battle_p.Execution(battle_p.sample_Mdps, action)

		flag = result[1]

		#print battle_p.bel
		print battle_p.taken_steps

		if result[0]:
			
			break


if __name__=="__main__":
	main()





