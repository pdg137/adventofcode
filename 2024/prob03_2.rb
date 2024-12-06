array = []
s = File.open('data03.txt').read

r = /(don't\(\)|do\(\)|mul\((\d+),(\d+)\))/

score = 0
dont = false
s.scan(r) do |m|
  case $1
  when "don't()"
    dont = true
  when "do()"
    dont = false
  else
    score += $2.to_i * $3.to_i unless dont
  end
end

puts score
