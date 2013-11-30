
%module rsMDPSlvi

%include "std_string.i"
%include "std_vector.i"

namespace std {
	%template(vec1i) vector<int>;
	%template(vec2i) vector< vector<int> >;
	%template(vec3i) vector< vector< vector<int> > >;

	%template(vec1s) vector<string>;
	%template(vec2s) vector< vector<string> >;

	%template(vec1d) vector<double>;
	%template(vec2d) vector< vector<double> >;
	%template(vec3d) vector< vector< vector<double> > >;
}

std::vector<std::string> RS_mdp_solver(int numStates,
	std::vector< std::vector<string> > &trans_act,
	std::vector< std::vector< std::vector<int> > > &trans_nxtS,
	std::vector< std::vector< std::vector<double> > > &trans_p,
	std::vector< std::vector<double> > &reward,
	std::vector< std::vector<double> > &rb,
	int H,
	double dis_RB,
	double dis_fac
	);

%{
#include "rsMDPSlvi.cpp"	
%}
