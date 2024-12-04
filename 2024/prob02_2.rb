safe = lambda do |a|
  diffs = (a.length-1).times.collect { |i|
    a[i+1] - a[i]
  }

  diffs.all?(1..3) || diffs.all?(-3..-1)
end

score = File.open('data02.txt').count do |line|
  a = line.split.map(&:to_i)

  sequences = a.each_index.collect do |i|
    a.dup.tap { |a2| a2.delete_at(i) }
  end

  sequences.any? safe
end

puts score
