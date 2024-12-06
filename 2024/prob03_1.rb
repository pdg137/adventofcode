array = []
s = File.open('data03.txt').read

r = /mul\((\d+),(\d+)\)/

score = 0
s.scan(r) do |m|
  score += $1.to_i * $2.to_i
end

puts score
