#include <vector>
#include <string>

using namespace std;

vector<string> RS_mdp_solver(int numStates,
	vector< vector<string> > &trans_act, // state, actions
	vector< vector< vector<int> > > &trans_nxtS, // state, actions, next states
	vector< vector< vector<double> > > &trans_p, // state, actions, next states
	vector< vector<double> > &reward, // state, action, reward
	vector< vector<double> > &rb, // state, action, reward bonus
	int H,
	double dis_RB,
	double dis_fac
	) {

	vector<double> v1(numStates, 0.0), v2(numStates, 0.0);
	vector<string> policy(numStates, "None");

	for (int i = 0; i < H; i++) {

		for (int s = 0; s < numStates; s++) {

			double max_val_s = -999999.0;
			for (int a = 0; a < trans_nxtS[s].size(); a++) {

				double tmp_futu_v = 0.0;
				for (int nxtS = 0; nxtS < trans_nxtS[s][a].size(); nxtS++)
					tmp_futu_v += trans_p[s][a][nxtS] * v1[ trans_nxtS[s][a][nxtS] ];

				double tmpVal = reward[s][a] + dis_RB * rb[s][a] + dis_fac * tmp_futu_v;

				if (tmpVal > max_val_s) {
					policy[s] = trans_act[s][a];
					max_val_s = tmpVal;
				}

			}

			v2[s] = max_val_s;
		}

		for (int k = 0; k < numStates; k++)
				v2[k] = v1[k];

	}

	return policy;
}
