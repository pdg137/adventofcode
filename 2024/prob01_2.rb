a1 = []
a2 = []
File.open('data01.txt').each do |line|
  line =~ /(\d+)\s+(\d+)/ or raise line
  a1 << $1.to_i
  a2 << $2.to_i
end

total = a1.each.sum do |x|
  x * a2.grep(x).length
end

puts total
