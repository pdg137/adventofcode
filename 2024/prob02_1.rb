module Enumerable
  def safe?
    diffs = (length-1).times.collect { |i|
      self[i+1] - self[i]
    }

    diffs.all?(1..3) || diffs.all?(-3..-1)
  end
end

score = File.open('data02.txt').count do |line|
  line.split.map(&:to_i).safe?
end

puts score
