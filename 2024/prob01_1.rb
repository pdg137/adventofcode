a1 = []
a2 = []
File.open('data01.txt').each do |line|
  line =~ /(\d+)\s+(\d+)/ or raise line
  a1 << $1.to_i
  a2 << $2.to_i
end

a1.sort!
a2.sort!

total = a1.each_index.sum do |i|
  (a1[i] - a2[i]).abs
end

puts total
