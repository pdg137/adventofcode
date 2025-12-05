10 REM First get dimensions
20 OPEN "D:\DATA04.TXT" FOR INPUT AS #1
30 H = 0
40 WHILE NOT EOF(1)
50     LINE INPUT# 1, L$
60     W = LEN(L$)
70     H = H + 1
80 WEND
90 CLOSE

100 REM Pad so we don't have to worry about
110 REM going off the edges.
120 W = W + 2
130 H = H + 2

140 REM Read data into array
150 OPEN "D:\DATA04.TXT" FOR INPUT AS #1
160 DIM A%(W,H)
170 FOR Y = 1 TO H-2
180     LINE INPUT# 1, L$
190     FOR X = 1 TO W-2
200         C$ = MID$(L$, X, 1)
210         A%(X,Y) = C$="@"
220     NEXT X
230 NEXT Y
240 CLOSE

250 REM calculate!
260 T=0
270 FOR Y = 1 TO H-2
280     FOR X = 1 TO W-2
290         C = A%(X-1,Y) + A%(X,Y-1) + A%(X+1,Y) + A%(X,Y+1)
300         C = C + A%(X-1,Y-1) + A%(X+1,Y-1) + A%(X+1,Y+1) + A%(X-1,Y+1)
310         IF A%(X,Y) AND C > -4 THEN T = T+1
320     NEXT X
330 NEXT Y

340 PRINT T
350 INPUT "PRESS ANY KEY...", I
360 SYSTEM
