#include <iostream>
#include <vector>

using namespace std;

void print_vec(vector<int> &v){
  for(auto &i : v){
    cout<<i<<" ";
  }
  cout<<endl;
}

void print_char_vec(vector<char>&v){
  for(auto &i : v){
    cout<<i<<" ";
  }
  cout<<endl;
}
int main(){
  int n = 21;
  vector<int> v;
  cout<<"vector : \n";
  for(int i = 0;i<n;i++){
    int x;
    cin>>x;
    v.push_back(x);
  }
  print_vec(v);
  for(auto &i : v){
    i+=96;
  }
  print_vec(v);
  vector<char> ans;
  for(auto &i: v){
    char c = (char)i;
    ans.push_back(c);
  }
  print_char_vec(ans);
  return 0;
}
