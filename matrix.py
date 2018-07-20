import random

from copy import deepcopy

class Matrix:

    def __init__(self, nrows, ncols):
        self.nrows=nrows
        self.ncols=ncols
        self.matrix=[]
        for i in range(self.nrows):
            row=[]
            for j in range(self.ncols):
                row.append(random.randint(0,9))
            self.matrix.append(row)

    def add(self, m):
        if self.nrows!=m.nrows or self.ncols!=m.ncols:
            print("Matrixs's size should be in the same size")
        else:
            matrixA=self.matrix
            matrixB=m.matrix
            new=Matrix(self.nrows,self.ncols)
            for i in range(self.nrows):
                for j in range(self.ncols):
                    new.matrix[i][j]=matrixA[i][j]+matrixB[i][j]
            return new.display()

    def sub(self, m):
        if self.nrows!=m.nrows or self.ncols!=m.ncols:
            print("Matrixs's size should be in the same size")
        else:
            matrixA=self.matrix
            matrixB=m.matrix
            new=Matrix(self.nrows,self.ncols)
            for i in range(self.nrows):
                for j in range(self.ncols):
                    new.matrix[i][j]=matrixA[i][j]-matrixB[i][j]
            return new.display()

    def mul(self, m):
        matrixA=self.matrix
        matrixB=m.matrix
        new=Matrix(self.nrows,m.ncols)
        new.nrows=self.nrows
        new.ncols=m.ncols
        for i in range(self.nrows):
            for j in range(m.ncols):
                total=0
                for k in range(m.nrows):
                    newsum=0
                    newsum=matrixA[i][k]*matrixB[k][j]
                    total=total+newsum
                new.matrix[i][j]=total    
        return new

    def transpose(self):
        matrixA=self.matrix
        new=Matrix(self.ncols,self.nrows)
        for i in range(self.nrows):
            for j in range(self.ncols):
                new.matrix[j][i]=matrixA[i][j]    
        return new

    def display(self):
        for i in range(self.nrows):
            for j in range(self.ncols):
                print(self.matrix[i][j],end=' ')
            print(end='\n')
        print(end='\n')



Ar=int(input('輸入A矩陣行數:'))
Ac=int(input('輸入A矩陣行數:'))
print('MatrixA(',Ar,Ac,')')
A=Matrix(Ar,Ac)
A.display()

Br=int(input('輸入A矩陣行數:'))
Bc=int(input('輸入A矩陣行數:'))
print('MatrixA(',Br,Bc,')')
B=Matrix(Br,Bc)
B.display()

print('='*10,'A+B','='*10)
C=A.add(B)

print('='*10,'A-B','='*10)
D=A.sub(B)

print('='*10,'A*B','='*10)
E=A.mul(B)
E.display()

print('='*5,'The transpose of A+B','='*5)
F=E.transpose()
F.display()
