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

def matches(array, center, m1, m2, s1, s2)
  'A' == safe_get(array, center) &&
    'M' == safe_get(array, m1) &&
    'M' == safe_get(array, m2) &&
    'S' == safe_get(array, s1) &&
    'S' == safe_get(array, s2)
end

score = 0
array.each_index do |y|
  array[0].each_index do |x|
    ul = [x-1,y-1]
    bl = [x-1,y+1]
    ur = [x+1,y-1]
    br = [x+1,y+1]

    if matches(array, [x,y], ul, bl, br, ur)
      score = score + 1
    end
    if matches(array, [x,y], ur, ul, bl, br)
      score = score + 1
    end
    if matches(array, [x,y], br, ur, ul, bl)
      score = score + 1
    end
    if matches(array, [x,y], bl, br, ur, ul)
      score = score + 1
    end
  end
end

puts score
