score = 0

def safe?(a)
  increasing = (a.length-1).times.all? do |i|
    diff = a[i+1] - a[i]
    [1,2,3].index(diff)
  end

  decreasing = (a.length-1).times.all? do |i|
    diff = a[i+1] - a[i]
    [-3,-2,-1].index(diff)
  end

  increasing || decreasing
end

File.open('data02.txt').each do |line|
  a = line.split.map(&:to_i)

  sequences = [a]

  a.each_index do |i|
    a2 = a.dup
    a2.delete_at(i)
    sequences << a2
  end

  score += 1 if sequences.any? { |s| safe?(s) }
end

puts score
