a1 = []
a2 = []
File.open('data01.txt').each do |line|
  line =~ /(\d+)\s+(\d+)/ or raise line
  a1 << $1.to_i
  a2 << $2.to_i
end

a1.sort!
a2.sort!

sum = 0
a1.each do |i|
  d = a2.select { |a| a == i }.length
  puts d
  sum += d * i
end

puts sum
