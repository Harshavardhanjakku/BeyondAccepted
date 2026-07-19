# Problem: Sum of Digits of String After Convert
# Difficulty: Easy
# Topic: String
# Language: c
# Submission: 1

int getLucky(char* s,int k){
    int res=0;

    for(int i=0;s[i]!='\0';i++){
        int r=s[i]-'a'+1;

        if(r<10){
            res+=r;
        }
        else{
            res+=(r/10)+(r%10);
        }
    }

    k--;

    while(k--){
        int tot=0;

        while(res>0){
            tot+=res%10;
            res/=10;
        }

        res=tot;
    }

    return res;
}
