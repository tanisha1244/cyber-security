#include<bits/stdc++.h>
using namespace std;
string  encrypt( string a)
{ string result=" ";

  for(int i=0;i<a.length();i++)
  {
  	 if(isupper(a[i]))
  	     { result+=char(int(a[i]+5-65)%26 +65);
  	 	
	      }
	 else
	   {
	   	result+=char(int(a[i]+5-97)%26 +97);
	   }
	  }	
return result;	
}
string  decrypt( string a)
{ string result=" ";
  for(int i=0;i<a.length();i++)
  {
  	 if(isupper(a[i]))
  	     { result+= char(int(a[i]-5-65+26)%26+65);
  	 	
	      }
	 else
	   {
	   	result+=char(int(a[i]-5-97+26)%26+97);
	   }
	  }	
return result;	
}
int main()
{ string s;
cout<<"enter the string"<<endl;
getline(cin,s);
int c;
cout<<"enter the choice"<<endl;
cin>>c;
switch(c)
{ case 0:
	{ cout<<"encrypt is:"<<encrypt( s)<<endl;
	 break;
	}
  case 1:
  	{cout<<"decrypt is:"<<decrypt( s)<<endl;
  	break;
	  }
}


return 0;	}
