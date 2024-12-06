array = []
guard = nil
File.open('data06.txt').each do |line|
  array << line.strip.split(//)
  if x = array.last.index('^')
    guard = [x, array.length - 1]
  end
end

def move(pos, dir)
  [
    pos[0] + dir[0],
    pos[1] + dir[1]
  ]
end

def get(array, pos)
  pos[0] >= 0 && pos[1] >= 0 &&
    array[pos[1]] && array[pos[1]][pos[0]]
end

def turn(dir)
  [
    -dir[1],
    dir[0]
  ]
end

class LoopError < RuntimeError
end

def check(array, guard)
  visited = {}
  dir = [0, -1]

  while get(array, guard)
    visited[guard] ||= {}
    raise LoopError.new if visited[guard][dir]
    visited[guard][dir] = true

    ahead = move(guard, dir)
    while get(array, ahead) == '#'
      dir = turn(dir)
      ahead = move(guard, dir)
    end

    guard = ahead
  end
  visited.keys.length
end

score = 0
array.each_index do |y|
  puts "#{y} of #{array.length-1}..."
  array[0].each_index do |x|
    new_array = Marshal.load(Marshal.dump(array))
    next if new_array[y][x] != '.'
    new_array[y][x] = '#'
    begin
      check(new_array, guard)
    rescue LoopError
      puts "#{x},#{y}"
      # loop!
      score += 1
    end
  end
end

puts score
