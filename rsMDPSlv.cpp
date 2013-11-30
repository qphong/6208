#include <string>
#include <map>
#include <vector>

using namespace std;

map<string,string> RS_mdp_solver(vector<string> &states, 
	map<string, map<string, vector<string> > > &trans_s1,
	map<string, map<string, map<string, double> > > &trans_p, 
	map<string, map<string, double> > &reward,
	map<string, map<string, double> > &rb,
	int H,
	double dis_RB) {

	map<string,double> val1, val2;
	map<string,string> policy;

	for (vector<string>::const_iterator i = states.begin(); i != states.end(); i++) {
		val1.insert(pair<string,double>(*i, 0.0));
		val2.insert(pair<string,double>(*i, 0.0));
		policy.insert(pair<string,string>(*i, "None"));
	}

	for (int i = 0; i < H; i++) {

		for (vector<string>::const_iterator s = states.begin(); s != states.end(); s++) {

			double max_val_s = -99999.0;
			for (map<string, vector<string> >::const_iterator a = trans_s1[*s].begin(); a != trans_s1[*s].end(); a++) {

				double tmp_futu_v = 0.0;
				for (vector<string>::const_iterator nxtS = a->second.begin(); nxtS != a->second.end(); nxtS++)
					tmp_futu_v += trans_p[*s][a->first][*nxtS] * val1[*nxtS];
				
				double tmpVal = reward[*s][a->first] + dis_RB * rb[*s][a->first] + tmp_futu_v;

				if (tmpVal > max_val_s) {
					policy[*s] = a->first;
					max_val_s = tmpVal;
				}

			}

			val2[*s] = max_val_s;

		}

		for (vector<string>::const_iterator s = states.begin(); s != states.end(); s++)
			val1[*s] = val2[*s];
	
	}

	return policy;

}

