10 REM First get dimensions
20 OPEN "D:\DATA04.TXT" FOR INPUT AS #1
30 H = 0
40 PRINT "CHECKING SIZE..."
50 WHILE NOT EOF(1)
60     PRINT H
70     LINE INPUT# 1, L$
80     W = LEN(L$)
90     H = H + 1
100 WEND
110 CLOSE

120 REM Pad so we don't have to worry about
130 REM going off the edges.
140 W = W + 2
150 H = H + 2

160 REM Read data into array
170 OPEN "D:\DATA04.TXT" FOR INPUT AS #1
180 PRINT "READING DATA..."
190 DIM A%(W,H)
200 FOR Y = 1 TO H-2
210     PRINT Y
220     LINE INPUT# 1, L$
230     FOR X = 1 TO W-2
240         C$ = MID$(L$, X, 1)
250         A%(X,Y) = C$="@"
260     NEXT X
270 NEXT Y
280 CLOSE

290 REM calculate!
300 T=0
310 PRINT "Calculating..."
320 REMOVED = 1
330 WHILE REMOVED > 0
340     REMOVED = 0 : REM we'll be done if we don't find any
350     FOR Y = 1 TO H-2
360         PRINT Y
370         FOR X = 1 TO W-2
380             C = A%(X-1,Y) + A%(X,Y-1) + A%(X+1,Y) + A%(X,Y+1)
390             C = C + A%(X-1,Y-1) + A%(X+1,Y-1) + A%(X+1,Y+1) + A%(X-1,Y+1)
400             IF A%(X,Y) AND C > -4 THEN T = T+1 : A%(X,Y)=0 : REMOVED = REMOVED+1
410         NEXT X
420     NEXT Y
430     PRINT "Removed " REMOVED
440 WEND

450 PRINT "Final sum:", T
460 INPUT "PRESS ANY KEY...", I
470 SYSTEM
