array = []
guard = nil
dir = [0, -1]
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
  array[pos[1]] && array[pos[1]][pos[0]]
end

def turn(dir)
  [
    -dir[1],
    dir[0]
  ]
end

visited = {}
while get(array, guard)
  visited[guard] = true

  ahead = move(guard, dir)
  while get(array, ahead) == '#'
    dir = turn(dir)
    ahead = move(guard, dir)
  end

  guard = ahead
end
puts visited.keys.length
