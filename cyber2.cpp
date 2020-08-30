#include<bits/stdc++.h>
using namespace std;
int main()
{ string s;
 getline(cin,s);
 int n=s.length();
 string a;
 a=s;
 for(int i=0;i<n/2;i++)
   { char t=s[i];
     s[i]=s[n-i-1];
     s[n-i-1]=t;
    }
if(s.compare(a)==0)
{  cout<<"string is palindrome "<<endl;
	}	
else
{ cout<<"string is not a palindrome "<<endl;
	}	
return 0;	
	
	
	
}
