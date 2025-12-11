set file [open data06.txt]
set homework {}

while {[chan gets $file line] >= 0} {
    set parts [eval concat [split $line]]
    set homework [concat $homework [list $parts]]
}
chan close $file

set ops [lpop homework]
set n_probs [llength $ops]
set n_nums [llength $homework]

set sum 0
for {set prob 0} {$prob < $n_probs} {incr prob} {
    set expr {}
    set op [lindex $ops $prob]
    for {set n 0} {$n < $n_nums} {incr n} {
        set expr [concat $expr [lindex [lindex $homework $n] $prob] $op]
    }
    # gives us e.g. "328 + 64 + 98 +"
    lpop expr
    incr sum [expr $expr]
}
puts $sum
