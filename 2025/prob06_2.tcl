set file [open data06.txt]
set homework {}

set homework {}
set chars {}
set c [chan read $file 1]
while {![chan eof $file]} {
    if {$c == "\n"} {
        set homework [concat $homework [list $chars]]
        set chars {}
    } elseif {$c == " "} {
        set chars [concat $chars {{}}]
    } else {
        set chars [concat $chars $c]
    }
    set c [chan read $file 1]
}
chan close $file

set ops [eval concat [lpop homework]]
# * + * +

set rows [llength $homework]
set cols [llength [lindex $homework 0]]

set sum 0
set col 0
set current_problem {}
set current_op [lpop ops 0]
for {set col 0} {$col < $cols} {incr col} {

    set current_term {}
    for {set row 0} {$row < $rows} {incr row} {
        set digit [lindex [lindex $homework $row] $col]
        set current_term [join [list $current_term $digit] ""]
    }

    if {$current_term != {}} {
        lappend current_problem $current_term
        lappend current_problem $current_op
    } else {
        # starting a new problem
        lpop current_problem
        incr sum [expr $current_problem]
        set current_problem {}
        set current_op [lpop ops 0]
    }
}
lpop current_problem
incr sum [expr $current_problem]
puts $sum
