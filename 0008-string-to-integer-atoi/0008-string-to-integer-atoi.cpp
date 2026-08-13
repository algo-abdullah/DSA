class Solution {
public:
    int myAtoi(string s) {
        int sign = 1;
        int i = 0;
        long long num = 0;
        while (i < s.size() && s[i] == ' ')
           { i++;}
        if (i < s.size() && s[i] == '-' || s[i] == '+') 
        {
            sign = (s[i] == '-' )? -1 : 1;
            i++;
        }
        while (i < s.size() && isdigit(s[i]))
        {
            int digit = s[i] - '0';
            num = num * 10 + digit;

            if (sign == 1 && num > INT_MAX)
                return INT_MAX;
            if (sign == -1 && (-num) < INT_MIN)
                return INT_MIN;
            i++;
        }
        return sign * num;
    }
};
