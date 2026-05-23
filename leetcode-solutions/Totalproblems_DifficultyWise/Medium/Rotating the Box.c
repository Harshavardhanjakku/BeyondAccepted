# Rotating the Box
# Difficulty: Medium
# Language: c

char** rotateTheBox(char** boxGrid,int boxGridSize,int* boxGridColSize,int* returnSize,int** returnColumnSizes){
    int rows=boxGridSize;
    int cols=boxGridColSize[0];

    for(int row=0;row<rows;row++){
        int empty=cols-1;

        for(int col=cols-1;col>=0;col--){
            if(boxGrid[row][col]=='*'){
                empty=col-1;
            }
            else if(boxGrid[row][col]=='#'){
                boxGrid[row][col]='.';
                boxGrid[row][empty]='#';
                empty--;
            }
        }
    }

    *returnSize=cols;

    *returnColumnSizes=(int*)malloc(cols*sizeof(int));
    for(int i=0;i<cols;i++){
        (*returnColumnSizes)[i]=rows;
    }

    char** res=(char**)malloc(cols*sizeof(char*));

    for(int i=0;i<cols;i++){
        res[i]=(char*)malloc((rows+1)*sizeof(char));
    }

    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            res[j][rows-1-i]=boxGrid[i][j];
        }
    }

    for(int i=0;i<cols;i++){
        res[i][rows]='\0';
    }

    return res;
}
