STOP_AT = 1000

f = io.open("data08.txt", "r")

points = {}

line = f:read()
while line ~= nil do
  xyz = {}
  for str in string.gmatch(line, "([0-9]+)") do
    table.insert(xyz, str)
  end

  table.insert(points, xyz)
  line = f:read()
end

function dist2(i, j)
  x1 = points[i][1]
  y1 = points[i][2]
  z1 = points[i][3]

  x2 = points[j][1]
  y2 = points[j][2]
  z2 = points[j][3]

  return (x1-x2)^2 + (y1-y2)^2 + (z1-z2)^2
end

distances = {}
groups = {}

for i = 1, #points do
  -- put i in a group consisting of 1 point
  table.insert(groups, {i})

  for j = i+1, #points do
    -- get the distance from i to j (without duplicates)
    table.insert(distances, {i, j, dist2(i,j)})
  end
end

function comp(d1, d2)
  return d1[3] < d2[3]
end

table.sort(distances, comp)

function find_group(i)
  for k, g in pairs(groups) do
    found = false
    for unused, l in pairs(g) do
      if l == i then
        return k
      end
    end
  end

  error(i.." not found in a group")
end

function negsize(x, y)
  return #x > #y
end

function show()
  table.sort(groups, negsize)

  for unused, g in pairs(groups) do
    print(table.concat(g, ","))
  end

end

count = 0
for unused, d in pairs(distances) do
  i = d[1]
  j = d[2]

  -- find the groups
  i_group_index = find_group(i)
  j_group_index = find_group(j)

  print("Connecting "..i.." to "..j..": "..d[3].." "..i_group_index.." "..j_group_index)

  -- if they are the same, don't do anything!
  if i_group_index ~= j_group_index then

    -- remove j
    j_group = table.remove(groups, j_group_index)

    -- move it to i
    i_group_index = find_group(i)
    i_group = groups[i_group_index]
    for unused, k in pairs(j_group) do
      table.insert(i_group, k)
    end
  end

  count = count + 1
  if #groups == 1 then
    break
  end
end

show()

x1 = points[i][1]
x2 = points[j][1]
print("Product of last two: "..x1.." * "..x2.." = "..x1*x2)