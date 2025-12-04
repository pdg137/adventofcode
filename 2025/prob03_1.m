silent_functions(1)
f = fopen('data03.txt')
sum = 0
while (s = fgetl(f)) != -1

  ## first digit: largest digit that is not the last on the line
  first_digit = -1
  first_digit_pos = -1
  for i = 1:(length(s)-1)
    n = str2num(s(i))
    if n > first_digit
      first_digit = n
      first_digit_pos = i
    endif
  endfor

  ## second digit: largest after that
  second_digit = -1
  for i = (first_digit_pos+1):length(s)
    n = str2num(s(i))
    if n > second_digit
      second_digit = n
    endif
  endfor

  sum += first_digit*10+second_digit
  #printf("%d%d\n", first_digit, second_digit)
endwhile
printf("sum: %d\n", sum)
