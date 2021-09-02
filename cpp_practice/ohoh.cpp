#include <iostream>
#include <string>
//#include <wstring>
#include <stdio.h>
#include <locale>
#include <codecvt>

using namespace std;


// convert wstring to UTF-8 string
string wstring_to_utf8 (const wstring& str)
{
    wstring_convert<codecvt_utf8<wchar_t>> myconv;
    return myconv.to_bytes(str);
}

int main(){
    wstring str1 = L"我是中文";
    printf("%i\n", str1[0]);
    cout << wstring_to_utf8(str1) << endl;
}
