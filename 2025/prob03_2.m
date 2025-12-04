silent_functions(1)
f = fopen('data03.txt')
sum = 0
while (s = fgetl(f)) != -1

  num = 0
  last_digit_pos = 0

  for d = 1:12
    num *= 10

    digit = -1
    for i = (last_digit_pos+1):(length(s)-12+d)
      n = str2num(s(i))
      if n > digit
        digit = n
        last_digit_pos = i
      endif
    endfor

    num += digit
  endfor

  sum += num
  #printf("%d\n", num)
endwhile
printf("sum: %d\n", sum)
