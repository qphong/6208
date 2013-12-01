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

	vector<double> v[2] = {vector<double>(numStates,0.0), 
		vector<double>(numStates,0.0)};
	vector<string> policy(numStates, "None");
	int i, s, a, nxtS, k, cur;
	double max_val_s, tmp_futu_v, tmpVal;

	cur = 0;
	for (i = 0; i < H; i++) {

		for (s = 0; s < numStates; s++) {

			max_val_s = -999999.0;
			for (a = 0; a < trans_nxtS[s].size(); a++) {

				tmp_futu_v = 0.0;
				for (nxtS = 0; nxtS < trans_nxtS[s][a].size(); nxtS++)
					tmp_futu_v += trans_p[s][a][nxtS] * v[1-cur][ trans_nxtS[s][a][nxtS] ];

				tmpVal = reward[s][a] + dis_RB * rb[s][a] + dis_fac * tmp_futu_v;

				if (tmpVal > max_val_s) {
					policy[s] = trans_act[s][a];
					max_val_s = tmpVal;
				}

			}

			v[cur][s] = max_val_s;
		}

		cur = 1 - cur;

	}

	return policy;
}
