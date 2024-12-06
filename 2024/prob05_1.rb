class Rule
  def initialize(a, b)
    @a = a
    @b = b
  end

  def fail?(update)
    i = update.index(@a)
    j = update.index(@b)
    i && j && i >= j
  end
end

rules = []
updates = []
score = 0

File.open('data05.txt').each do |line|
  if line =~ /(\d+)\|(\d+)/
    rules << Rule.new($1.to_i, $2.to_i)
  elsif line =~ /\d/
    updates << line.split(',').map(&:to_i)
  end
end

updates.each do |update|
  next if rules.any? { |rule|
    rule.fail?(update)
  }

  score += update[(update.length-1)/2]
end

puts score
