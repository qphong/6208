
%module rsMDPSlv

%include "std_string.i"
%include "std_map.i"
%include "std_vector.i"

namespace std {
	%template(vec_str) vector<string>;

	%template(map_str_vecStr) map<string, vector<string> >;
	%template(map_2str_vecStr) map<string, map<string, vector<string> > >;

	%template(map_str_dbl) map<string,double>;
	%template(map_2str_dbl) map<string, map<string, double> >;
	%template(map_3str_dbl) map<string, map<string, map<string, double> > >;
}

std::map<std::string,std::string> RS_mdp_solver( std::vector<std::string> &states, 
	 std::map<std::string, std::map<std::string, std::vector<std::string> > > &trans_s1, 
	 std::map<std::string, std::map<std::string, std::map<std::string, double> > > &trans_p, 
	 std::map<std::string, std::map<std::string, double> > &reward,
	 std::map<std::string, std::map<std::string, double> > &rb,
	int H,
	double dis_RB);

%{
#include"rsMDPSlv.cpp"	
%}
