# Asintment 2
messi_score = int(input('Enter the score of points Messi scored: '))
ronaldo_score = int(input('Enter the score of points Ronaldo scored:'))
neymar_score = int(input('Enter the score of points Neymar scored:'))
if neymar_score < messi_score > ronaldo_score:
    print('messi won!')
elif neymar_score < ronaldo_score > messi_score:
    print('ronaldo won!')
elif ronaldo_score < neymar_score > messi_score:
    print('neymar won!')
else:
    print("It's not a clear win !?")

# 70, 80, 70 ronaldo