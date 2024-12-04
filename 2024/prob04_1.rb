array = []
File.open('data04.txt').each do |line|
  array << line.split(//)
end

def safe_get(array, p)
  case
  when p[0] < 0 || p[0] >= array[0].length
    nil
  when p[1] < 0 || p[1] >= array.length
    nil
  else
    array[p[1]][p[0]]
  end
end

def matches(array, coords)
  'X' == safe_get(array, coords[0]) &&
    'M' == safe_get(array, coords[1]) &&
    'A' == safe_get(array, coords[2]) &&
    'S' == safe_get(array, coords[3])
end

score = 0
array.each_index do |y|
  array[0].each_index do |x|
    [[1, 0], [1, 1], [0, 1], [-1, 1],
     [-1, 0], [-1, -1], [0, -1], [1, -1]].each do |dx, dy|
      if matches(array, [[x,y], [x+dx,y+dy], [x+2*dx,y+2*dy], [x+3*dx,y+3*dy]])
        score = score + 1
      end
    end
  end
end

puts score
