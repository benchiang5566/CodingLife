/// week09-1.cpp
/// LeetCode 38. Count and Say 數字連續出現，就模依 RLE 方法「編碼」成「數字+字母」的形式
class Solution {
public:
    string countAndSay(int n) {
        if(n==1) return "1"; /// 最簡單的CASE，如果1回傳"1"
        string prev = countAndSay(n-1);/// 函式呼叫函式 大問題變成小問題
        string ans = "";
        char prevC = prev[0]; /// 前一個字母，累計出現多次
        int prevN = 1;

        for(int i=1; i<prev.length(); i++){
            if(prevC == prev[i]) prevN++; /// 相同就加 1
            else{
                ans+= string(to_string(prevN)) + prevC; /// 出現幾次 + 哪個字母(送出之前累計的字母)
                prevC = prev[i]; /// 新的字母
                prevN = 1; /// 從 1 開始(新的字母，有 1 個)
            }
        }

        ans += string(to_string(prevN)) + prevC;
        return ans;

    }
};
