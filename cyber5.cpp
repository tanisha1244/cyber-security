#include<bits/stdc++.h>
using namespace std;
void message(string b, int n)
{ int c=1;
char a=97;
for(int i=0;i<n;i++)
  { c=1+b[i]-a;
    if(c==0)
      { cout<<"#";
	  }
  	else
  	{ for(int j=1;j<=c;j++)
  	    if(c%2==0)
  	     { cout<<"$";
		   }
		else 
		 { cout<<"#";
		 }
  	}
  }
}
int main()
{string s;
cout<<"enter the string"<<endl;
getline(cin,s);
int n;
n=s.length();
message(s,n);
return 0;
}
